
log_config = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s : %(levelname)s : module %(module)s : function %(funcName)s : line %(lineno)s : \nLog : %(message)s",
            "datefmt": "%d-%m-%YT%I:%M:%S"
        }
    },
    "handlers": {
        "file": {
            "formatter": "default",
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "logs/9ABDR-DEP-TRABALHO-FINAL.log",
            "mode": "a"
        },
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "": {
            "handlers": [ "file", "console" ],
            "level": "DEBUG",
            "propagete": False,
        }
    }
}