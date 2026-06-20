from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import (
    StructType, StructField, StringType, DoubleType, LongType, TimestampType, BooleanType, FloatType,
)

from config.settings import Settings


class PedidosReader:
    """ 
    Classe de leitura do dataset de Pedidos. 
    Contempla a criação de schemas e método de leitura

    Atende à exigencia nº 1:
    1. **Schemas explícitos**
    TODOS os dataframes devem ter seus schemas explicitamente definidos (sem inferência) 
    """
    SCHEMA = StructType([
        StructField("ID_PEDIDO", StringType(), True),
        StructField("PRODUTO", StringType(), True),
        StructField("VALOR_UNITARIO", DoubleType(), True),
        StructField("QUANTIDADE", LongType(), True),
        StructField("DATA_CRIACAO", TimestampType(), True),
        StructField("UF", StringType(), True),
        StructField("ID_CLIENTE", LongType(), True),
    ])

    def __init__(self, spark: SparkSession, settings: Settings):
        self._spark = spark
        self._settings = settings

    def read(self) -> DataFrame:
        return (
            self._spark.read
            .schema(self.SCHEMA)
            .option("header", self._settings.pedidos_header)
            .option("sep", self._settings.pedidos_separator)
            .csv(self._settings.pedidos_path)
        )


class PagamentosReader:
    """ 
    Classe de leitura do dataset de Pagamentos. 
    Contempla a criação de schemas e método de leitura.
    Por ter um subset de dados, é feito a criação de dois schemas:
    - AVALIACAO_FRAUDE_SCHEMA: Subschema 
    - SCHEMA: Schema principal, contempla AVALIACAO_FRAUDE_SCHEMA como um campo
    
    Atende à exigencia nº 1:
    1. **Schemas explícitos**
    TODOS os dataframes devem ter seus schemas explicitamente definidos (sem inferência) 
    """

    AVALIACAO_FRAUDE_SCHEMA = StructType([
        StructField("fraude", BooleanType(), True),
        StructField("score", FloatType(), True),
    ])

    SCHEMA = StructType([
        StructField("id_pedido", StringType(), True),
        StructField("forma_pagamento", StringType(), True),
        StructField("valor_pagamento", DoubleType(), True),
        StructField("status", BooleanType(), True),
        StructField("data_processamento", TimestampType(), True),
        StructField("avaliacao_fraude", AVALIACAO_FRAUDE_SCHEMA, True),
    ])

    def __init__(self, spark: SparkSession, settings: Settings):
        self._spark = spark
        self._settings = settings

    def read(self) -> DataFrame:
        return (
            self._spark.read
            .schema(self.SCHEMA)
            .json(self._settings.pagamentos_path)
        )
