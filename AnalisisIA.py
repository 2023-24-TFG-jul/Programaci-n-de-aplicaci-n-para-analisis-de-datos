#Nombre:AnalisisIA
#Autor:Álvaro Villar Val
#Fecha:9/06/24
#Versión:0.7.0
#Descripción: Apliación de inteligencia artificial para el análisis de datos resultantes de la central meteorológica
#########################################################################################################################
#Definimos los imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from Calculadora import Calculadora
from BaseDatosLvl2 import BaseDatosLvl2
from pysolar.solar import *
import math
from sklearn.preprocessing import MinMaxScaler


class AnalisisIA:

    fechaini="00-00-00"
    fechafin="99-01-30"

    def __init__(self):
        self.base_datos =BaseDatosLvl2()
        self.calc=Calculadora()
    
        with open('setting.txt', 'r') as file:
              self.fechaUltimAct = float(file.read())
        self.longitude=-3.6879829504876676
        self.latitude=42.3515619402223
              

    def analisis(self, colum, numin, titulo, flags):
        # Supongamos que tus datos están en un archivo CSV

        col = "TIMESTAMP," + colum[0] + "," + colum[1] + "," + colum[2] + ",fallo,date"
        
        dataAll = self.base_datos.obtenerdat(col, "radioproc", self.fechaini, self.fechafin)
        max_date = dataAll['date'].max()
        #with open('setting.txt', 'w') as file:
        #      file.write(str(max_date))
        # Filtrar las filas de 'fallo' que contienen los flags
        dataAll['fallo'] = dataAll['fallo'].str.slice(numin, numin+3)
        print(dataAll.shape)
        for flag in flags:
            dataAll = dataAll[~dataAll['fallo'].str.contains(flag)]
        print(dataAll.shape)
        dataAll = dataAll.dropna()
        print(dataAll.shape)
        # Calculamos la fecha de manera que se pueda introducir en la función de pysolar
        dataAll["TIMESTAMP"] = dataAll[["TIMESTAMP"]].apply(lambda row: self.calc.dates(row["TIMESTAMP"]), axis=1)
        # Calculamos la suma de la irradiancia difusa y directa multiplicada por el coseno del ángulo de incidencia
        dataAll["Suma Difusa y directa"] = dataAll[[colum[1], colum[2], "TIMESTAMP"]].apply(
            lambda row: row[colum[1]] + row[colum[2]] * math.cos(math.radians(90 - get_altitude(self.latitude, self.longitude, row["TIMESTAMP"]))), axis=1)
        dataAll["angle"] = dataAll[["TIMESTAMP"]].apply(lambda row: 90 - get_altitude(self.latitude, self.longitude, row["TIMESTAMP"]), axis=1)
        data = dataAll[dataAll['date'] < self.fechaUltimAct]
        new_data = dataAll[dataAll['date'] > self.fechaUltimAct]

        # Separar características y la variable objetivo
        X = data[[colum[1], colum[2]]]
        y = data[[colum[0],"Suma Difusa y directa","angle"]]
        # Normalizar los datos
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)



        # Dividir los datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        y_train = y_train[colum[0]]
        ysuma=y_test[["Suma Difusa y directa","angle"]]
        y_test = y_test[colum[0]]
        
        # Definir el modelo
        model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', max_iter=1000,random_state=42)

        # Entrenar el modelo
        model.fit(X_train, y_train)

        # Hacer predicciones
        preds_test = model.predict(X_test)
        r2 = r2_score(y_test, preds_test)
        print("Estudio con datos antinguos\n")
        print(f"R^2: {r2}")
        # Evaluar el modelo
        rmse = np.sqrt(mean_squared_error(y_test, preds_test))
        print(f"RMSE: {rmse}")

        # Calcular el nRMSE (RMSE normalizado)
        nrmse = rmse / (y_test.max() - y_test.min())
        print(f"nRMSE: {nrmse}")            

        # Calcular el MBE (Mean Bias Error)
        mbe = np.mean(preds_test - y_test)
        print(f"MBE: {mbe}")

        # Calcular el nMBE (MBE normalizado)
        nmbe = mbe / (y_test.max() - y_test.min())
        print(f"nMBE: {nmbe}")

        # Preprocesar nuevos datos
        X_new = new_data[[colum[1], colum[2]]]
        y_new = new_data[colum[0]]
        X_new_scaled = scaler.transform(X_new)
        # Aplicar PCA a los nuevos datos
    

        # Combinar datos antiguos y nuevos
        X_combined = np.vstack((X_train, X_new_scaled))
        y_combined = np.hstack((y_train, y_new))

        # Retrain el modelo con datos combinados
        model.fit(X_combined, y_combined)

        # Hacer predicciones nuevamente
        preds_combined_test = model.predict(X_test)

        # Evaluar el modelo retrain
        print("Estudio con todos los datos\n")
        r2 = r2_score(y_test, preds_combined_test)
        print(f"R^2: {r2}")
        # Evaluar el modelo
        rmse = np.sqrt(mean_squared_error(y_test, preds_combined_test))
        print(f"RMSE: {rmse}")

        # Calcular el nRMSE (RMSE normalizado)
        nrmse = rmse / (y_test.max() - y_test.min())
        print(f"nRMSE: {nrmse}")            

        # Calcular el MBE (Mean Bias Error)
        mbe = np.mean(preds_combined_test - y_test)
        print(f"MBE: {mbe}")

        # Calcular el nMBE (MBE normalizado)
        nmbe = mbe / (y_test.max() - y_test.min())
        print(f"nMBE: {nmbe}")




        y_tests = ysuma[["Suma Difusa y directa","angle"]]
        y_tests[colum[0]] = y_test.values
        preds_tests = ysuma[["Suma Difusa y directa","angle"]]
        preds_tests[colum[0]] = preds_test
        preds_combined_tests = ysuma[["Suma Difusa y directa","angle"]]
        preds_combined_tests[colum[0]] = preds_combined_test
        y_test_AmanAtar=y_tests[y_tests['angle']>60]
        y_test_gen=y_tests[y_tests['angle']<60]
        preds_test_AmanAtar=preds_tests[preds_tests['angle']>60]
        preds_test_gen=preds_tests[preds_tests['angle']<60]
        preds_combined_test_AmanAtar=preds_combined_tests[preds_combined_tests['angle']>60]
        preds_combined_test_gen=preds_combined_tests[preds_combined_tests['angle']<60]
        #Graficar resultados después del retrain
        plt.figure(figsize=(13, 4))
        plt.plot(y_test_AmanAtar[colum[0]],y_test_AmanAtar["Suma Difusa y directa"], 'o',color='#EB1515', label='Measured Azimuth>60')
        plt.plot(y_test_gen[colum[0]],y_test_gen["Suma Difusa y directa"], 'o',color='#A91C00', label='Measured Azimiuth<60')
        plt.plot(preds_test_AmanAtar[colum[0]],preds_test_AmanAtar["Suma Difusa y directa"], 'o',color='#5CEC0F', label='Historic prediction')
        plt.plot(preds_test_gen[colum[0]],preds_test_gen["Suma Difusa y directa"], 'o',color='#5CEC0F')
        plt.plot(preds_combined_test_AmanAtar[colum[0]],preds_combined_test_AmanAtar["Suma Difusa y directa"], 'o',color='#0D49F7', label='Recent prediction')
        plt.plot(preds_combined_test_gen[colum[0]],preds_combined_test_gen["Suma Difusa y directa"], 'o',color='#0D49F7')
        plt.xlabel('Global Horizontal(W/m^2)')
        plt.ylabel('Sum of diffuse and direct (W/m^2)')
        plt.legend()
        
        plt.title(titulo)
        plt.show()


        # Asegúrate de que la columna 'TIMESTAMP' esté en formato de datetime
        dataAll['TIMESTAMP'] = pd.to_datetime(dataAll['TIMESTAMP'])

        # Extraer la hora del día y el día
        dataAll['HOUR'] = dataAll['TIMESTAMP'].dt.hour
        dataAll['DATE'] = dataAll['TIMESTAMP'].dt.date

        # Crear un nuevo DataFrame para almacenar los valores por hora
        result_df = pd.DataFrame()

        # Iterar sobre cada hora del día (0 a 23) y almacenar los valores en nuevas columnas
        for hour in range(24):
            # Filtrar datos para la hora actual
            hour_values = dataAll[dataAll['HOUR'] == hour].copy()
            if not hour_values.empty:
                # Agrupar por fecha para mantener los valores diarios juntos
                hour_values_grouped = hour_values.groupby('DATE').apply(lambda x: x.reset_index(drop=True)).reset_index(drop=True)
                # Renombrar la columna de interés
                col_name = hour
                hour_values_grouped.rename(columns={colum[0]: col_name}, inplace=True)
                # Añadir los valores al DataFrame resultante
                if col_name in hour_values_grouped:
                    result_df = pd.concat([result_df, hour_values_grouped[[col_name]]], axis=1)
                else:
                    # Manejar el caso donde la columna no exista
                    print(f"Warning: {col_name} not found in hour_values_grouped")
        print(result_df.shape)
        result_df.boxplot(figsize=(15, 5))
        plt.title(titulo)
        plt.ylabel('GH (W/m^2)')
        plt.xlabel('Hour of the day')
        plt.show()

    

    def analisiIrra(self):
        self.analisis(["BuRaGH_Avg","BuRaDH_Avg","BuRaB_Avg"],0,"Analisís de la Irradiancia Todo",['0'])
        self.analisis(["BuRaGH_Avg","BuRaDH_Avg","BuRaB_Avg"],0,"Analisís de la Irradiancia Fisico",['0','2'])
        self.analisis(["BuRaGH_Avg","BuRaDH_Avg","BuRaB_Avg"],0,"Analisís de la Irradiancia ClearSky",['0','2''3','4'])
        self.analisis(["BuRaGH_Avg","BuRaDH_Avg","BuRaB_Avg"],0,"Analisís de la Irradiancia Coherencia",['0','2','3','4','5','6'])

    def analisiIlum(self):
        self.analisis(["BuLxGH_Avg","BuLxDH_Avg","BuLxB_Avg"],3,"Analisís de la iluminancia Todo",['0'])
        self.analisis(["BuLxGH_Avg","BuLxDH_Avg","BuLxB_Avg"],3,"Analisís de la iluminancia Fisico",['0','2'])
        self.analisis(["BuLxGH_Avg","BuLxDH_Avg","BuLxB_Avg"],3,"Analisís de la iluminancia ClearSky",['0','2''3','4'])
        self.analisis(["BuLxGH_Avg","BuLxDH_Avg","BuLxB_Avg"],3,"Analisís de la iluminancia Coherencia",['0','2','3','4','5','6'])
        
    def analsisPar(self):
        self.analisis(["BuPaGH_Avg","BuPaDH_Avg","BuPaB_Avg"],6,"Analisís de la Par Todo",['0'])
        self.analisis(["BuPaGH_Avg","BuPaDH_Avg","BuPaB_Avg"],6,"Analisís de la Par Fisico",['0','2'])
        self.analisis(["BuPaGH_Avg","BuPaDH_Avg","BuPaB_Avg"],6,"Analisís de la Par ClearSky",['0','2','3','4'])
        self.analisis(["BuPaGH_Avg","BuPaDH_Avg","BuPaB_Avg"],6,"Analisís de la Par Coherencia",['0','2','3','4','5','6'])
    def analisiUv(self):
        self.analisis(["BuUvGH_Avg","BuUvDH_Avg","BuUvB_Avg"],9,"Analisís de la Uv Todo",['0'])
        self.analisis(["BuUvGH_Avg","BuUvDH_Avg","BuUvB_Avg"],9,"Analisís de la Uv Fisico",['2'])
        self.analisis(["BuUvGH_Avg","BuUvDH_Avg","BuUvB_Avg"],9,"Analisís de la Uv ClearSky",['0','2','3','4'])
        self.analisis(["BuUvGH_Avg","BuUvDH_Avg","BuUvB_Avg"],9,"Analisís de la Uv Coherencia",['0','2','3','4','5','6'])

#anal=AnalisisIA()
#anal.analisiIrra()