import logging
import module2customlogger
logger = logging.getLogger('module_1_logger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('module_1.log', mode='a')

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S %p')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.critical("This is a critical message")
logger.error("This is a error message")
logger.warning("This is a warning message")
logger.info("This is a info message")
logger.debug("This is a debug message")