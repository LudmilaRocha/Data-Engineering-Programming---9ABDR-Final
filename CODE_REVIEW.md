# CODE REVIEW - Validações

**Responsável:** Ludmila Rocha  
**Data:** 28/06/2026  

---

## 1. Clonagem
* **Status:** OK, sem impedimentos.

> [!NOTE]
> O processo de clonagem do repositório foi executado com sucesso e todos os arquivos foram baixados corretamente.

<img width="886" height="541" alt="image" src="https://github.com/user-attachments/assets/ff155f14-c25b-4d7a-a786-8d44fbb2bf3d" />


---

## 2. Execução do Script Bash (`run_program.sh`)

### Conteúdo - README
Observei no [README.md](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/README.md) que ele orienta a executar como `bash run_program.py`, mas o correto deveria ser `run_program.sh`. 

<img width="886" height="523" alt="image" src="https://github.com/user-attachments/assets/4ef6bcff-840c-4b70-b6a5-04128ec9871e" />

---

### Cenários de Teste e Execução

#### Cenário 1 - Execução no VS Code
```powershell
PS C:\Users\Usuario\Documents\MBA Engenharia de Dados\Projetos\Data Engineering Programming\Data-Engineering-Programming Final\Data-Engineering-Programming---9ABDR-Final> bash run_program.sh
: invalid optionline 2: set: -
set: usage: set [-abefhkmnptuvxBCEHPT] [-o option-name] [--] [-] [arg ...]
run_program.sh: line 3: $'\r': command not found
run_program.sh: line 7: $'\r': command not found
```
<img width="886" height="210" alt="image" src="https://github.com/user-attachments/assets/50cfb04f-36fe-410d-aee2-5d6cd3675ff9" />



#### Cenário 2 - Execução no PowerShell
Abri o meu diretório com o comando `cd` e executei o comando `bash run_program.sh`, retornando os mesmos erros:
```powershell
PS C:\Users\Usuario\Documents\MBA Engenharia de Dados\Projetos\Data Engineering Programming\Data-Engineering-Programming Final\Data-Engineering-Programming---9ABDR-Final> bash run_program.sh
: invalid optionline 2: set: -
set: usage: set [-abefhkmnptuvxBCEHPT] [-o option-name] [--] [-] [arg ...]
run_program.sh: line 3: $'\r': command not found
run_program.sh: line 7: $'\r': command not found
```

<img width="886" height="763" alt="image" src="https://github.com/user-attachments/assets/3e74bb97-e23a-4dfc-9c56-fabd4c4f7b00" />


#### Cenário 3 - Dois cliques no arquivo
Ele solicita para escolher um aplicativo para execução.

<img width="886" height="791" alt="image" src="https://github.com/user-attachments/assets/1ccb2f38-73a7-40e1-a91e-1563257cb0a1" />


---

### Diagnóstico, Impacto e Resolução

* **Impacto:** O erro ocorre devido à diferença de comportamento de quebras de linha entre ambientes Linux e Windows.
  * No **Windows**, a quebra de linha utiliza retorno de carro e alimentação de linha (`\r\n` / CRLF).
  * No **Linux/Terminal**, espera-se apenas a alimentação de linha (`\n` / LF).

* **Sugestão:** Criação do arquivo `.gitattributes` com a regra `*.sh text eol=lf`. Com isso, o Git consegue ajustar automaticamente a quebra de linha nos dois ambientes (Linux/Windows) quando o professor clonar o repositório.

* **Resolução na minha máquina local:** No VS Code, cliquei em **CRLF** no canto inferior direito, mudei para **LF** e salvei o arquivo (`Ctrl + S`).
  <img width="886" height="628" alt="image" src="https://github.com/user-attachments/assets/5e2e6853-0cde-4986-8fa2-c30325c05f1e" />


* **Novo erro encontrado:** O script subentende que a pessoa tem Python instalado na máquina e configurado corretamente no path, o que pode não ocorrer em todas as máquinas.
  ```text
  === Configurando ambiente Python ===
  Instalando pipenv...
  run_program.sh: line 42: pip: command not found
  ```
  <img width="886" height="135" alt="image" src="https://github.com/user-attachments/assets/9d356c81-c29f-495f-b4e9-538ffb226a7e" />

  Para corrigir localmente, precisei instalar na minha máquina:
  ```powershell
  winget install Python.Python.3.11
  python -m pip install pipenv
  ```
  <img width="886" height="194" alt="image" src="https://github.com/user-attachments/assets/fcbcbe7a-faae-4140-820d-a503c9ad4cb5" />
  <img width="886" height="323" alt="image" src="https://github.com/user-attachments/assets/4d2e103a-22d3-4333-94dc-8f8550e4681e" />


  Executei novamente `bash run_program.sh`, mas apresentou o mesmo erro:
  ```text
  Pagamentos: 25 arquivos

  === Configurando ambiente Python ===
  Instalando pipenv...
  run_program.sh: line 42: pip: command not found 
  ```
  <img width="767" height="313" alt="image" src="https://github.com/user-attachments/assets/228cf188-11ae-411c-860d-be66134d7d4b" />


