import HtmlTestRunner
import unittest

from tests.search import TestSearchBar



class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_de_rulat = unittest.TestSuite()
        test_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSearchBar)
        ])
        # daca avem mai multe clase de test, rezultatele vor fi puse in acelasi raport de executie
        runner = HtmlTestRunner.HTMLTestRunner(

            report_title='TestReport',
            combine_reports=True,
            report_name='Smoke Test Result'
        )

        runner.run(test_de_rulat)