# Solução

## Leitura do Código
Durante a primeira leitura do código notei vários erros que impediriam sua execução,
ou um resultado diferente do esperado. Listei abaixo alguns dos erros solucionados:
* Espaçamento e identação incorretos;
* Função de depósito que subtrai valores ao invés de incrementá-los;
* Condições com a síntaxe incorreta;
* Função declarada indevidamente;
* Strings com aspas `"` não fechadas;
* Variáveis usadas sem declaração, ou com nome incorreto;
* Laço de repetição baseado em entrada do usuário com divergência entre suas opções
e condicionais executadas;
* Chamada de função inexistente;

## Entendimento do Código
Para entendimento do código o meu processo sempre envolve sua documentação, usei
**Docstrings** para descrever o comportamento das funções, assim como seus parâmetros
e retornos. Também estruturei o seguindo o conhecimento que possuo da **PEP 8**.

## Separar Código
Decidi tornar o código mais **modular** ao separá-lo em arquivos diferentes, cada 
um responsável por uma única funcionalidade. Isso ajuda em sua **manutenção**, pois 
alterações em uma parte do código são menos propensas a causar problemas em outras
partes. Arquivos menores também possuem uma **legibilidade** maior e são mais fáceis
de entender, por fim é mais fácil adicionar novas funcionalidades. O que torna sua 
**escabilidade** mais fácil.

## Testes Unitários
Para garantir que as partes do código funcionam como esperado implementei testes
unitários que me ajudam a identificar e corrigir possíveis erros. É algo que também
aumenta a confiança na entrega que estou fazendo. Os testes unitários podem ser executados com o seguinte comando:
```sh
py -m unittest discover -s tests
```

## Padrões de Design
Consigo entender o valor de se aplicar padrões de design para ajudar na manutenção
e expansão de projetos. No caso da classe ContaBancaria encontrei as oportunidades
abaixo:

### Strategy Pattern
Com este padrão é possível adicionar novas operações bancárias como `investir`, através
de um método abstrato.
```python
from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def executar(self, conta: 'ContaBancaria', valor: float) -> None:
        pass


class Deposito(Operacao):
    def executar(self, conta: 'ContaBancaria', valor: float) -> None:
        conta.saldo += valor


class Saque(Operacao):
    def executar(self, conta: 'ContaBancaria', valor: float) -> None:
        if conta.saldo >= valor:
            conta.saldo -= valor


class ContaBancaria:
    def __init__(self, saldo_inicial=0.00):
        self.saldo = saldo_inicial


    def realizar_operacao(self, operacao: Operacao, valor: float) -> None:
        operacao.executar(self, valor)

```

### Factory Pattern
Com este padrão é possível encapsular a lógia para criação de `ContaBancaria` para criar
diferentes tipos de conta, `poupança`, `corrente` e `investimento`, por exemplo.
```python
class ContaBancariaFactory:
    @staticmethod
    def criar_conta(tipo: str, saldo_inicial: float) -> ContaBancaria:
        if tipo == 'poupanca':
            return ContaPoupanca(saldo_inicial)
        elif tipo == 'corrente':
            return ContaCorrente(saldo_inicial)
        elif tipo == 'investimento':
            return ContaInvestimento(saldo_inicial)
        else:
            raise ValueError("Atenção, tipo de conta desconhecido.")
```

## Uso
Clone o repositório.
```sh
git clone https://github.com/humbertoarndt/Processo-Seletivo-Investment-Services.git <dir>
```

Acesse o diretório criado na pasta `caso_logica`.
```sh
cd <dir>/caso_logica
```

Execute o programa com a seguinte instrução.
```sh
py main.py
```

O programa pode ser encerrado ao entrar a opção `4` em seu terminal, ou com `Ctrl + C` para
interromper sua execução pelo envio de um sinal `SIGINT`.