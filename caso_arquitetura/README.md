# Solução

## Modelar Processo
Para projetar a arquitetura de um sistema de **tranferência PIX**, meu primeiro 
passo foi construir um modelo do processo que imaginei usando notação **BPMN**.
![Modelo de processo do PIX](https://github.com/humbertoarndt/Processo-Seletivo-Investment-Services/blob/main/caso_arquitetura/img/20240816_BPMN.drawio.png)

## Componentes da Arquitetura
Tendo em mente um desenho do que queria atingir passei a pensar em quais componentes
utilizaria. São eles:

* **Rede de Distribuição de Conteúdo:** Interface para entrega de sites multiplataforma
estáticos ou dinâmicos;
* **API Gateway:** Gerencia as requisições externas e roteia para os serviços internos;
* **Load Balancer:** Distribui o tráfego entre servidores;
* **Ambiente de Produção:** Escalável, consistente e de alta disponibilidade;
* **Serviço de Transferência:** Recebe as ordens de transferência e coordena o débito e crédito entre contas;
* **Serviço de Contas:** Gerencia as contas dos usuários, incluindo saldo e histórico de transações;
* **Serviço de Histórico:** Armazena o histórico de todas as transações por 5 anos;
* **Sistema de Mensageria:** Envio e consumo de mensagens de forma assíncrona;
* **Banco de Dados:** Armazena dados das contas e transações;
* **Sistema de Armazenamento:** Local para armezar dados históricos por 5 anos;
* **Sistema de Logs e Métricas:** Coleta e armazena logs e métricas para monitoramento e análise;

## Microserviços
* POST transfer-service-app /transfer
    * Envia para fila
    * Armazena no banco de dados
* GET account-service-app /account/{clientId}
    * Faz leitura na base de dados informações do cliente (Conta, saldo, extrato)
* GET / POST account-service-app /acount/{clientId}/saldo
    * Faz leitura na base de dados informações do cliente (Conta, saldo, extrato)
    * Faz escrita na base de dados de saldo
* GET account-service-app /account/{clientId}/history
    * Consulta dados no banco de dados e retorna o histórico de transações

## Tecnologias Sugeridas
* **Rede de Distribuição de Conteúdo:** AWS Cloudfront
* **API Gateway:** AWS API Gateway
* **Load Balancer:** AWS Elastic Load Balancer
* **Ambiente de Produção:** Cluster Kubernetes
* **Sistema de Mensageria:** Apache Kafka, AWS SQS ou RabbitMQ
* **Banco de Dados:** AWS RDS
* **Sistema de Armazenamento:** AWS S3
* **Sistema de Logs e Métricas:** AWS CloudWatch e Prometheus/Grafana

## Fluxo de Trabalho
* Recebimento da Ordem de Transferência:
    - O cliente envia uma ordem de transferência para o API Gateway.
    - O API Gateway roteia a requisição para o Serviço de Transferência.
* Processamento da Transferência:
    - O Serviço de Transferência valida a ordem e solicita o débito na conta do remetente ao Serviço de Contas.
    - O Serviço de Contas verifica o saldo e, se suficiente, debita o valor e retorna a confirmação.
    - O Serviço de Transferência então solicita o crédito na conta do destinatário ao Serviço de Contas.
    - O Serviço de Contas credita o valor na conta do destinatário e retorna a confirmação.
* Armazenamento do Histórico:
    - O Serviço de Transferência envia uma mensagem para o Serviço de Histórico com os detalhes da transação.
    - O Serviço de Histórico armazena a transação no banco de dados e em um armazaenamento de longo prazo
* Logs e Métricas:
    - Todos os serviços enviam logs e métricas para o sistema de monitoramento

## Diagrama de Arquitetura
![Diagrama PIX AWS](https://github.com/humbertoarndt/Processo-Seletivo-Investment-Services/blob/main/caso_arquitetura/img/20240816_PIX.drawio.png)

## Vamos de Turma
Para chegar na solução apresentada contei com a ajuda de colegas incríveis, sem eles esta entrega não seria possível. Obrigado!