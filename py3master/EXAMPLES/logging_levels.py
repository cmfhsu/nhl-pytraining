#!/usr/bin/env python
import logging

logging.basicConfig(
    filename='../TEMP/levels.log',
    level=logging.WARN,
)

logging.warning('This message will be logged')
logging.debug('This message will NOT be logged')
logging.error('This message will be logged')