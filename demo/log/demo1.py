# coding:utf-8
import logging


log_file = "./basic_logger.log"

logging.basicConfig(filename=log_file, level=logging.DEBUG)

logging.debug("this is a debugmsg!")
logging.info("this is a infomsg!")
logging.warn("this is a warn msg!")
logging.error("this is a error msg!")
logging.critical("this is a critical msg!")