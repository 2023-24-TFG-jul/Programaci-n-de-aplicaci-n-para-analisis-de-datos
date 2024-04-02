#Nombre:BD2_test
#Autor:Álvaro Villar Val
#Fecha:14/03/24
#Versión:0.0.1
#Descripción:Test de la clase BaseDatosLvl2
#########################################################################################################################
#Definimos los imports
import unittest
from unittest.mock import MagicMock
from BaseDatosLvl1 import BaseDatosLvl1
from BaseDatosLvl2 import BaseDatosLvl2

class TestBaseDatosLvl2(unittest.TestCase):

    def setUp(self):
        self.db1_mock = MagicMock(spec=BaseDatosLvl1)
        self.original_db1 = BaseDatosLvl2.db1
        BaseDatosLvl2.db1 = self.db1_mock
        self.db2 = BaseDatosLvl2()

    def tearDown(self):
        BaseDatosLvl2.db1 = self.original_db1

    def test_init(self):
        self.assertEqual(self.db2.dirradio, "Datos\\datalogger")
        self.assertEqual(self.db2.dircamera, "Datos\\sky-camera")
        self.assertEqual(self.db2.dirscanner, "Datos\\Sky-scanner 2023_12")
        self.assertEqual(self.db2.dirimgCam1, "Datos\\Fotos\\CAM1\\imagenes")
        self.assertEqual(self.db2.dirimgCam2, "Datos\\Fotos\\CAM2\\imagenes")
        self.assertEqual(self.db2.datahost, "localhost")
        self.db1_mock.assert_called_once()

if __name__ == '__main__':
    unittest.main()