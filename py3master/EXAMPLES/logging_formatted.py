#!/usr/bin/env python
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    filename='../TEMP/formatted.log',
    level=logging.INFO,
)

logging.info("this is information")
logging.warn("this is a warning")
logging.info("this is information")
logging.fatal("this is fatal")
