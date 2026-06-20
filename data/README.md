OBS: Descrição dos metadados gerada por IA e revisada por humanos 

# Datasets

Os dados utilizados neste projeto são disponibilizados pelo professor em repositórios públicos no GitHub.
Os arquivos não são versionados neste repositório por boas práticas — dados brutos não devem ser armazenados em controle de versão devido ao tamanho e à natureza mutável dos mesmos.

## Origem

| Dataset | Repositório | Caminho dos arquivos |
|---|---|---|
| Pedidos | https://github.com/infobarbosa/datasets-csv-pedidos | `data/pedidos/` |
| Pagamentos | https://github.com/infobarbosa/dataset-json-pagamentos | `data/pagamentos/` |

## Dataset de Pedidos

- **Formato:** CSV
- **Separador:** `;` (ponto-e-vírgula)
- **Compressão:** gzip (`.csv.gz`)
- **Header:** presente na primeira linha
- **Nomenclatura:** `pedidos-YYYY-MM.csv.gz`

### Schema

| Campo | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `ID_PEDIDO` | string (UUID) | Identificador único do pedido | `09faf14c-3def-4551-bb73-cc062421ee81` |
| `PRODUTO` | string | Nome do produto | `MONITOR` |
| `VALOR_UNITARIO` | float | Preço unitário do produto | `600.0` |
| `QUANTIDADE` | long | Quantidade de itens no pedido | `1` |
| `DATA_CRIACAO` | timestamp (ISO 8601) | Data e hora de criação do pedido | `2025-01-03T07:26:01` |
| `UF` | string (2 chars) | Sigla do estado brasileiro | `PE` |
| `ID_CLIENTE` | long | Identificador numérico do cliente | `100` |

### Exemplo de registro

```
ID_PEDIDO;PRODUTO;VALOR_UNITARIO;QUANTIDADE;DATA_CRIACAO;UF;ID_CLIENTE
09faf14c-3def-4551-bb73-cc062421ee81;MONITOR;600.0;1;2025-01-03T07:26:01;PE;100
```

---

## Dataset de Pagamentos

- **Formato:** JSON (newline-delimited, um registro por linha)
- **Compressão:** gzip (`.json.gz`)
- **Nomenclatura:** `pagamentos-YYYY-MM.json.gz`

### Schema

| Campo | Tipo | Descrição | Exemplo |
|---|---|---|---|
| `id_pedido` | string (UUID) | Identificador único do pedido | `09faf14c-3def-4551-bb73-cc062421ee81` |
| `forma_pagamento` | string | Método de pagamento | `CARTAO_CREDITO`, `PIX`, `BOLETO` |
| `valor_pagamento` | float | Valor monetário do pagamento | `600.0` |
| `status` | boolean | Pagamento aprovado (`true`) ou recusado (`false`) | `true` |
| `data_processamento` | timestamp (ISO 8601, microsegundos) | Data e hora do processamento | `2025-01-04T02:46:26.582439` |
| `avaliacao_fraude` | struct | Objeto com a análise de fraude | — |
| `avaliacao_fraude.fraude` | boolean | Classificado como fraude (`true`) ou legítimo (`false`) | `false` |
| `avaliacao_fraude.score` | float (0 a 1) | Score de probabilidade de fraude | `0.82` |

### Exemplo de registro

```json
{
    "id_pedido": "09faf14c-3def-4551-bb73-cc062421ee81",
    "forma_pagamento": "CARTAO_CREDITO",
    "valor_pagamento": 600.0,
    "status": true,
    "data_processamento": "2025-01-04T02:46:26.582439",
    "avaliacao_fraude": {
        "fraude": false,
        "score": 0.82
    }
}
```

---

## Relacionamento entre os datasets

A chave de join entre os dois datasets é o identificador do pedido:

- **Pedidos:** `ID_PEDIDO` (casing UPPER)
- **Pagamentos:** `id_pedido` (casing lower)

Ambos são UUIDs no formato `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

> **Nota:** O valor total do pedido deve ser calculado como `VALOR_UNITARIO * QUANTIDADE` (dataset de pedidos), e não confundido com `valor_pagamento` (dataset de pagamentos), que pode conter descontos ou ajustes.
