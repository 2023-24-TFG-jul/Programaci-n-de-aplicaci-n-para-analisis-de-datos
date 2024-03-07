#Nombre:BD1_test
#Autor:Álvaro Villar Val
#Fecha:07/03/24
#Versión:0.2.0
#Descripción: Test para de la creación de la base de datos
#########################################################################################################################
#Definimos los imports
import unittest #Importamos la librería unittest
from BaseDatosLvl1 import BaseDatosLvl1 #Importamos la clase BaseDatosLvl1


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
    
    def test_actualizardatos(self):
        # Comprobamos que en una base de datos nueva no hay errores al actualizar los datos
        # La función devuelve el nº de errores que se han producido al actualizar los datos
        #Por lo cual en una nueva base de datos el resultado debería ser 0
        _,_,_,err1,err2,err3 = self.db.actualizardatos()
        self.assertTrue(err1==0)
        self.assertTrue(err2==0)
        self.assertTrue(err3==0)
    
    def test_obtenerdat(self):
        _,_,_,err1,err2,err3 = self.db.actualizardatos()
        result=self.db.obtenerdat("*","radio","23-10-01","23-10-01")
        self.assertFalse(result.empty)

if __name__ == '__main__':
    unittest.main()