# SteamDB Sales Scraper

## Descrição
Este projeto é uma aplicação de **Web Scraping** desenvolvida para coletar informações de promoções de jogos no site **SteamDB** e carregar os dados em uma tabela no **Google BigQuery**. Ele automatiza a extração, transformação e carregamento (ETL) de dados relevantes, como nome do jogo, preço com desconto, percentual de desconto e avaliação.

## Funcionalidades
* Extração de dados do SteamDB:
  * ``Nome do jogo``
  * ``Preço com desconto``
  * ``Percentual de desconto``
  * ``Avaliação (%)``
* Carregamento no BigQuery:
  * Inserção dos dados processados em uma tabela configurada no ``Google Cloud Platform``.

## Tecnologias Utilizadas
* Linguagem: ``Python``
* Web Scraping: ``Selenium``
* BigQuery: ``Google Cloud BigQuery API``
* Transformação de Dados: ``Pandas``

## Estrutura do Projeto
```
steamdb_scraper/
├── scraping/
│   ├── steamdb_scraper.py  # Código para scraping dos dados
│   ├── utils.py            # Funções auxiliares para processamento de dados
├── bigquery/
│   ├── bigquery_uploader.py # Código para upload ao BigQuery
│   ├── bigquery_config.py   # Configuração para autenticação no BigQuery
├── config/
│   ├── config.yaml          # Arquivo de configuração (URL e variáveis do projeto)
│   ├── bigquery_credentials.json  # Credenciais para o Google Cloud
├── main.py                  # Script principal para executar o processo completo
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

## Pré-requisitos
1. ``Python 3.9+`` instalado.
2. Credenciais configuradas para acesso ao ``Google Cloud BigQuery``.
3. Navegador ``Google Chrome`` e o ``ChromeDriver`` instalados.

## Configuração
1. Clone o repositório:
   `
   git clone https://github.com/usuario/steamdb-sales-scraper.git
   cd steamdb-sales-scraper
   `

2. Instale as dependências:
   `
   pip install -r requirements.txt
   `

3. Configuração do `config.yaml:`
   No arquivo `config/config.yaml`, configure:
   * `steamdb_url: "https://steamdb.info/sales/"`
   * `bigquery_project_id: "steamdb-442416"`
   * `bigquery_dataset: "steamdb_dataset"`
   * `bigquery_table: "sales"`

4. Configuração do `BigQuery:`
   Suba as credenciais do serviço no arquivo `config/credentials.json`.

## Execução
1. Iniciar o processo de scraping e upload para o BigQuery:
   `
   python main.py
   `

2. Verificar os dados no BigQuery:
   * Acesse o console do BigQuery: [BigQuery Console](https://console.cloud.google.com/bigquery)
   * Navegue até a tabela `sales` para verificar os dados.


## 
Desenvolvido com Python, Selenium e BigQuery para automatizar análises de dados de promoções no Steam.
