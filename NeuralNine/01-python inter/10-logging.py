import logging
# DEBUG
# INFO
# WARNING
# ERROR 
# CRITICAL
# logging.basicConfig(level=logging.DEBUG)        # let you see the debug and higger levels
# logging.basicConfig(level=logging.CRITICAL)        # let you see the critical and higger levels (none is higger)
# logging.basicConfig(level=logging.INFO)        # let you see the info and higger levels
# logging.info("You have 20 mails in your email")
# logging.critical("A component failed!")
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("my Logger")
# logger.info("Best logger created")
# logger.critical("You will die")
# logger.log(logging.ERROR, "an error occured")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formater = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formater)

logger.addHandler(handler)
logger.debug("This is an debug message")
logger.info("This is an info message")
logger.critical("You will die")
logger.log(logging.ERROR, "an error occured")