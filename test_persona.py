import unittest
from persona import Persona
from unittest.mock import patch


class TestPersona(unittest.TestCase):

    @patch('builtins.input', side_effect=[1, 'Fernandez', 'Alberto'])
    def test_persona(self, mock_input):
        persona = Persona()
        persona.input()
        self.assertEqual(persona.__repr__(), "Persona: 1 - Fernandez, Alberto")


if __name__ == "__main__":
    unittest.main()
