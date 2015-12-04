'''
Created on 3 Dec 2015

@author: alex
'''
import os
import unittest
import vcf

from phe.variant_filters.DepthFilter import DepthFilter


class TestDepthFilter(unittest.TestCase):


    def setUp(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        self.vcf_in = os.path.join(base_path, "sample.vcf")
        self.filter_threshold = 5
        self.filter = DepthFilter({DepthFilter.parameter: self.filter_threshold})

        self.bad_positions = [31809, 31810]
        self.bad_positions.sort()

    def tearDown(self):
        pass

    def test_call(self):

        reader = vcf.Reader(filename=self.vcf_in)

        bad_positions = []
        for record in reader:
            result = self.filter(record)

            if result is None:
                continue

            bad_positions.append(record.POS)

        bad_positions.sort()

        self.assertListEqual(self.bad_positions, bad_positions)

    def test_short_desc(self):
        short_desc = "Filter sites by depth. (DP > %s)" % self.filter_threshold

        self.assertEquals(short_desc, self.filter.short_desc())

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()