* **Dica de Resolução no Script:** Em vez de usar `pipenv install --dev`, utilizar `python -m pipenv install --dev`, pois isso evita a necessidade de configurar manualmente o path do Windows.
* *Nota:* Finalizei as validações do script neste ponto e não executei mais testes do script bash diretamente.


---

## 3. Docker e Docker Compose

### Docker Compose
* **Comando:** `docker compose up --build`
* **Resultado:** Demorou bastante tempo para compilar/executar. No entanto, não conseguiu baixar os arquivos do Excel e retornou uma tabela de resultados vazia.
```text
dep-trabalho-final  | 26/06/28 19:36:46 INFO TaskSchedulerImpl: Killing all running tasks in stage 5: Stage finished
dep-trabalho-final  | 26/06/28 19:36:46 INFO DAGScheduler: Job 5 finished: showString at NativeMethodAccessorImpl.java:0, took 52.438479 ms
dep-trabalho-final  | 
dep-trabalho-final  | +---------+--+---------------+-----------+-----------+
dep-trabalho-final  | |id_pedido|UF|forma_pagamento|valor_total|data_pedido|
dep-trabalho-final  | +---------+--+---------------+-----------+-----------+
dep-trabalho-final  | +---------+--+---------------+-----------+-----------+
dep-trabalho-final  | 
dep-trabalho-final  | 28-06-2026T17:36:46 : INFO : module orchestrator : function run : line 46 :
dep-trabalho-final  | Log : Pipeline finalizado com sucesso
```

<img width="886" height="331" alt="image" src="https://github.com/user-attachments/assets/06aadf44-1397-4a16-9ceb-7001ec345623" />


### Sem Docker Compose (Execução Manual do Docker)
* **Comandos:**
  ```bash
  docker build -t dep-trabalho-final .
  docker run -v ./output:/app/output -v ./logs:/app/logs dep-trabalho-final
  ```
* **Resultado:** Também não conseguiu baixar o Excel.
```text
26/06/28 20:19:06 INFO TaskSchedulerImpl: Canceling stage 5
26/06/28 20:19:06 INFO TaskSchedulerImpl: Killing all running tasks in stage 5: Stage finished
26/06/28 20:19:06 INFO DAGScheduler: Job 5 finished: showString at NativeMethodAccessorImpl.java:0, took 69.286387 ms
+---------+---+---------------+-----------+-----------+
|id_pedido|UF |forma_pagamento|valor_total|data_pedido|
+---------+---+---------------+-----------+-----------+
+---------+---+---------------+-----------+-----------+
```

<img width="886" height="326" alt="image" src="https://github.com/user-attachments/assets/b8331668-2eb8-4d52-a8fb-32498ad422ad" />


---

## Validação do Código (Com arquivos locais baixados e LF configurado)

Para realizar a validação correta do código, precisei baixar os arquivos CSV manualmente, utilizando o `bash run_program.sh` após realizar a configuração de quebra de linha para LF.

### Logs do Terminal (Download de Arquivos)
```text
remote: Counting objects: 100% (30/30), done.
remote: Compressing objects: 100% (29/29), done.
remote: Total 30 (delta 0), reused 29 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (30/30), 2.26 MiB | 9.71 MiB/s, done.
[4/4] Copiando arquivos de pagamentos para data/pagamentos/...
=== Limpando arquivos temporários ===
Pedidos:    25 arquivos
Pagamentos: 25 arquivos

=== Configurando ambiente Python ===
Instalando pipenv...
run_program.sh: line 42: pip: command not found
```
<img width="886" height="223" alt="image" src="https://github.com/user-attachments/assets/0fa9ca28-b28a-404b-8f4e-b3c4e5dc6d14" />



### Execução no Docker (Após obtenção dos dados)
```bash
docker build -t dep-trabalho-final .
docker run -v ./output:/app/output -v ./logs:/app/logs dep-trabalho-final
```

