#Nombre:BD1_test
#Autor:Álvaro Villar Val
#Fecha:07/03/24
#Versión:0.3.0
#Descripción: Test para de la creación de la base de datos
#########################################################################################################################
#Definimos los imports
import unittest #Importamos la librería unittest
from BaseDatosLvl1 import BaseDatosLvl1 #Importamos la clase BaseDatosLvl1
import os #Importamos la librería os

class TestBaseDatosLvl1(unittest.TestCase):

    def setUp(self):
        self.db = BaseDatosLvl1()
        self.db.crear()

    def tearDown(self):
        # Limpiamos la base de datos
        self.db.cur.execute("DROP TABLE IF EXISTS skyscanner")
        self.db.cur.execute("DROP TABLE IF EXISTS skycamera")
        self.db.cur.execute("DROP TABLE IF EXISTS radio")
        self.db.cur.execute("DROP TABLE IF EXISTS imagescam1")
        self.db.conn.commit()
        self.db.conn.close()
        datos=os.listdir("DatosResulta")
        if len(datos)>0:
            for i in datos:
                os.remove("DatosResulta/"+i)
        img=os.listdir("FotosResulta")
        if len(img)>0:
            for i in img:
                os.remove("FotosResulta/"+i)
        self.db.stop()

    def test_table_skyscanner_exists(self):
        # Comprobamos que se crea la tabla skyscanner
        self.db.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'skyscanner'")
        self.assertIsNotNone(self.db.cur.fetchone())

    def test_table_skycamera_exists(self):
        # Comprobamos que se crea la tabla skycamera
        self.db.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'skycamera'")
        self.assertIsNotNone(self.db.cur.fetchone())

    def test_table_radio_exists(self):
        # Comprobamos que se crea la tabla radio
        self.db.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'radio'")
        self.assertIsNotNone(self.db.cur.fetchone())

    def test_actuimgCam1(self):
        # Comprobamos que en una base de datos nueva no hay errores al actualizar las imagenes de la cámara 1
        # La función devuelve el nº de errores que se han producido al actualizar laa imagenes de la cámara 1
        #Por lo cual en una nueva base de datos el resultado debería ser 0
        result = self.db.actuimgCam1()
        self.assertTrue(result==0)  # Ponemos que sea 0 el resultado´

    def test_actualizardatos_obtenerda_y_descDat(self):
        # Comprobamos que en una base de datos nueva no hay errores al actualizar los datos
        # La función devuelve el nº de errores que se han producido al actualizar los datos
        #Por lo cual en una nueva base de datos el resultado debería ser 0
        _,_,_,err1,err2,err3 = self.db.actualizardatos()
        self.assertTrue(err1==0)
        self.assertTrue(err2==0)
        self.assertTrue(err3==0)
        result=self.db.obtenerdat("*","radio","23-10-01","23-10-01")
        self.assertFalse(result.empty)
        self.db.descDat("*","radio","23-10-01","23-10-01")
        datos=os.listdir("DatosResulta")
        self.assertTrue(len(datos)>0)

    def test_descImg(self):
        # Comprobamos que en una base de datos nueva no hay errores al descargar las imagenes
        # La función devuelve el nº de errores que se han producido al descargar las imagenes
        #Por lo cual en una nueva base de datos el resultado debería ser 0
        self.db.actuimgCam1()
        self.db.obtenerImg("23-11-29-10","23-11-29-10")
        img=os.listdir("FotosResulta")
        self.assertTrue(len(img)>0)


if __name__ == '__main__':
    unittest.main()