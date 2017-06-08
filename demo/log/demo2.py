# coding:utf-8
import logging

log_file = "./nomal_logger.log"
log_level = logging.DEBUG

logger = logging.getLogger("loggingmodule.NomalLogger")
handler = logging.FileHandler(log_file)
formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(log_level)

# test
logger.debug("this is a debug msg!")
logger.info("this is a info msg!")
logger.warn("this is a warn msg!")
logger.error("this is a error msg!")
logger.critical("this is a critical msg!")