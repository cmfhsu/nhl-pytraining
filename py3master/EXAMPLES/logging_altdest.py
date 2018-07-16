#!/usr/bin/env python
import sys
import logging
import logging.handlers

logger = logging.getLogger('ThisApplication')
logger.setLevel(logging.DEBUG)  # minimum level

if sys.platform == 'win32':
    eventlog_handler = logging.handlers.NTEventLogHandler()
    logger.addhandler(eventlog_handler)
else:
    syslog_handler = logging.handlers.SysLogHandler()
    logger.addHandler(syslog_handler)

# note -- use your own SMTP server...
email_handler = logging.handlers.SMTPHandler(
    ('smtpcorp.com',8025),
    'LOGGER@pythonclass.com',
    ['jstrick@mindspring.com'],
    'ThisApplication Log Entry',
    ('jstrickpython', 'python(monty)'),
)

logger.addHandler(email_handler)

logger.debug('this is debug')
logger.critical('this is critical')
logger.warn('this is a warning')
