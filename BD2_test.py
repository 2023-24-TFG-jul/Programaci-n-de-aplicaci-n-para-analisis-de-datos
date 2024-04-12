#Nombre:BD2_test
#Autor:Álvaro Villar Val
#Fecha:14/03/24
#Versión:0.1.0
#Descripción:Test de la clase BaseDatosLvl2
#########################################################################################################################
#Definimos los imports
import unittest
import unittest
from unittest.mock import patch, MagicMock
from BaseDatosLvl2 import BaseDatosLvl2  # Reemplaza 'your_module' con el nombre de tu módulo real

class TestBaseDatosLvl2(unittest.TestCase):
    def setUp(self):
        self.bd2 = BaseDatosLvl2()

    def test_init(self):
        self.assertIsInstance(self.bd2, BaseDatosLvl2)
        # Verifica que el motor SQL se inicializa correctamente
        self.assertIsNotNone(self.bd2.engine)

    @patch('your_module.BaseDatosLvl1')
    def test_crear(self):
        self.bd2.cur = MagicMock()
        self.bd2.conn = MagicMock()
        
        self.bd2.crear()
        self.bd2.cur.execute.assert_called()
        self.bd2.conn.commit.assert_called()

    def test_actualizarImg(self):
        with patch.object(self.bd2.db1, 'actuimgCam1', return_value=10) as mocked_actuimgCam1:
            result = self.bd2.actualizarImg()
            mocked_actuimgCam1.assert_called_once()
            self.assertEqual(result, 10)

    def test_descImg(self):
        self.bd2.db1 = MagicMock()
        self.bd2.descImg('2022-01-01', '2022-01-02')
        self.bd2.db1.obtenerImg.assert_called_once_with('2022-01-01', '2022-01-02')

    def test_descdat(self):
        self.bd2.db1 = MagicMock()
        self.bd2.descdat('select *', 'radioproc', 'date=20220101', 'date=20220102')
        self.bd2.db1.descDat.assert_called_once_with('select *', 'radioproc', 'date=20220101', 'date=20220102')

    def test_actualizardatos(self):
        mock_data = MagicMock()
        self.bd2.db1 = MagicMock()
        self.bd2.db1.actualizardatos.return_value = (mock_data, mock_data, mock_data, 1, 1, 1)

        self.bd2.actualizarRadio = MagicMock()
        self.bd2.actualizarCammera = MagicMock()
        self.bd2.actualizarScanner = MagicMock()

        self.bd2.actualizardatos()
        self.bd2.actualizarRadio.assert_called_with(mock_data)
        self.bd2.actualizarCammera.assert_called_with(mock_data)
        self.bd2.actualizarScanner.assert_called_with(mock_data)

    def test_procdatos(self):
        self.bd2.calc = MagicMock()
        self.bd2.calc.comprobarghi.return_value = 'result'
        self.bd2.calc.comprobardhi.return_value = 'result'
        # Añade todos los mocks necesarios para otros métodos del objeto calculadora

        result = self.bd2.procdatos('2022-01-01', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        self.assertTrue('result' in result)

    def test_obtenerdat(self):
        self.bd2.db1 = MagicMock()
        self.bd2.obtenerdat('select *', 'radioproc', 'date=20220101', 'date=20220102')
        self.bd2.db1.obtenerdat.assert_called_once_with('select *', 'radioproc', 'date=20220101', 'date=20220102')

    def test_stop(self):
        self.bd2.cur = MagicMock()
        self.bd2.conn = MagicMock()
        self.bd2.db1 = MagicMock()
        
        self.bd2.stop()
        
        self.bd2.cur.close.assert_called()
        self.bd2.conn.close.assert_called()
        self.bd2.db1.stop.assert_called()

if __name__ == '__main__':
    unittest.main()
