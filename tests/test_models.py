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
from models import *


class TestResource(TestCase):

    def setUp(self):
        self.resource = Resource()

    def test_init(self):
        self.assertEquals(type(self.resource), Resource)

    def tearDown(self):
        pass
