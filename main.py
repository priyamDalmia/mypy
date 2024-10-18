from omegaconf import OmegaConf
import sys

from loggers.basic_logger import setup_logging
import logging

config = OmegaConf.load("config.yaml")
logger = logging.getLogger(__name__)
setup_logging(config_filepath=config.logging.config_filepath)

logger.info("Running main logger!")
