# ==============================================================================
# Classe ContaBancaria
# ==============================================================================
class ContaBancaria:
    """Classe que representa uma conta bancaria simples.

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
        """Inicializa a ContaBancaria com um saldo inicial.

        Args:
            saldo_inicial (int, optional): O saldo inicial da conta. Por padrão 0.
        """
        self.saldo = saldo_inicial


    def depositar(self, valor: float) -> None:
        """Função para depositar um valor em uma ContaBancaria.

        Args:
            valor (float): O valor a ser depositado.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Valor inválido para depósito. Depósito não realizado.")


    def sacar(self, valor: float) -> None:
        """Função para sacar um valor de uma ContaBancaria.

        A função verifica se existe saldo disponível para ser sacado. Se houver
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
        """Função para tranferir um valor de uma ContaBancaria para outra.

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


# ==============================================================================
# Utils
# ==============================================================================
def obter_valor_input(mensagem: str) -> float:
    """Função para capturar entrada de texto do usuário, e converter para o tipo
    float. Caso não seja possível converter o valor capturado um erro uma exceção
    é exibida.

    Args:
        mensagem (str): Informativo para captura de texto.

    Returns:
        float: Valor recebido após conversão para float.
    """
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")


# ==============================================================================
# Main
# ==============================================================================
def main():
    conta1_saldo_inicial = obter_valor_input("Informe o saldo inicial da conta 1: R$")
    conta2_saldo_inicial = obter_valor_input("Informe o saldo inicial da conta 2: R$")

    conta1 = ContaBancaria(conta1_saldo_inicial)
    conta2 = ContaBancaria(conta2_saldo_inicial)

    while True:
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            valor_deposito = obter_valor_input("Informe o valor a ser depositado na Conta 1: R$")
            conta1.depositar(valor_deposito)
        elif escolha == "2": 
            valor_saque = obter_valor_input("Informe o valor a ser sacado na Conta 1: R$")
            conta1.sacar(valor_saque)
        elif escolha == "3":
            valor_transfencia = obter_valor_input("Informe o valor a ser transferido da Conta 1 para a Conta 2: R$")
            conta1.transferir(conta2, valor_transfencia)
        elif escolha == "4":
            break

    print("\nSaldos Finais:")
    print(f"Conta 1: R$ {conta1.saldo}")
    print(f"Conta 2: R$ {conta2.saldo}")


if __name__ == "__main__":
    main()