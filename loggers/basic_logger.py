import logging
import sys
from logging.config import dictConfig

from omegaconf import OmegaConf

config = OmegaConf.load("config.yaml")
# loggers are created using the getLogger function
logger = logging.getLogger(__name__)

# logging_config = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "simple": {
#             "format": "%(levelname)s: %(message)s",
#         }
#     },
#     "handlers": {
#         "stdout": {
#             "class": "logging.StreamHandler",
#             "formatter": "simple",
#             "stream": sys.stdout,  # Directly referencing sys.stdout
#         }
#     },
#     "loggers": {
#         "root": {
#             "level": "DEBUG",
#             "handlers": ["stdout"],
#         }
#     },
# }


def setup_logging(config_filepath=None):
    logging_config = OmegaConf.load(config_filepath)
    logging_config = OmegaConf.to_object(logging_config)
    dictConfig(logging_config)
    logger.info("Running base logger")
    pass
