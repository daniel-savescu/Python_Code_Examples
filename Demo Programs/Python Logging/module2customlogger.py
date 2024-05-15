import logging

logger = logging.getLogger("module_2_logger")
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("module_2.log", mode='w')
logger.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.critical("Critical message from module 2")
logger.error("Error message from module 2")
logger.warning("Warning message from module 2")
logger.info("Info message from module 2")
logger.debug("Debug message from module 2")