'''
'''
import logging

logging.basicConfig(
    filename='testLog.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

logging.info('App Started')
logging.error('Whatever message to be sent to the file')

try:
    res = 1 / 0
except Exception as e:
    logging.exception('Exception Occured')
