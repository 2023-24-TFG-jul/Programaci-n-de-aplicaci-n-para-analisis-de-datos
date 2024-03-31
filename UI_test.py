#Nombre:UI_test
#Autor:Álvaro Villar Val
#Fecha:14/03/24
#Versión:0.0.1
#Descripción: test de la clase UI
#########################################################################################################################
#Definimos los imports
import unittest
import UI

class TestUI(unittest.TestCase):

    def test_function1(self):
        # Replace 'function1' with the name of a function in the UI module
        result = UI.function1()
        expected_result = # Add the expected result here
        self.assertEqual(result, expected_result)

    def test_function2(self):
        # Replace 'function2' with the name of another function in the UI module
        result = UI.function2()
        expected_result = # Add the expected result here
        self.assertEqual(result, expected_result)

    # Add more test methods here to test other functions or classes in the UI module

if __name__ == '__main__':
    unittest.main()