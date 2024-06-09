#Nombre:AnalisisIA
#Autor:Álvaro Villar Val
#Fecha:9/06/24
#Versión:0.1.0
#Descripción: Apliación de inteligencia artificial para el análisis de datos resultantes de la central meteorológica
#########################################################################################################################
#Definimos los imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from Calculadora import Calculadora
from BaseDatosLvl2 import BaseDatosLvl2
from pysolar.solar import *
import math

class AnalisisIA:

    def __init__(self, base_datos):
        self.base_datos = base_datos
        self.calc=Calculadora()
        #with open('setting.txt', 'r') as file:
        #       self.fechaUltimAct = float(file.read())
        self.fechaUltimAct="11-11-2023"
        self.longitude=-3.6879829504876676
        self.latitude=42.3515619402223
              

    def analisis(self,colum,numin):
        # Supongamos que tus datos están en un archivo CSV

        col="TIMESTAMP,"+colum[0]+","+colum[1]+","+colum[2]+",fallo"
        
        #Obtenemos los datos de la base de datos partiendo del inicio de los tiempos hasta el siglo 31
        data=self.base_datos.obtenerdat(col,"radioproc","00-00-0000",self.fechaUltimAct)
        #nos quedamos con las parte del fallo que nos interesa
        data['fallo'] = data['fallo'].str.slice(numin, numin+3)
        data = data[data["fallo"] != "000"]
        data=data.dropna()
        #Calculamos la fecha de manera que se pueda introducir en la función de pysolar
        data["TIMESTAMP"] =data[["TIMESTAMP"]].apply(lambda row :self.calc.dates(row["TIMESTAMP"]),axis=1)
        #Calculamos la suma de la irradiancia difusa y directa multiplicada por el coseno del angulo de incidencia
        data["Suma Difusa y directa"] = data[[colum[1],colum[2],"TIMESTAMP"]].apply(lambda row :row[colum[1]]+row[colum[2]]*math.cos(math.radians(90-get_altitude(self.latitude, self.longitude, row["TIMESTAMP"]))),axis=1)


       
        # Separar características y la variable objetivo
        X = data[[colum[0],colum[1],colum[2]]]
        y = data["Suma Difusa y directa"]  

        # Normalizar los datos
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Dividir los datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # Definir el modelo
        model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', max_iter=500)

        # Entrenar el modelo
        model.fit(X_train, y_train)

        # Hacer predicciones
        preds_train = model.predict(X_train)
        preds_test = model.predict(X_test)

        # Evaluar el modelo
        train_loss = mean_squared_error(y_train, preds_train)
        test_loss = mean_squared_error(y_test, preds_test)

        print(f"Train Loss: {train_loss}")
        print(f"Test Loss: {test_loss}")

        # Graficar resultados
        plt.figure(figsize=(12, 6))
        plt.plot(y_test.values, label='Actual')
        plt.plot(preds_test, label='Predicted')
        plt.legend()
        plt.show()

        # Supongamos que los nuevos datos también están en un CSV
        new_data = pd.read_csv('nuevos_datos.csv')

        # Preprocesar nuevos datos
        X_new = new_data[[colum[0],colum[1],colum[2]]]
        y_new = new_data["Suma Difusa y directa"]  # Esta es tu variable objetivo en los nuevos datos
        X_new_scaled = scaler.transform(X_new)

        # Combinar datos antiguos y nuevos
        X_combined = np.vstack((X_train, X_new_scaled))
        y_combined = np.hstack((y_train, y_new))

        # Retrain el modelo con datos combinados
        model.fit(X_combined, y_combined)

        # Hacer predicciones nuevamente
        preds_combined_test = model.predict(X_test)

        # Evaluar el modelo retrain
        combined_test_loss = mean_squared_error(y_test, preds_combined_test)
        print(f"Combined Test Loss: {combined_test_loss}")

        # Graficar resultados después del retrain
        plt.figure(figsize=(12, 6))
        plt.plot(y_test.values, label='Actual')
        plt.plot(preds_test, label='Original Predicted')
        plt.plot(preds_combined_test, label='Combined Predicted')
        plt.legend()
        plt.show()

    def analisiIrra(self):
        self.analisis(["BuRaGH_Avg","BuRaDH_Avg","BuRaB_Avg"],0)

    def analisiIlum(self):
        self.analisis(["BuLxGH_Avg","BuLxDH_Avg","BuLxB_Avg"],3)
        
    def analsisPar(self):
        self.analisis(["BuPaGH_Avg","BuPaDH_Avg","BuPaB_Avg"],6)
    def analisiUv(self):
        self.analisis(["BuUvGH_Avg","BuUvDH_Avg","BuUvB_Avg"],9)

base=BaseDatosLvl2()
ana=AnalisisIA(base)
ana.analisiIrra()