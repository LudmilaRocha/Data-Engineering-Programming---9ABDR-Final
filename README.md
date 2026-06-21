# TRABALHO FINAL - DATA ENGINEERING PROGRAMMING

Trabalho final da disciplina de Data Engineering Programming para o curso de pós graduação MBA em Engenharia de Dados na FIAP. Professor Marcelo Barbosa Pinto.

Membros do grupo:

- Guilherme Csorgo Henriques: 370073
- Karen Luzia Vitório Martins: 370096
- Ludmila Rocha Silva: 372484
- Thiago Guilherme: 375344

## TODOs: 
- Dizer que o enunciado do trabalho está no arquivo `ESCOPO.md`
- Adicionar disclaimer que não estamos versionando os dados pq não faz o menor sentido (Porque é uma péssima prática e pq é muito pesado pra manter isso no repo)
- Dizer que não estamos usando pip e sim pipenv (e os porquês: Mais fácil gerenciar pacote, resolve conflitos sozinho, guarda hashes dos pacotes em um arquivo `.lock`, além de separar o que é dependencia dev e o que é prod)
- Revisar e atualizar o "Estrutura do Projeto" e o "Descrição dos pacotes" ao final do trabalho
- Apontar no projeto o que foi feito por IA e o que foi feito por humanos. Também adicionar essa informação aqui
- Não vamos usar múltiplas branches com feature, bugfix, etc.. vamos fazer tudo na main para facilitar

## Estrutura do Projeto
Buscamos criar uma estrutura que consolide os aprendizados vistos em aula com as boas práticas de mercado. Levamos em consideração tanto a separação de escopos como a modularização dos escopos. 

```
9ABDR-DEP-TRABALHO-FINAL/
├── src/                           # Pacote principal da aplicação
│   ├── main.py                    # Ponto de entrada (aggregation root)
│   ├── config/
│   │   └── settings.py            # Classe de configuração do projeto (caminhos, parâmetros, etc)
│   ├── spark/
│   │   └── session.py             # Classe de gerenciamento da SparkSession
│   ├── io/
│   │   ├── reader.py              # Classes de leitura de dados (CSV e JSON a priori)
│   │   └── writer.py              # Classe de escrita de dados (Parquet)
│   ├── business/
│   │   └── logic.py               # Classe de lógica de negócio (filtros, joins, transformações, etc)
│   └── pipeline/
│       └── orchestrator.py        # Classe de orquestração do pipeline
├── tests/
│   └── test_logic.py              # Centralização dos testes
├── data/
│   ├── pagamentos/                # Dataset de pagamentos (JSON) - não versionado
│   └── pedidos/                   # Dataset de pedidos (CSV) - não versionado
├── output/                        # Resultado do pipeline em formato Parquet - não versionado
├── Pipfile                        # Dependências gerenciadas pelo pipenv
├── Pipfile.lock                   # Lock das versões exatas das dependências
├── pyproject.toml                 # Configuração de build e metadados do projeto
├── requirements.txt               # Dependências (fallback para pip install -r)
├── MANIFEST.in                    # Arquivos incluídos no pacote distribuível
└── .gitignore                     # Regras de versionamento
```

### Descrição dos pacotes

| Pacote | Responsabilidade |
|---|---|
| `src/config` | Centraliza todas as configurações do projeto (caminhos de entrada/saída, nome da aplicação, parâmetros de execução). |
| `src/spark` | Gerencia a criação e o ciclo de vida da SparkSession. |
| `src/data_io` | Leitura dos datasets de origem (pedidos em CSV, pagamentos em JSON) e escrita do relatório final em Parquet. Todos os schemas são definidos explicitamente. |
| `src/business` | Contém as regras de negócio: filtros, joins e transformações. Inclui logging das etapas e tratamento de erros com try/except. |
| `src/pipeline` | Orquestra a execução do pipeline de ponta a ponta (leitura → transformação → escrita). |
| `tests` | Testes unitários da lógica de negócio utilizando pytest. |

### Dados

Os datasets não são versionados no repositório. Para executar o projeto, clone os datasets do professor nas pastas correspondentes:

- **Pagamentos (JSON):** copie os arquivos de `dataset-json-pagamentos/data/pagamentos/` para `data/pagamentos/`
- **Pedidos (CSV):** copie os arquivos de `datasets-csv-pedidos/data/pedidos/` para `data/pedidos/`

## Como executar

### Pré-requisitos

- Python 3.11+
- Java 8 ou 11 (necessário para o PySpark)
- pipenv (`pip install pipenv`)

### Instalação das dependências

```bash
pipenv install
```

Para instalar também as dependências de desenvolvimento (pytest):

```bash
pipenv install --dev
```

### Executando o pipeline

```bash
pipenv run python src/main.py
```

O resultado será gravado em formato Parquet na pasta `output/`.

### Executando os testes

```bash
pipenv run pytest
```