#### Resultado
```text
26/06/28 20:33:15 INFO CodeGenerator: Code generated in 7.319433 ms
+------------------------------------+---+---------------+-----------+-------------------+
|id_pedido                           |UF |forma_pagamento|valor_total|data_pedido        |
+------------------------------------+---+---------------+-----------+-------------------+
|acbf9b42-eaca-4cd9-914a-109de59aa943|AL |BOLETO         |2500.0     |2025-02-02 17:02:14|
|df280f1a-b8f4-4a29-be64-66fb7fab2a25|AL |BOLETO         |1100.0     |2025-06-12 12:29:22|
|394c5640-fae2-413f-bdfb-52f316fa6782|AL |CARTAO_CREDITO |5000.0     |2025-01-03 18:49:13|
|4440113d-717d-4887-8889-574853e47e20|AL |CARTAO_CREDITO |1100.0     |2025-03-06 06:33:11|
|cdbf1791-ad2f-4357-af93-1af7e9545214|AL |CARTAO_CREDITO |600.0      |2025-03-15 13:24:44|
|a66abc7f-d362-4942-8be9-e6f7b696b14e|AL |CARTAO_CREDITO |300.0      |2025-03-27 20:28:37|
|9b459f36-d5b9-4b1a-91d9-0be858e369dc|AL |CARTAO_CREDITO |30.0       |2025-04-18 16:21:57|
|f70efb0f-6457-4356-aa20-a72c7fb0b45f|AL |CARTAO_CREDITO |1500.0     |2025-04-27 11:16:35|
|7e8d385e-c6a1-449b-943c-0a7d43c1683a|AL |CARTAO_CREDITO |1500.0     |2025-05-09 16:29:05|
|b8dc3820-2cc6-4426-9b95-d127228482cf|AL |CARTAO_CREDITO |3000.0     |2025-05-11 18:13:18|
|14ecf8c2-9b0b-49b4-a44b-b94b551e75bd|AL |CARTAO_CREDITO |1100.0     |2025-05-18 12:13:55|
|346b4309-9521-487a-934e-4a772f4b2b29|AL |CARTAO_CREDITO |600.0      |2025-05-20 23:45:06|
|93c92691-1cca-4004-94d7-bfaffb79856b|AL |CARTAO_CREDITO |1100.0     |2025-05-26 12:49:28|
|f365080a-c5d5-49aa-b26d-d33738955836|AL |CARTAO_CREDITO |900.0      |2025-07-02 16:13:48|
|8d0016e6-5e86-4833-93f8-e8c22cf797fb|AL |CARTAO_CREDITO |600.0      |2025-07-08 06:39:34|
|c7c65286-16ce-4386-8fb0-704c917f2636|AL |CARTAO_CREDITO |1500.0     |2025-07-23 18:38:16|
|2d0792c2-5140-4915-bf1d-a927e1733cba|AL |CARTAO_CREDITO |500.0      |2025-08-26 08:06:39|
|44642917-5605-441a-a8b7-d68e1a2e39af|AL |CARTAO_CREDITO |500.0      |2025-08-26 22:13:12|
|b65004e8-93fd-45bf-971f-1cad6d1913e7|AL |CARTAO_CREDITO |3000.0     |2025-08-28 21:59:29|
|a6081e4a-3506-4635-a250-aef9ded4366a|AL |CARTAO_CREDITO |2500.0     |2025-09-16 11:48:16|
+------------------------------------+---+---------------+-----------+-------------------+
only showing top 20 rows
28-06-2026T08:33:15 : INFO : module orchestrator : function run : line 46 : 
Log : Pipeline finalizado com sucesso
26/06/28 20:33:15 INFO SparkContext: SparkContext is stopping with exitCode 0 from stop at NativeMethodAccessorImpl.java:0.
26/06/28 20:33:15 INFO SparkUI: Stopped Spark web UI at http://da5f8152ffa0:4040
26/06/28 20:33:15 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
26/06/28 20:33:15 INFO MemoryStore: MemoryStore cleared
26/06/28 20:33:15 INFO BlockManager: BlockManager stopped
26/06/28 20:33:15 INFO BlockManagerMaster: BlockManagerMaster stopped
26/06/28 20:33:15 INFO OutputCommitCoordinator$OutputCommitCoordinatorEndpoint: OutputCommitCoordinator stopped!
26/06/28 20:33:15 INFO SparkContext: Successfully stopped SparkContext (Uptime: 8898 ms)
28-06-2026T08:33:16 : INFO : module main : function main : line 42 : 
Log : Aplicação encerrada
```
<img width="886" height="455" alt="image" src="https://github.com/user-attachments/assets/26709a88-e507-43eb-a25a-2ed3322ca712" />


---

## Validação de Regras de Negócio

