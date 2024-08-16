# ==============================================================================
# Imports
# ==============================================================================
import unittest
from unittest.mock import patch
from utils import obter_valor_input

# ==============================================================================
# Classe TestUtils
# ==============================================================================
class TestUtils(unittest.TestCase):
    """
    Testes unitários para as funções utilitárias.

    Contém testes para a função obter_valor_input, que captura a entrada do
    usuário e a converte para um número float.
    """


    @patch('builtins.input', return_value='50')
    def test_obter_valor_input_valido(self, mock_input):
        """
        Testa função obter_valor_input com uma entrada válida.

        Este teste verifica se a função converte corretamente a entrada do
        usuário para um valor float quando a entrada é válida.
        """
        valor = obter_valor_input("Informe o valor: R$")
        self.assertEqual(valor, 50.0)


    @patch('builtins.input', side_effect=['abc', '100'])
    def test_obter_valor_input_invalid(self, mock_input):
        """
        Testa a função obter_valor_input com uma entrada inválida seguida de uma
        válida.

        Este teste verifica se a função lida corretamente com uma entrada inválida
        (Não numérica) e continua pedindo até receber uma entrada válida, que é
        então convertida para float.
        """
        valor = obter_valor_input("Informe o valor: R$")
        self.assertEqual(valor, 100.0)


if __name__ == "__name__":
    unittest.main()
