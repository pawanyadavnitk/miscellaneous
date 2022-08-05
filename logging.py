import os
import logging
from logging import handlers
from logging.config import dictConfig
import pathlib

logs_directory = os.getcwd() + "/logs"

pathlib.Path(logs_directory).mkdir(parents = True, exist_ok = True)


def setup_logging(name):
    logging_config = dict(
        version = 1,
        disable_existing_loggers = True,
        formatters = {
            'f': {
                'format': '%(asctime)s %(levelname)-8s %(message)s',
                'datefmt': "%Y/%m/%d %H:%M:%S %Z%z"
            },
            'simple': {
                'format': "%(asctime)s %(process)d %(filename)s %(lineno)s %(levelname)s %(message)s",
                'datefmt': "%Y/%m/%d %H:%M:%S %Z%z"
            },
            "extra": {
                "format": "%(asctime)s %(process)d %(thread)d %(filename)s %(lineno)s %(funcName)s %(levelname)s %(message)s",
                'datefmt': "%Y/%m/%d %H:%M:%S %Z%z"
            }
        },
        handlers = {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            },
            'info_file_handler': {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": 'INFO',
                "formatter": "extra",
                "filename": f"{logs_directory}/ae_extractor_info_{name}.log",
                "when": "midnight",
                "interval": 1,
                "backupCount": 31,
                "encoding": "utf8"
            },
            'error_file_handler': {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": 'ERROR',
                "formatter": "extra",
                "filename": logs_directory + "/ae_extractor_errors.log",
                "when": "midnight",
                "interval": 1,
                "backupCount": 31,
                "encoding": "utf8"
            }
        },
        loggers = {
            "my_module": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": "no"
            }
        },
        root = {
            "level": "INFO",
            "handlers": ["console", "info_file_handler", "error_file_handler"]
        }
    )

    dictConfig(logging_config)

    log = logging.getLogger()
    log.setLevel(logging.INFO)
    return log


def root_configurer(queue):
    h = handlers.QueueHandler(queue)
    root = logging.getLogger()
    root.addHandler(h)
    root.setLevel(logging.DEBUG)


def listener_configurer():
    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler(logs_directory + "/ae_extractor_info.log", 'a', 300, 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)


def worker_configurer(queue):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    root = logging.getLogger()
    root.addHandler(h)
    # send all messages, for demo; no other level or filter logic applied.
    root.setLevel(logging.INFO)