### Atributos do Relatório Final (Status: OK)
* Identificador do pedido (`id_pedido`)
* Estado onde o pedido foi feito (`UF`)
* Forma de pagamento
* Valor total do pedido
* Data do pedido

### Regras Aplicadas e Validadas

| Regra de Negócio | Arquivo de Validação | Status | Observação |
| :--- | :--- | :---: | :--- |
| Compreender apenas pedidos do ano de **2025** | [settings.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/config/settings.py) | **OK** | Ano filtrado corretamente conforme parametrização. |
| Ordenação por estado (`UF`), forma de pagamento e data de criação do pedido | [logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/business/logic.py) | **OK** | Implementação de ordenação múltipla conforme esperado. |
| Gravação do relatório em formato **Parquet** | [settings.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/config/settings.py) | **OK** | Tipo de arquivo e caminho parametrizados para Parquet. |
| Filtragem de pagamentos recusados (`status = false`) | [logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/business/logic.py) | **OK** | Exclusão de pagamentos recusados validada na lógica. |

* Arquivos responsáveis validados e em conformidade:
  * [writer.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/data_io/writer.py) (Escrita de dados): **OK**
  * [logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/business/logic.py) (Regras de negócio): **OK**



---

## Critérios Específicos de Avaliação

Abaixo está o detalhamento de cada item exigido no escopo do trabalho e o resultado da avaliação:

### 1. Schemas Explícitos
* **Requisito:** Todos os DataFrames devem ter schemas definidos explicitamente (sem inferência).
* **Avaliação:** **OK**
* **Detalhes:** Validada a definição explícita de schemas para os datasets de pedidos e pagamentos no arquivo [reader.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/data_io/reader.py).

### 2. Orientação a Objetos
* **Requisito:** Todos os componentes do projeto devem ser encapsulados em classes.
* **Avaliação:** **OK**
* **Detalhes:** Todas as classes do projeto foram validadas e se encontram devidamente encapsuladas.

### 3. Injeção de Dependências
* **Requisito:** Utilizar `main.py` como Aggregation Root, instanciar e injetar todas as dependências no fluxo principal.
* **Avaliação:** **OK**
* **Detalhes:** Classes avaliadas e injetadas corretamente no [main.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/main.py):
  * Configuração;
  * Gerenciamento de sessão Spark;
  * Leitura e Escrita de Dados;
  * Lógica de Negócios;
  * Orquestração do Pipeline.

### 4. Configurações Centralizadas
* **Requisito:** Definir pacote de configurações, possuir pelo menos uma classe de configuração e utilizá-la no fluxo principal.
* **Avaliação:** **OK**
* **Sugestão de Melhoria:** Acho interessante documentar melhor no [README.md](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/README.md) o funcionamento da linha abaixo (usada para localizar as pastas de arquivo de forma dinâmica):
  ```python
  base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  ```
  No material de referência do professor, os caminhos foram definidos de forma estática no YAML:
  ```yaml
  paths:
    clientes: "./data-engineering-pyspark/data/input/dataset-json-clientes/data/clientes.json.gz"
    pedidos: "./data-engineering-pyspark/data/input/datasets-csv-pedidos/data/pedidos/"
  ```

### 5. Sessão Spark
* **Requisito:** Pacote de gerenciamento da sessão Spark, criação de classe de gerenciamento e utilização na main.
* **Avaliação:** **OK**
* **Detalhes:** Validado o arquivo [session.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/spark/session.py) e a classe `SparkSessionManager` sendo devidamente instanciada e utilizada no [main.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/main.py).

### 6. Leitura e Escrita de Dados (I/O)
* **Requisito:** Definir pacote de leitura/escrita, criar classes associadas e usá-las na main.
* **Avaliação:** **OK**
* **Detalhes:** Pasta `data_io` estruturada com os arquivos [reader.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/data_io/reader.py) e [writer.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/data_io/writer.py) contendo a definição explícita de schema dos DataFrames.

### 7. Lógica de Negócio
* **Requisito:** Pacote e classe de lógica de negócio sendo consumidos na main.
* **Avaliação:** **OK**
* **Detalhes:** Validados no arquivo [logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/business/logic.py) e consumidos na [main.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/main.py).

### 8. Orquestração do Pipeline
* **Requisito:** Pacote e classe de orquestração do pipeline consumidos na main.
* **Avaliação:** **OK**
* **Detalhes:** Validada a classe `PipelineOrchestrator` em [orchestrator.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/pipeline/orchestrator.py) e sua chamada no fluxo da [main.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/main.py).

