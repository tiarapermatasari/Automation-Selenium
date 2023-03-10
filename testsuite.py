import unittest
from unittest.suite import TestSuite
import register, login, cart

if __name__ == '__main__':
    # create test suite from classes
    suite = TestSuite()
    # panggil test
    tests = unittest.TestLoader()
    # menambahkan test ke suite
    suite.addTests(tests.loadTestsFromModule(register))
    suite.addTests(tests.loadTestsFromModule(login))
    suite.addTests(tests.loadTestsFromModule(cart))

    #run test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
