#Nombre:BD2_test
#Autor:Álvaro Villar Val
#Fecha:14/03/24
#Versión:0.2.0
#Descripción:Test de la clase BaseDatosLvl2
#########################################################################################################################
#Definimos los imports
import unittest
import unittest
import os
from BaseDatosLvl2 import BaseDatosLvl2  # Reemplaza 'your_module' con el nombre de tu módulo real

class TestBaseDatosLvl2(unittest.TestCase):
    def setUp(self):
        self.db2 = BaseDatosLvl2()
    def tearDown(self):
        self.db2.cur.execute("DROP TABLE IF EXISTS skyscanner")
        self.db2.cur.execute("DROP TABLE IF EXISTS skycamera")
        self.db2.cur.execute("DROP TABLE IF EXISTS radio")
        self.db2.cur.execute("DROP TABLE IF EXISTS imagescam1")
        self.db2.cur.execute("DROP TABLE IF EXISTS skyscannerproc")
        self.db2.cur.execute("DROP TABLE IF EXISTS skycameraproc")
        self.db2.cur.execute("DROP TABLE IF EXISTS radioproc")
        self.db2.conn.commit()
        self.db2.conn.close()
        datos=os.listdir("DatosResulta")
        if len(datos)>0:
            for i in datos:
                os.remove("DatosResulta/"+i)
        img=os.listdir("FotosResulta")
        if len(img)>0:
            for i in img:
                os.remove("FotosResulta/"+i)
        self.db2.stop()
 
    def test_crear(self):
        self.db2.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'skyscanner'")
        self.assertIsNotNone(self.db2.cur.fetchone())
        self.db2.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'skycamera'")
        self.assertIsNotNone(self.db2.cur.fetchone())
        self.db2.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'radio'")
        self.assertIsNotNone(self.db2.cur.fetchone())
        self.db2.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'imagescam1'")
        self.assertIsNotNone(self.db2.cur.fetchone())
        self.db2.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'skyscannerproc'")
        self.assertIsNotNone(self.db2.cur.fetchone())
        self.db2.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'skycameraproc'")
        self.assertIsNotNone(self.db2.cur.fetchone())
        self.db2.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = 'radioproc'")
        self.assertIsNotNone(self.db2.cur.fetchone())

    def test_actualizarImg(self):
        result=self.db2.actualizarImg()
        self.assertTrue(result==0) 


    def test_descImg(self):
        self.db2.actualizarImg()
        self.db2.descImg("23-11-29-10","23-11-29-10")
        img=os.listdir("FotosResulta")
        self.assertTrue(len(img)>0)


    def test_descdat_obtenerdat_Y_descDat(self):
        err1,err2,err3=self.db2.actualizardatos()
        self.assertTrue(err1==0)
        self.assertTrue(err2==0)
        self.assertTrue(err3==0)
        result=self.db2.obtenerdat("*","radioproc","23-10-01","23-10-01")
        self.assertFalse(result.empty)
        self.db2.descdat("*","radioproc","23-10-01","23-10-01")
        datos=os.listdir("DatosResulta")
        self.assertTrue(len(datos)>0)

        
    
    
if __name__ == '__main__':
    unittest.main()