### 9. Logging
* **Requisito:** Importação do pacote `logging` na classe de lógica, configuração centralizada do logging e uso para registro de etapas.
* **Avaliação:** **OK** (Com observações de design)
* **Detalhes:** 
  * Importado corretamente usando `import logging`.
  * Logging implementado e ativo nos arquivos:
    * [main.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/main.py) (Configuração do logger raiz);
    * [orchestrator.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/pipeline/orchestrator.py) (Registro das etapas do pipeline);
    * [logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/business/logic.py) (Registro de filtros e processamentos);
    * [writer.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/data_io/writer.py) (Registro de escrita do Parquet).
  * *Observação de Design:* Conforme o material do professor (exemplo do [Passo 8 - Logging](https://github.com/infobarbosa/pyspark-poo#passo-8-logging)), a recomendação indicava criar o arquivo `src/config/logging.py`. O projeto atual está centralizando as configurações de logs corretas de forma um pouco diferente, mas funcional.

### 10. Tratamento de Erros
* **Requisito:** Estrutura `try/except` na classe de lógica e uso de logging para registro do erro capturado.
* **Avaliação:** **OK**
* **Detalhes:** Implementado no arquivo [logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/business/logic.py) (linhas 36 a 48), integrando o logger do arquivo [logging.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/config/logging.py).

Trecho do código validado:
```python
def execute(self, df_pedidos: DataFrame, df_pagamentos: DataFrame) -> DataFrame:
    try:
        self.logger.info("Iniciando execução da lógica de negócio")
        df_pagamentos_filtrado = self._filtrar_pagamentos(df_pagamentos)
        df_pedidos_filtrado = self._filtrar_pedidos_por_ano(df_pedidos)
        df_joined = self._join_pedidos_pagamentos(df_pedidos_filtrado, df_pagamentos_filtrado)
        df_selecionado = self._selecionar_colunas(df_joined)
        df_ordenado = self._ordenar(df_selecionado)
        self.logger.info("Lógica de negócio finalizada com sucesso")
        return df_ordenado
    except Exception as e:
        self.logger.error("Erro durante a execução da lógica de negócio: %s", e)
        raise
```

```

```

### 11. Empacotamento da Aplicação
* **Requisito:** Existência dos arquivos estruturais e de distribuição.
* **Avaliação:** **OK**
* **Detalhes:**
  * [pyproject.toml](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/pyproject.toml): Validado. Possui a configuração adicional do pytest `[tool.pytest.ini_options]`, que está configurada de forma abrangente comparada ao template mais genérico sugerido pelo professor.
  * [requirements.txt](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/requirements.txt): Validado.
  * [README.md](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/README.md): Validado. Observação: Considero importante detalhar melhor como executar os testes e o fluxo do programa.
  * [MANIFEST.in](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/MANIFEST.in): Validado.

### 12. Testes Unitários
* **Requisito:** Pelo menos um teste unitário para a lógica de negócio executado com sucesso utilizando o `pytest`.
* **Avaliação:** **PENDENTE**
* **Detalhes:**
  * Referências comparadas com o repositório de testes do professor (Passo 13).
  * O teste unitário deve validar as regras contidas em [logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/src/business/logic.py), porém a estrutura de código correspondente em [test_logic.py](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/tests/test_logic.py) ainda está pendente ou ausente.
  * O pacote `pytest>=8.0.0` está devidamente listado no arquivo [requirements.txt](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/requirements.txt) e a configuração correspondente está inserida no final do arquivo [pyproject.toml](file:///c:/Users/Usuario/Documents/MBA%20Engenharia%20de%20Dados/Projetos/Data%20Engineering%20Programming/Data-Engineering-Programming%20Final/Data-Engineering-Programming---9ABDR-Final/pyproject.toml):
    ```toml
    [tool.pytest.ini_options]
    pythonpath = ["src"]
    testpaths = ["tests"]
    markers = [
        "unit: Testes unitários isolados (sem I/O externo)",
        "integration: Testes de integração (orquestração entre componentes)",
    ]
    addopts = "-v"
    ```
    <img width="886" height="331" alt="image" src="https://github.com/user-attachments/assets/d12a81f9-064b-4f06-b501-dab31f7ed37b" />


#### Sugestão de Cenário de Teste (Dataset Pagamentos)
Acho interessante testar os comportamentos de fraude e legitimidade dos pagamentos recusados:
1. **Recusado e Legítimo (Deve PASSAR):**
   `("pedido-A", "PIX", 100.0, False, "2025-01-01T10:00:00", (False, 0.1))`
2. **Recusado e Fraude (Deve ser DESCARTADO):**
   `("pedido-C", "CARTAO_CREDITO", 300.0, False, "2025-01-01T10:00:00", (True, 0.95))`

