# import logging
#
# def test_loggingDemo():
#     # create an object for logging
#
#     logger = logging.getLogger(__name__)
#
#     # select where to write
#
#     fileHandler = logging.FileHandler('logfile.log')  # note that here parent 'logging' is used
#     formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")  # setting the format used
#     fileHandler.setFormatter(formatter)  # connecting the format to the filehandler
#
#     logger.addHandler(fileHandler)  # filehandler object. connecting the filehandler to the logger
#
#     logger.setLevel(logging.INFO)  # setting the level. only messages starting from this level are displayed (i.e. if info, then debug level is not displayed)
#
#     # logs with different error levels
#     logger.debug("a debug statement is executed")  # just prints
#     logger.info("information message")  # also prints, but as info
#     logger.warning("something is in warning mode")
#     logger.error("a major error")
#     logger.critical("critical issue")

