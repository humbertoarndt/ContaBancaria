# ==============================================================================
# Imports
# ==============================================================================
import unittest
from contaBancaria import ContaBancaria

# ==============================================================================
# Classe TestContaBancaria
# ==============================================================================
class TestContaBancaria(unittest.TestCase):
    """
    Teste unitários para a classe ContaBancaria.

    O testes garatem que as operações de depósio, saque e transferência funcionem
    conforme o esperado em diferentes cenários.
    """


    def test_depositar(self):
        """
        Testa o método depositar da classe ContaBancaria.

        O método depositar deve adicionar corretamente um valor positivo ao saldo
        da ContaBancaria.

        Este teste verifica:
        1. Se o saldo é atualizado corretamente após um depósito válido.
        2. Se valores negativos não afetam o saldo.
        """
        conta = ContaBancaria(100)

        # Testar caminho válido
        conta.depositar(50)
        self.assertEqual(conta.saldo, 150)

        # Testar valor inválido, não alterar saldo
        conta.depositar(-20)
        self.assertEqual(conta.saldo, 150)


    def test_sacar(self):
        """
        Testa o método sacar da classe ContaBancaria.

        O método sacar deve subtrair corretamente um valor do saldo da ContaBancaria,
        desde que haja saldo suficiente.

        Este teste verifica:
        1. Se o saldo é atualizado corretamente após um saque válido.
        2. Se saques superiores ao saldo disponível não são permitidos.
        3. Se valores negativos não afetam o saldo.
        """
        conta = ContaBancaria(100)

        # Testar caminho válido
        conta.sacar(50)
        self.assertEqual(conta.saldo, 50)

        # Testar saldo insuficente, não alterar saldo
        conta.sacar(100)
        self.assertEqual(conta.saldo, 50)

        # Testar valor inválido, não alterar saldo
        conta.sacar(-20)
        self.assertEqual(conta.saldo, 50)


    def test_transferir(self):
        """
        Testa o método transferir da classe ContaBancaria.

        O método tranferir deve debitar um valor do saldo da conta origem e creditar
        esse valor na conta destinatária, desde que a conta origem tenha saldo suficiente.

        Este teste verifica:
        1. Se a transferência válida atualiza corretamente os saldos de ambas as contas.
        2. Se a transferência com saldo insuficiente na conta origem não são permitidas.
        3. Se valores negativos não afetam os saldos.
        """
        conta1 = ContaBancaria(100)
        conta2 = ContaBancaria(50)

        # Testar caminho válido
        conta1.transferir(conta2, 30)
        self.assertEqual(conta1.saldo, 70)
        self.assertEqual(conta2.saldo, 80)

        # Testar saldo insuficiente, não alterar saldo
        conta2.transferir(conta2, 100)
        self.assertEqual(conta1.saldo, 70)
        self.assertEqual(conta2.saldo, 80)

        # Testar valor inválido, não alterar saldo
        conta1.transferir(conta1, -20)
        self.assertEqual(conta1.saldo, 70)
        self.assertEqual(conta2.saldo, 80)


if __name__ == "__main__":
    unittest.main()