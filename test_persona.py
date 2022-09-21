import unittest
from persona import Person
from unittest.mock import patch


class TestPersona(unittest.TestCase):

    @patch('builtins.input', side_effect=[1, 'Fernandez', 'Alberto'])
    def test_persona(self, mock_input):
        persona = Person()
        self.assertEqual(persona.get_data(), {
            "dni": 1,
            "apellido": "Fernandez",
            "nombre": "Alberto"
        })

    @patch('builtins.input', side_effects=[3, 'Trump', 'Donald'])
    def test_input(self, input):
        persona = Person()
        persona.__init__()
        self.assertEqual(input, {
            'documento': 3,
            'apellido': 'Trump',
            'nombre': 'Donald'
        })


if __name__ == "__main__":
    unittest.main()