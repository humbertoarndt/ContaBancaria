# ==============================================================================
# Classe ContaBancaria
# ==============================================================================
class ContaBancaria:
    """
    Classe que representa uma conta bancária simples.

    A classe 'ContaBancaria' permite realizar operações básicas como depósito,
    saque e transferência entre contas. Cada conta possui um saldo inicial que
    pode ser definido no momento de criação da conta.

    Attributes:
        saldo (float): O saldo inicial da conta bancária.

    Methods:
        depositar(self, valor: float) -> None:
            Deposita um valor na conta.

        sacar(self, valor: float) -> None:
            Saca um valor da conta, se houver saldo suficiente.

        transferir(self, destinatario: 'ContaBancaria', valor: float) -> None:
            Transfere um valor para outra conta, se houver saldo suficiente.
    """


    def __init__(self, saldo_inicial=0.00):
        """
        Inicializa a ContaBancaria com um saldo inicial.

        Args:
            saldo_inicial (float, optional): O saldo inicial da conta. Por padrão 0.
        """
        self.saldo = saldo_inicial


    def depositar(self, valor: float) -> None:
        """
        Função para depositar um valor em uma ContaBancaria.

        Args:
            valor (float): O valor a ser depositado.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Valor inválido para depósito. Depósito não realizado.")


    def sacar(self, valor: float) -> None:
        """
        Função para sacar um valor de uma ContaBancaria.

        A função verifica se existe saldo disponível para ser sacado. Se houver,
        o valor é removido do saldo atual.

        Args:
            valor (float): O valor a ser sacado.
        """
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
            else:
                print("Saldo insuficiente. Operação não realizada.")
        else:
            print("Valor inválido para saque. Saque não realizado.")


    def transferir(self, destinatario: 'ContaBancaria', valor: float) -> None:
        """
        Função para tranferir um valor de uma ContaBancaria para outra.

        A função verifica se o valor a ser tranferido é válido e se há saldo
        suficiente na conta de origem para realizar a operação. Se tudo estiver
        correto, o valor é debitado da conta origem e creditado na conta destino.

        Args:
            destinatario (ContaBancaria): A conta que receberá o valor tranferido.
            valor (float): O valor a ser tranferido.
        """
        if valor > 0: 
            if valor <= self.saldo:
               self.saldo -= valor
               destinatario.depositar(valor)
               print(f"Transferência de R${valor} realizada. Novo saldo: R${self.saldo}")
            else:
                print("Saldo insuficente. Transferência não realizada.")
        else:
            print("Valor inválido para transferência. Transferência não realizada.")