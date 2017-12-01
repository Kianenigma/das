import logging
import os

class ACTIONS:
    MOVE = 'move'
    HEAL = 'heal'
    ATTACK = 'attack'

class DIRECTIONS:
    H = 'h'
    V = 'v'

class TRANSPORT:
    host = 'localhost'
    port = 8081

class USERS:
    PLAYER = 'p'
    DRAGON = 'd'


logger = logging.getLogger()

def init_logger(file):

    #If log directory doesn't exist creates it

    dirname = os.path.dirname(file)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # clear contents from previous run
    open(file, 'w').close()

    fileHandler = logging.FileHandler(file)
    formatter = logging.Formatter(
        '%(asctime)s %(name)-2s %(levelname)-8s %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

    logger.debug("Logger initialized")
