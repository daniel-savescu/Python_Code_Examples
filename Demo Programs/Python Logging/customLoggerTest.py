import logging
from custom_logger import get_custom_logger

def f1():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical("Critical message from f1()")
    logger.error("Error message from f1()")
    logger.warning("Warning message from f1()")
    logger.info("Info message from f1()")
    logger.debug("Debug message from f1()")

def f2():
    logger = get_custom_logger(logging.WARNING)
    logger.critical("Critical message from f2()")
    logger.error("Error message from f2()")
    logger.warning("Warning message from f2()")
    logger.info("Info message from f2()")
    logger.debug("Debug message from f2()")

f1()
f2()