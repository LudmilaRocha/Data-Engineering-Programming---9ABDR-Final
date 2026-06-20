import logging
import logging.config

from config.logging import log_config

logging.config.dictConfig(log_config)

def main():
    logging.info("Aplicação executando. Aperte Ctrl + C para encerrar.")

if __name__ == "__main__":
    main()
