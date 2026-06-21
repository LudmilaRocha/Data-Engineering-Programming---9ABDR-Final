from pyspark.sql import DataFrame

from config.settings import Settings


class ParquetWriter:
    """ Classe responsável pela leitura de arquivos parquet """ 

    def __init__(self, settings: Settings):
        self._settings = settings

    def write(self, df: DataFrame) -> None:
        (
            df.write
            .mode("overwrite")
            .parquet(self._settings.output_path)
        )
