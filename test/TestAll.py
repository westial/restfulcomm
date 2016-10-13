"""
Run all test
"""
import sys
import unittest

sys.path.append('..')
from test.testrabbitmq import TestRabbitMq
from test.testwerkzeug import TestWerkzeug

testrabbitmq = unittest.makeSuite(TestRabbitMq, 'test')
testwerkzeug = unittest.makeSuite(TestWerkzeug, 'test')

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(testrabbitmq)
    unittest.TextTestRunner(verbosity=2).run(testwerkzeug)
