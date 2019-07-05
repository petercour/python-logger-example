import logging


logging.basicConfig(level=logging.INFO, 
                    filename='my_app.log', # log to this file
                    format='%(asctime)s [INFO] %(message)s') # include timestamp

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#fh = logging.FileHandler('my_app.log')
#fh.setLevel(logging.INFO)
#logger.addHandler(fh)

def main():
    logger.info("Program started")
    print("Hello World")
    logger.info("Hello World printed")
    logger.info("Program finished")

main()
