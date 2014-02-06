#-------------------------------------------------------------------------------
# Name:        test_models
# Purpose:     Provides Unit tests for Python BIBFRAME models using
#              <http://bibframe.org:8282/vocab.rdf>
#
# Author:      Jeremy Nelson
#
# Created:     2014-02-06
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     MIT
#-------------------------------------------------------------------------------
import unittest
from models import *


class TestResource(unittest.TestCase):

    def setUp(self):
        self.resource = Resource()

    def test_init(self):
        self.assertEquals(type(self.resource), Resource)

    def tearDown(self):
        pass

class TestAuthority(unittest.TestCase):

    def setUp(self):
        self.new_base_authority = Authority()

    def test_init(self):
        self.assert_(isinstance(self.new_base_authority, Authority))


    def test_hasAnnotation(self):
        pass


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
