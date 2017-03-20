#!/usr/bin/env python
import nose
import logging

formatter = '%(asctime)s %(levelname)8s [%(filename)18s:%(lineno)04d]:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatter)

def setup_module():
    logging.info('setup_module()')
 
def teardown_module():
    logging.info('teardown_module()')

class TestCase(object):
    """ 3.0
    http://wiki.megvii-inc.com/pages/viewpage.action?pageId=7772647
    """
    @classmethod
    def setup_class(cls):
        logging.info('TestClass.setup_class()')

    @classmethod
    def teardown_class(cls):
        logging.info('TestClass.teardown_class()')

    def setup(self):
        logging.info('TestClass.setup()')

    def teardown(self):
        logging.info('TestClass.teardown()')


