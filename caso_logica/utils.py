# ==============================================================================
# Utils
# ==============================================================================
def obter_valor_input(mensagem: str) -> float:
    """
    Função para capturar entrada de texto do usuário, e converter para o tipo
    float. Caso não seja possível converter o valor capturado um erro uma exceção
    é exibida.

    Args:
        mensagem (str): Informativo para captura de texto.

    Raises:
        ValueError: Se tipo recebido não for float.

    Returns:
        float: Valor recebido após conversão para float.
    """
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")