from pyspark.sql import SparkSession

from config.settings import Settings


class SparkSessionManager:
    """ Classe responsável por fornecer (e manter) a sessão spark. """

    def __init__(self, settings: Settings):
        self._settings = settings
        self._spark = None

    def get_session(self) -> SparkSession:
        if self._spark is None:
            self._spark = (
                SparkSession.builder
                .appName(self._settings.app_name)
                .master("local[*]")
                .getOrCreate()
            )
        return self._spark

    def stop(self):
        if self._spark is not None:
            self._spark.stop()
            self._spark = None
