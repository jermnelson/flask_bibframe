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
import json
import unittest
from models import *

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent(label="Agent")

    def test_init(self):
        self.assert_(isinstance(self.agent, Agent))

    def test_rdf_properties(self):
        self.assert_(hasattr(self.agent, 'authorityAssigner'))
        self.assert_(hasattr(self.agent, 'authoritySource'))
        self.assert_(hasattr(self.agent, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.agent, 'hasAuthority'))
        self.assert_(hasattr(self.agent, 'identifier'))
        self.assert_(hasattr(self.agent, 'label'))
        self.assert_(hasattr(self.agent, 'relatedTo'))

    def test_to_dict(self):
        self.assertItemsEqual(self.agent.as_dict(),
                          {u'hasAuthority': None,
                           u'authorityAssigner': None,
                           'identifiers': {},
                           'label': 'Agent',
                           u'relatedTo': None,
                           u'authoritySource': None,
                           u'identifier': None,
                           u'authorizedAccessPoint': None})
        self.assertItemsEqual(self.agent.as_dict(show_null=False),
                          {'identifiers': {},
                           'label': 'Agent'})

    def test_to_json(self):
        self.assertEquals(json.loads(self.agent.as_json()),
                          json.loads("""{
                            "authorityAssigner": null,
                            "authoritySource": null,
                            "authorizedAccessPoint": null,
                            "hasAuthority": null,
                            "identifier": null,
                            "identifiers": {},
                            "label": "Agent",
                            "relatedTo": null}"""))


    def tearDown(self):
        pass


class TestAnnotation(unittest.TestCase):

    def setUp(self):
        self.annotation = Annotation()

    def test_init(self):
        self.assert_(isinstance(self.annotation, Annotation))

    def test_rdf_properties(self):
        self.assert_(hasattr(self.annotation, 'annotates'))
        self.assert_(hasattr(self.annotation, 'annotationAssertedBy'))
        self.assert_(hasattr(self.annotation, 'annotationBody'))
        self.assert_(hasattr(self.annotation, 'annotationSource'))
        self.assert_(hasattr(self.annotation, 'assertionDate'))
        self.assert_(hasattr(self.annotation, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.annotation, 'identifier'))
        self.assert_(hasattr(self.annotation, 'label'))
        self.assert_(hasattr(self.annotation, 'relatedTo'))

    def tearDown(self):
        pass

class TestArchival(unittest.TestCase):

    def setUp(self):
        self.archival = Archival()

    def test_init(self):
        self.assert_(isinstance(self.archival, Archival))

    def test_rdf_properties(self):
        self.assert_(hasattr(self.archival, 'abbreviatedTitle'))
        self.assert_(hasattr(self.archival, 'ansi'))
        self.assert_(hasattr(self.archival, 'arrangement'))
        self.assert_(hasattr(self.archival, 'aspectRatio'))
        self.assert_(hasattr(self.archival, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.archival, 'awardNote'))
        self.assert_(hasattr(self.archival, 'carrierCategory'))
        self.assert_(hasattr(self.archival, 'coden'))
        self.assert_(hasattr(self.archival, 'colorContent'))
        self.assert_(hasattr(self.archival, 'contentAccessibility'))
        self.assert_(hasattr(self.archival, 'contentsNote'))
        self.assert_(hasattr(self.archival, 'custodialHistory'))
        self.assert_(hasattr(self.archival, 'dimensions'))
        self.assert_(hasattr(self.archival, 'distribution'))
        self.assert_(hasattr(self.archival, 'doi'))
        self.assert_(hasattr(self.archival, 'duration'))
        self.assert_(hasattr(self.archival, 'ean'))
        self.assert_(hasattr(self.archival, 'edition'))
        self.assert_(hasattr(self.archival, 'editionResponsibility'))
        self.assert_(hasattr(self.archival, 'extent'))
        self.assert_(hasattr(self.archival, 'fingerprint'))
        self.assert_(hasattr(self.archival, 'formatOfMusic'))
        self.assert_(hasattr(self.archival, 'frequency'))
        self.assert_(hasattr(self.archival, 'frequencyNote'))
        self.assert_(hasattr(self.archival, 'graphicScaleNote'))
        self.assert_(hasattr(self.archival, 'hasEquivalent'))
        self.assert_(hasattr(self.archival, 'hdl'))
        self.assert_(hasattr(self.archival, 'identifier'))
        self.assert_(hasattr(self.archival, 'illustrationNote'))
        self.assert_(hasattr(self.archival, 'instanceOf'))
        self.assert_(hasattr(self.archival, 'instanceTitle'))
        self.assert_(hasattr(self.archival, 'isbn'))
        self.assert_(hasattr(self.archival, 'isbn10'))
        self.assert_(hasattr(self.archival, 'isbn13'))
        self.assert_(hasattr(self.archival, 'ismn'))
        self.assert_(hasattr(self.archival, 'iso'))
        self.assert_(hasattr(self.archival, 'isrc'))
        self.assert_(hasattr(self.archival, 'issn'))
        self.assert_(hasattr(self.archival, 'issueNumber'))
        self.assert_(hasattr(self.archival, 'issuedWith'))
        self.assert_(hasattr(self.archival, 'keyTitle'))
        self.assert_(hasattr(self.archival, 'label'))
        self.assert_(hasattr(self.archival, 'lcOverseasAcq'))
        self.assert_(hasattr(self.archival, 'lccn'))
        self.assert_(hasattr(self.archival, 'legalDeposit'))
        self.assert_(hasattr(self.archival, 'local'))
        self.assert_(hasattr(self.archival, 'manufacture'))
        self.assert_(hasattr(self.archival, 'matrixNumber'))
        self.assert_(hasattr(self.archival, 'mediaCategory'))
        self.assert_(hasattr(self.archival, 'modeOfIssuance'))
        self.assert_(hasattr(self.archival, 'musicPlate'))
        self.assert_(hasattr(self.archival, 'musicPublisherNumber'))
        self.assert_(hasattr(self.archival, 'nban'))
        self.assert_(hasattr(self.archival, 'nbn'))
        self.assert_(hasattr(self.archival, 'notation'))
        self.assert_(hasattr(self.archival, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.archival, 'postalRegistration'))
        self.assert_(hasattr(self.archival, 'preferredCitation'))
        self.assert_(hasattr(self.archival, 'production'))
        self.assert_(hasattr(self.archival, 'provider'))
        self.assert_(hasattr(self.archival, 'providerStatement'))
        self.assert_(hasattr(self.archival, 'publication'))
        self.assert_(hasattr(self.archival, 'publisherNumber'))
        self.assert_(hasattr(self.archival, 'relatedInstance'))
        self.assert_(hasattr(self.archival, 'relatedTo'))
        self.assert_(hasattr(self.archival, 'reportNumber'))
        self.assert_(hasattr(self.archival, 'reproduction'))
        self.assert_(hasattr(self.archival, 'responsibilityStatement'))
        self.assert_(hasattr(self.archival, 'serialFirstIssue'))
        self.assert_(hasattr(self.archival, 'serialLastIssue'))
        self.assert_(hasattr(self.archival, 'sici'))
        self.assert_(hasattr(self.archival, 'soundContent'))
        self.assert_(hasattr(self.archival, 'stockNumber'))
        self.assert_(hasattr(self.archival, 'strn'))
        self.assert_(hasattr(self.archival, 'studyNumber'))
        self.assert_(hasattr(self.archival, 'supplementaryContentNote'))
        self.assert_(hasattr(self.archival, 'titleStatement'))
        self.assert_(hasattr(self.archival, 'upc'))
        self.assert_(hasattr(self.archival, 'uri'))
        self.assert_(hasattr(self.archival, 'urn'))
        self.assert_(hasattr(self.archival, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestArrangement(unittest.TestCase):

    def setUp(self):
        self.arrangement = Arrangement()

    def test_init(self):
        self.assertEquals(type(self.arrangement), Arrangement)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.arrangement, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.arrangement, 'identifier'))
        self.assert_(hasattr(self.arrangement, 'label'))
        self.assert_(hasattr(self.arrangement, 'materialArrangement'))
        self.assert_(hasattr(self.arrangement, 'materialHierarchicalLevel'))
        self.assert_(hasattr(self.arrangement, 'materialOrganization'))
        self.assert_(hasattr(self.arrangement, 'materialPart'))
        self.assert_(hasattr(self.arrangement, 'relatedTo'))

    def tearDown(self):
        pass

class TestAudio(unittest.TestCase):

    def setUp(self):
        self.audio = Audio()

    def test_init(self):
        self.assertEquals(type(self.audio), Audio)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.audio, 'absorbed'))
        self.assert_(hasattr(self.audio, 'absorbedBy'))
        self.assert_(hasattr(self.audio, 'absorbedInPart'))
        self.assert_(hasattr(self.audio, 'absorbedInPartBy'))
        self.assert_(hasattr(self.audio, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.audio, 'classification'))
        self.assert_(hasattr(self.audio, 'classificationDdc'))
        self.assert_(hasattr(self.audio, 'classificationLcc'))
        self.assert_(hasattr(self.audio, 'classificationNlm'))
        self.assert_(hasattr(self.audio, 'classificationUdc'))
        self.assert_(hasattr(self.audio, 'containedIn'))
        self.assert_(hasattr(self.audio, 'contains'))
        self.assert_(hasattr(self.audio, 'contentCategory'))
        self.assert_(hasattr(self.audio, 'continuedBy'))
        self.assert_(hasattr(self.audio, 'continuedInPartBy'))
        self.assert_(hasattr(self.audio, 'continues'))
        self.assert_(hasattr(self.audio, 'continuesInPart'))
        self.assert_(hasattr(self.audio, 'dataSource'))
        self.assert_(hasattr(self.audio, 'dissertationDegree'))
        self.assert_(hasattr(self.audio, 'dissertationIdentifier'))
        self.assert_(hasattr(self.audio, 'dissertationInstitution'))
        self.assert_(hasattr(self.audio, 'dissertationNote'))
        self.assert_(hasattr(self.audio, 'dissertationYear'))
        self.assert_(hasattr(self.audio, 'event'))
        self.assert_(hasattr(self.audio, 'expressionOf'))
        self.assert_(hasattr(self.audio, 'findingAid'))
        self.assert_(hasattr(self.audio, 'geographicCoverageNote'))
        self.assert_(hasattr(self.audio, 'hasDerivative'))
        self.assert_(hasattr(self.audio, 'hasExpression'))
        self.assert_(hasattr(self.audio, 'hasInstance'))
        self.assert_(hasattr(self.audio, 'identifier'))
        self.assert_(hasattr(self.audio, 'index'))
        self.assert_(hasattr(self.audio, 'isDerivativeOf'))
        self.assert_(hasattr(self.audio, 'isan'))
        self.assert_(hasattr(self.audio, 'issnL'))
        self.assert_(hasattr(self.audio, 'istc'))
        self.assert_(hasattr(self.audio, 'iswc'))
        self.assert_(hasattr(self.audio, 'label'))
        self.assert_(hasattr(self.audio, 'languageNote'))
        self.assert_(hasattr(self.audio, 'mergedToForm'))
        self.assert_(hasattr(self.audio, 'originDate'))
        self.assert_(hasattr(self.audio, 'originPlace'))
        self.assert_(hasattr(self.audio, 'originalVersion'))
        self.assert_(hasattr(self.audio, 'otherEdition'))
        self.assert_(hasattr(self.audio, 'precedes'))
        self.assert_(hasattr(self.audio, 'relatedTo'))
        self.assert_(hasattr(self.audio, 'relatedWork'))
        self.assert_(hasattr(self.audio, 'separatedFrom'))
        self.assert_(hasattr(self.audio, 'series'))
        self.assert_(hasattr(self.audio, 'splitInto'))
        self.assert_(hasattr(self.audio, 'subject'))
        self.assert_(hasattr(self.audio, 'subseries'))
        self.assert_(hasattr(self.audio, 'subseriesOf'))
        self.assert_(hasattr(self.audio, 'succeeds'))
        self.assert_(hasattr(self.audio, 'supersededBy'))
        self.assert_(hasattr(self.audio, 'supersededInPartBy'))
        self.assert_(hasattr(self.audio, 'supersedes'))
        self.assert_(hasattr(self.audio, 'supersedesInPart'))
        self.assert_(hasattr(self.audio, 'supplement'))
        self.assert_(hasattr(self.audio, 'supplementTo'))
        self.assert_(hasattr(self.audio, 'temporalCoverageNote'))
        self.assert_(hasattr(self.audio, 'translation'))
        self.assert_(hasattr(self.audio, 'translationOf'))
        self.assert_(hasattr(self.audio, 'unionOf'))
        self.assert_(hasattr(self.audio, 'workTitle'))

    def tearDown(self):
        pass

class TestAuthority(unittest.TestCase):

    def setUp(self):
        self.authority = Authority()

    def test_init(self):
        self.assert_(isinstance(self.authority, Authority))


    def test_rdf_properties(self):
        self.assert_(hasattr(self.authority, 'authorityAssigner'))
        self.assert_(hasattr(self.authority, 'authoritySource'))
        self.assert_(hasattr(self.authority, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.authority, 'hasAuthority'))
        self.assert_(hasattr(self.authority, 'identifier'))
        self.assert_(hasattr(self.authority, 'label'))
        self.assert_(hasattr(self.authority, 'relatedTo'))


    def test_hasAnnotation(self):
        pass


    def tearDown(self):
        pass


class TestCartography(unittest.TestCase):

    def setUp(self):
        self.cartography = Cartography()

    def test_init(self):
        self.assert_(isinstance(self.cartography, Cartography))

    def test_rdf_properties(self):
        self.assert_(hasattr(self.cartography, 'absorbed'))
        self.assert_(hasattr(self.cartography, 'absorbedBy'))
        self.assert_(hasattr(self.cartography, 'absorbedInPart'))
        self.assert_(hasattr(self.cartography, 'absorbedInPartBy'))
        self.assert_(hasattr(self.cartography, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.cartography, 'cartographicAscensionAndDeclination'))
        self.assert_(hasattr(self.cartography, 'cartographicCoordinates'))
        self.assert_(hasattr(self.cartography, 'cartographicEquinox'))
        self.assert_(hasattr(self.cartography, 'cartographicExclusionGRing'))
        self.assert_(hasattr(self.cartography, 'cartographicOuterGRing'))
        self.assert_(hasattr(self.cartography, 'cartographicProjection'))
        self.assert_(hasattr(self.cartography, 'cartographicScale'))
        self.assert_(hasattr(self.cartography, 'classification'))
        self.assert_(hasattr(self.cartography, 'classificationDdc'))
        self.assert_(hasattr(self.cartography, 'classificationLcc'))
        self.assert_(hasattr(self.cartography, 'classificationNlm'))
        self.assert_(hasattr(self.cartography, 'classificationUdc'))
        self.assert_(hasattr(self.cartography, 'containedIn'))
        self.assert_(hasattr(self.cartography, 'contains'))
        self.assert_(hasattr(self.cartography, 'contentCategory'))
        self.assert_(hasattr(self.cartography, 'continuedBy'))
        self.assert_(hasattr(self.cartography, 'continuedInPartBy'))
        self.assert_(hasattr(self.cartography, 'continues'))
        self.assert_(hasattr(self.cartography, 'continuesInPart'))
        self.assert_(hasattr(self.cartography, 'dataSource'))
        self.assert_(hasattr(self.cartography, 'dissertationDegree'))
        self.assert_(hasattr(self.cartography, 'dissertationIdentifier'))
        self.assert_(hasattr(self.cartography, 'dissertationInstitution'))
        self.assert_(hasattr(self.cartography, 'dissertationNote'))
        self.assert_(hasattr(self.cartography, 'dissertationYear'))
        self.assert_(hasattr(self.cartography, 'event'))
        self.assert_(hasattr(self.cartography, 'expressionOf'))
        self.assert_(hasattr(self.cartography, 'findingAid'))
        self.assert_(hasattr(self.cartography, 'geographicCoverageNote'))
        self.assert_(hasattr(self.cartography, 'hasDerivative'))
        self.assert_(hasattr(self.cartography, 'hasExpression'))
        self.assert_(hasattr(self.cartography, 'hasInstance'))
        self.assert_(hasattr(self.cartography, 'identifier'))
        self.assert_(hasattr(self.cartography, 'index'))
        self.assert_(hasattr(self.cartography, 'isDerivativeOf'))
        self.assert_(hasattr(self.cartography, 'isan'))
        self.assert_(hasattr(self.cartography, 'issnL'))
        self.assert_(hasattr(self.cartography, 'istc'))
        self.assert_(hasattr(self.cartography, 'iswc'))
        self.assert_(hasattr(self.cartography, 'label'))
        self.assert_(hasattr(self.cartography, 'languageNote'))
        self.assert_(hasattr(self.cartography, 'mergedToForm'))
        self.assert_(hasattr(self.cartography, 'originDate'))
        self.assert_(hasattr(self.cartography, 'originPlace'))
        self.assert_(hasattr(self.cartography, 'originalVersion'))
        self.assert_(hasattr(self.cartography, 'otherEdition'))
        self.assert_(hasattr(self.cartography, 'precedes'))
        self.assert_(hasattr(self.cartography, 'relatedTo'))
        self.assert_(hasattr(self.cartography, 'relatedWork'))
        self.assert_(hasattr(self.cartography, 'separatedFrom'))
        self.assert_(hasattr(self.cartography, 'series'))
        self.assert_(hasattr(self.cartography, 'splitInto'))
        self.assert_(hasattr(self.cartography, 'subject'))
        self.assert_(hasattr(self.cartography, 'subseries'))
        self.assert_(hasattr(self.cartography, 'subseriesOf'))
        self.assert_(hasattr(self.cartography, 'succeeds'))
        self.assert_(hasattr(self.cartography, 'supersededBy'))
        self.assert_(hasattr(self.cartography, 'supersededInPartBy'))
        self.assert_(hasattr(self.cartography, 'supersedes'))
        self.assert_(hasattr(self.cartography, 'supersedesInPart'))
        self.assert_(hasattr(self.cartography, 'supplement'))
        self.assert_(hasattr(self.cartography, 'supplementTo'))
        self.assert_(hasattr(self.cartography, 'temporalCoverageNote'))
        self.assert_(hasattr(self.cartography, 'translation'))
        self.assert_(hasattr(self.cartography, 'translationOf'))
        self.assert_(hasattr(self.cartography, 'unionOf'))
        self.assert_(hasattr(self.cartography, 'workTitle'))


    def tearDown(self):
        pass

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.category = Category()

    def test_init(self):
        self.assertEquals(type(self.category), Category)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.category, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.category, 'categorySource'))
        self.assert_(hasattr(self.category, 'categoryType'))
        self.assert_(hasattr(self.category, 'categoryValue'))
        self.assert_(hasattr(self.category, 'identifier'))
        self.assert_(hasattr(self.category, 'label'))
        self.assert_(hasattr(self.category, 'relatedTo'))

    def tearDown(self):
        pass

class TestClassification(unittest.TestCase):

    def setUp(self):
        self.classification = Classification()

    def test_init(self):
        self.assertEquals(type(self.classification), Classification)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.classification, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.classification, 'classificationAssigner'))
        self.assert_(hasattr(self.classification, 'classificationDesignation'))
        self.assert_(hasattr(self.classification, 'classificationEdition'))
        self.assert_(hasattr(self.classification, 'classificationItem'))
        self.assert_(hasattr(self.classification, 'classificationNumber'))
        self.assert_(hasattr(self.classification, 'classificationNumberUri'))
        self.assert_(hasattr(self.classification, 'classificationScheme'))
        self.assert_(hasattr(self.classification, 'classificationSpanEnd'))
        self.assert_(hasattr(self.classification, 'classificationStatus'))
        self.assert_(hasattr(self.classification, 'classificationTable'))
        self.assert_(hasattr(self.classification, 'classificationTableSeq'))
        self.assert_(hasattr(self.classification, 'identifier'))
        self.assert_(hasattr(self.classification, 'label'))
        self.assert_(hasattr(self.classification, 'relatedTo'))

    def tearDown(self):
        pass


class TestCollection(unittest.TestCase):

    def setUp(self):
        self.collection = Collection()

    def test_init(self):
        self.assertEquals(type(self.collection), Collection)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.collection, 'abbreviatedTitle'))
        self.assert_(hasattr(self.collection, 'ansi'))
        self.assert_(hasattr(self.collection, 'arrangement'))
        self.assert_(hasattr(self.collection, 'aspectRatio'))
        self.assert_(hasattr(self.collection, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.collection, 'awardNote'))
        self.assert_(hasattr(self.collection, 'carrierCategory'))
        self.assert_(hasattr(self.collection, 'coden'))
        self.assert_(hasattr(self.collection, 'colorContent'))
        self.assert_(hasattr(self.collection, 'contentAccessibility'))
        self.assert_(hasattr(self.collection, 'contentsNote'))
        self.assert_(hasattr(self.collection, 'custodialHistory'))
        self.assert_(hasattr(self.collection, 'dimensions'))
        self.assert_(hasattr(self.collection, 'distribution'))
        self.assert_(hasattr(self.collection, 'doi'))
        self.assert_(hasattr(self.collection, 'duration'))
        self.assert_(hasattr(self.collection, 'ean'))
        self.assert_(hasattr(self.collection, 'edition'))
        self.assert_(hasattr(self.collection, 'editionResponsibility'))
        self.assert_(hasattr(self.collection, 'extent'))
        self.assert_(hasattr(self.collection, 'fingerprint'))
        self.assert_(hasattr(self.collection, 'formatOfMusic'))
        self.assert_(hasattr(self.collection, 'frequency'))
        self.assert_(hasattr(self.collection, 'frequencyNote'))
        self.assert_(hasattr(self.collection, 'graphicScaleNote'))
        self.assert_(hasattr(self.collection, 'hasEquivalent'))
        self.assert_(hasattr(self.collection, 'hdl'))
        self.assert_(hasattr(self.collection, 'identifier'))
        self.assert_(hasattr(self.collection, 'illustrationNote'))
        self.assert_(hasattr(self.collection, 'instanceOf'))
        self.assert_(hasattr(self.collection, 'instanceTitle'))
        self.assert_(hasattr(self.collection, 'isbn'))
        self.assert_(hasattr(self.collection, 'isbn10'))
        self.assert_(hasattr(self.collection, 'isbn13'))
        self.assert_(hasattr(self.collection, 'ismn'))
        self.assert_(hasattr(self.collection, 'iso'))
        self.assert_(hasattr(self.collection, 'isrc'))
        self.assert_(hasattr(self.collection, 'issn'))
        self.assert_(hasattr(self.collection, 'issueNumber'))
        self.assert_(hasattr(self.collection, 'issuedWith'))
        self.assert_(hasattr(self.collection, 'keyTitle'))
        self.assert_(hasattr(self.collection, 'label'))
        self.assert_(hasattr(self.collection, 'lcOverseasAcq'))
        self.assert_(hasattr(self.collection, 'lccn'))
        self.assert_(hasattr(self.collection, 'legalDeposit'))
        self.assert_(hasattr(self.collection, 'local'))
        self.assert_(hasattr(self.collection, 'manufacture'))
        self.assert_(hasattr(self.collection, 'matrixNumber'))
        self.assert_(hasattr(self.collection, 'mediaCategory'))
        self.assert_(hasattr(self.collection, 'modeOfIssuance'))
        self.assert_(hasattr(self.collection, 'musicPlate'))
        self.assert_(hasattr(self.collection, 'musicPublisherNumber'))
        self.assert_(hasattr(self.collection, 'nban'))
        self.assert_(hasattr(self.collection, 'nbn'))
        self.assert_(hasattr(self.collection, 'notation'))
        self.assert_(hasattr(self.collection, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.collection, 'postalRegistration'))
        self.assert_(hasattr(self.collection, 'preferredCitation'))
        self.assert_(hasattr(self.collection, 'production'))
        self.assert_(hasattr(self.collection, 'provider'))
        self.assert_(hasattr(self.collection, 'providerStatement'))
        self.assert_(hasattr(self.collection, 'publication'))
        self.assert_(hasattr(self.collection, 'publisherNumber'))
        self.assert_(hasattr(self.collection, 'relatedInstance'))
        self.assert_(hasattr(self.collection, 'relatedTo'))
        self.assert_(hasattr(self.collection, 'reportNumber'))
        self.assert_(hasattr(self.collection, 'reproduction'))
        self.assert_(hasattr(self.collection, 'responsibilityStatement'))
        self.assert_(hasattr(self.collection, 'serialFirstIssue'))
        self.assert_(hasattr(self.collection, 'serialLastIssue'))
        self.assert_(hasattr(self.collection, 'sici'))
        self.assert_(hasattr(self.collection, 'soundContent'))
        self.assert_(hasattr(self.collection, 'stockNumber'))
        self.assert_(hasattr(self.collection, 'strn'))
        self.assert_(hasattr(self.collection, 'studyNumber'))
        self.assert_(hasattr(self.collection, 'supplementaryContentNote'))
        self.assert_(hasattr(self.collection, 'titleStatement'))
        self.assert_(hasattr(self.collection, 'upc'))
        self.assert_(hasattr(self.collection, 'uri'))
        self.assert_(hasattr(self.collection, 'urn'))
        self.assert_(hasattr(self.collection, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestCoverArt(unittest.TestCase):

    def setUp(self):
        self.coverart = CoverArt()

    def test_init(self):
        self.assertEquals(type(self.coverart), CoverArt)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.coverart, 'annotates'))
        self.assert_(hasattr(self.coverart, 'annotationAssertedBy'))
        self.assert_(hasattr(self.coverart, 'annotationBody'))
        self.assert_(hasattr(self.coverart, 'annotationSource'))
        self.assert_(hasattr(self.coverart, 'assertionDate'))
        self.assert_(hasattr(self.coverart, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.coverart, 'coverArt'))
        self.assert_(hasattr(self.coverart, 'coverArtFor'))
        self.assert_(hasattr(self.coverart, 'coverArtThumb'))
        self.assert_(hasattr(self.coverart, 'identifier'))
        self.assert_(hasattr(self.coverart, 'label'))
        self.assert_(hasattr(self.coverart, 'relatedTo'))

    def tearDown(self):
        pass

class TestDataset(unittest.TestCase):

    def setUp(self):
        self.dataset = Dataset()

    def test_init(self):
        self.assertEquals(type(self.dataset), Dataset)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.dataset, 'absorbed'))
        self.assert_(hasattr(self.dataset, 'absorbedBy'))
        self.assert_(hasattr(self.dataset, 'absorbedInPart'))
        self.assert_(hasattr(self.dataset, 'absorbedInPartBy'))
        self.assert_(hasattr(self.dataset, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.dataset, 'classification'))
        self.assert_(hasattr(self.dataset, 'classificationDdc'))
        self.assert_(hasattr(self.dataset, 'classificationLcc'))
        self.assert_(hasattr(self.dataset, 'classificationNlm'))
        self.assert_(hasattr(self.dataset, 'classificationUdc'))
        self.assert_(hasattr(self.dataset, 'containedIn'))
        self.assert_(hasattr(self.dataset, 'contains'))
        self.assert_(hasattr(self.dataset, 'contentCategory'))
        self.assert_(hasattr(self.dataset, 'continuedBy'))
        self.assert_(hasattr(self.dataset, 'continuedInPartBy'))
        self.assert_(hasattr(self.dataset, 'continues'))
        self.assert_(hasattr(self.dataset, 'continuesInPart'))
        self.assert_(hasattr(self.dataset, 'dataSource'))
        self.assert_(hasattr(self.dataset, 'dissertationDegree'))
        self.assert_(hasattr(self.dataset, 'dissertationIdentifier'))
        self.assert_(hasattr(self.dataset, 'dissertationInstitution'))
        self.assert_(hasattr(self.dataset, 'dissertationNote'))
        self.assert_(hasattr(self.dataset, 'dissertationYear'))
        self.assert_(hasattr(self.dataset, 'event'))
        self.assert_(hasattr(self.dataset, 'expressionOf'))
        self.assert_(hasattr(self.dataset, 'findingAid'))
        self.assert_(hasattr(self.dataset, 'geographicCoverageNote'))
        self.assert_(hasattr(self.dataset, 'hasDerivative'))
        self.assert_(hasattr(self.dataset, 'hasExpression'))
        self.assert_(hasattr(self.dataset, 'hasInstance'))
        self.assert_(hasattr(self.dataset, 'identifier'))
        self.assert_(hasattr(self.dataset, 'index'))
        self.assert_(hasattr(self.dataset, 'isDerivativeOf'))
        self.assert_(hasattr(self.dataset, 'isan'))
        self.assert_(hasattr(self.dataset, 'issnL'))
        self.assert_(hasattr(self.dataset, 'istc'))
        self.assert_(hasattr(self.dataset, 'iswc'))
        self.assert_(hasattr(self.dataset, 'label'))
        self.assert_(hasattr(self.dataset, 'languageNote'))
        self.assert_(hasattr(self.dataset, 'mergedToForm'))
        self.assert_(hasattr(self.dataset, 'originDate'))
        self.assert_(hasattr(self.dataset, 'originPlace'))
        self.assert_(hasattr(self.dataset, 'originalVersion'))
        self.assert_(hasattr(self.dataset, 'otherEdition'))
        self.assert_(hasattr(self.dataset, 'precedes'))
        self.assert_(hasattr(self.dataset, 'relatedTo'))
        self.assert_(hasattr(self.dataset, 'relatedWork'))
        self.assert_(hasattr(self.dataset, 'separatedFrom'))
        self.assert_(hasattr(self.dataset, 'series'))
        self.assert_(hasattr(self.dataset, 'splitInto'))
        self.assert_(hasattr(self.dataset, 'subject'))
        self.assert_(hasattr(self.dataset, 'subseries'))
        self.assert_(hasattr(self.dataset, 'subseriesOf'))
        self.assert_(hasattr(self.dataset, 'succeeds'))
        self.assert_(hasattr(self.dataset, 'supersededBy'))
        self.assert_(hasattr(self.dataset, 'supersededInPartBy'))
        self.assert_(hasattr(self.dataset, 'supersedes'))
        self.assert_(hasattr(self.dataset, 'supersedesInPart'))
        self.assert_(hasattr(self.dataset, 'supplement'))
        self.assert_(hasattr(self.dataset, 'supplementTo'))
        self.assert_(hasattr(self.dataset, 'temporalCoverageNote'))
        self.assert_(hasattr(self.dataset, 'translation'))
        self.assert_(hasattr(self.dataset, 'translationOf'))
        self.assert_(hasattr(self.dataset, 'unionOf'))
        self.assert_(hasattr(self.dataset, 'workTitle'))

    def tearDown(self):
        pass

class TestDescriptionAdminInfo(unittest.TestCase):

    def setUp(self):
        self.descriptionadmininfo = DescriptionAdminInfo()


    def test_init(self):
        self.assertEquals(type(self.descriptionadmininfo), DescriptionAdminInfo)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.descriptionadmininfo, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.descriptionadmininfo, 'identifier'))
        self.assert_(hasattr(self.descriptionadmininfo, 'label'))
        self.assert_(hasattr(self.descriptionadmininfo, 'relatedTo'))


    def tearDown(self):
        pass

class TestElectronic(unittest.TestCase):
    def setUp(self):
        self.electronic = Electronic()


    def test_init(self):
        self.assertEquals(type(self.electronic), Electronic)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.electronic, 'abbreviatedTitle'))
        self.assert_(hasattr(self.electronic, 'ansi'))
        self.assert_(hasattr(self.electronic, 'arrangement'))
        self.assert_(hasattr(self.electronic, 'aspectRatio'))
        self.assert_(hasattr(self.electronic, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.electronic, 'awardNote'))
        self.assert_(hasattr(self.electronic, 'carrierCategory'))
        self.assert_(hasattr(self.electronic, 'coden'))
        self.assert_(hasattr(self.electronic, 'colorContent'))
        self.assert_(hasattr(self.electronic, 'contentAccessibility'))
        self.assert_(hasattr(self.electronic, 'contentsNote'))
        self.assert_(hasattr(self.electronic, 'custodialHistory'))
        self.assert_(hasattr(self.electronic, 'dimensions'))
        self.assert_(hasattr(self.electronic, 'distribution'))
        self.assert_(hasattr(self.electronic, 'doi'))
        self.assert_(hasattr(self.electronic, 'duration'))
        self.assert_(hasattr(self.electronic, 'ean'))
        self.assert_(hasattr(self.electronic, 'edition'))
        self.assert_(hasattr(self.electronic, 'editionResponsibility'))
        self.assert_(hasattr(self.electronic, 'extent'))
        self.assert_(hasattr(self.electronic, 'fingerprint'))
        self.assert_(hasattr(self.electronic, 'formatOfMusic'))
        self.assert_(hasattr(self.electronic, 'frequency'))
        self.assert_(hasattr(self.electronic, 'frequencyNote'))
        self.assert_(hasattr(self.electronic, 'graphicScaleNote'))
        self.assert_(hasattr(self.electronic, 'hasEquivalent'))
        self.assert_(hasattr(self.electronic, 'hdl'))
        self.assert_(hasattr(self.electronic, 'identifier'))
        self.assert_(hasattr(self.electronic, 'illustrationNote'))
        self.assert_(hasattr(self.electronic, 'instanceOf'))
        self.assert_(hasattr(self.electronic, 'instanceTitle'))
        self.assert_(hasattr(self.electronic, 'isbn'))
        self.assert_(hasattr(self.electronic, 'isbn10'))
        self.assert_(hasattr(self.electronic, 'isbn13'))
        self.assert_(hasattr(self.electronic, 'ismn'))
        self.assert_(hasattr(self.electronic, 'iso'))
        self.assert_(hasattr(self.electronic, 'isrc'))
        self.assert_(hasattr(self.electronic, 'issn'))
        self.assert_(hasattr(self.electronic, 'issueNumber'))
        self.assert_(hasattr(self.electronic, 'issuedWith'))
        self.assert_(hasattr(self.electronic, 'keyTitle'))
        self.assert_(hasattr(self.electronic, 'label'))
        self.assert_(hasattr(self.electronic, 'lcOverseasAcq'))
        self.assert_(hasattr(self.electronic, 'lccn'))
        self.assert_(hasattr(self.electronic, 'legalDeposit'))
        self.assert_(hasattr(self.electronic, 'local'))
        self.assert_(hasattr(self.electronic, 'manufacture'))
        self.assert_(hasattr(self.electronic, 'matrixNumber'))
        self.assert_(hasattr(self.electronic, 'mediaCategory'))
        self.assert_(hasattr(self.electronic, 'modeOfIssuance'))
        self.assert_(hasattr(self.electronic, 'musicPlate'))
        self.assert_(hasattr(self.electronic, 'musicPublisherNumber'))
        self.assert_(hasattr(self.electronic, 'nban'))
        self.assert_(hasattr(self.electronic, 'nbn'))
        self.assert_(hasattr(self.electronic, 'notation'))
        self.assert_(hasattr(self.electronic, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.electronic, 'postalRegistration'))
        self.assert_(hasattr(self.electronic, 'preferredCitation'))
        self.assert_(hasattr(self.electronic, 'production'))
        self.assert_(hasattr(self.electronic, 'provider'))
        self.assert_(hasattr(self.electronic, 'providerStatement'))
        self.assert_(hasattr(self.electronic, 'publication'))
        self.assert_(hasattr(self.electronic, 'publisherNumber'))
        self.assert_(hasattr(self.electronic, 'relatedInstance'))
        self.assert_(hasattr(self.electronic, 'relatedTo'))
        self.assert_(hasattr(self.electronic, 'reportNumber'))
        self.assert_(hasattr(self.electronic, 'reproduction'))
        self.assert_(hasattr(self.electronic, 'responsibilityStatement'))
        self.assert_(hasattr(self.electronic, 'serialFirstIssue'))
        self.assert_(hasattr(self.electronic, 'serialLastIssue'))
        self.assert_(hasattr(self.electronic, 'sici'))
        self.assert_(hasattr(self.electronic, 'soundContent'))
        self.assert_(hasattr(self.electronic, 'stockNumber'))
        self.assert_(hasattr(self.electronic, 'strn'))
        self.assert_(hasattr(self.electronic, 'studyNumber'))
        self.assert_(hasattr(self.electronic, 'supplementaryContentNote'))
        self.assert_(hasattr(self.electronic, 'titleStatement'))
        self.assert_(hasattr(self.electronic, 'upc'))
        self.assert_(hasattr(self.electronic, 'uri'))
        self.assert_(hasattr(self.electronic, 'urn'))
        self.assert_(hasattr(self.electronic, 'videorecordingNumber'))

class TestEvent(unittest.TestCase):
    def setUp(self):
        self.event = Event()


    def test_init(self):
        self.assertEquals(type(self.event), Event)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.event, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.event, 'eventAgent'))
        self.assert_(hasattr(self.event, 'eventDate'))
        self.assert_(hasattr(self.event, 'eventPlace'))
        self.assert_(hasattr(self.event, 'identifier'))
        self.assert_(hasattr(self.event, 'label'))
        self.assert_(hasattr(self.event, 'relatedTo'))


    def tearDown(self):
        pass

    def tearDown(self):
        pass

class TestFamily(unittest.TestCase):

    def setUp(self):
        self.family = Family()


    def test_init(self):
        self.assertEquals(type(self.family), Family)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.family, 'authorityAssigner'))
        self.assert_(hasattr(self.family, 'authoritySource'))
        self.assert_(hasattr(self.family, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.family, 'hasAuthority'))
        self.assert_(hasattr(self.family, 'identifier'))
        self.assert_(hasattr(self.family, 'label'))
        self.assert_(hasattr(self.family, 'relatedTo'))

    def tearDown(self):
        pass

class TestHeldItem(unittest.TestCase):
    def setUp(self):
        self.helditem = HeldItem()


    def test_init(self):
        self.assertEquals(type(self.helditem), HeldItem)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.helditem, 'accessCondition'))
        self.assert_(hasattr(self.helditem, 'annotates'))
        self.assert_(hasattr(self.helditem, 'annotationAssertedBy'))
        self.assert_(hasattr(self.helditem, 'annotationBody'))
        self.assert_(hasattr(self.helditem, 'annotationSource'))
        self.assert_(hasattr(self.helditem, 'assertionDate'))
        self.assert_(hasattr(self.helditem, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.helditem, 'barcode'))
        self.assert_(hasattr(self.helditem, 'circulationStatus'))
        self.assert_(hasattr(self.helditem, 'componentOf'))
        self.assert_(hasattr(self.helditem, 'copyNote'))
        self.assert_(hasattr(self.helditem, 'enumerationAndChronology'))
        self.assert_(hasattr(self.helditem, 'heldBy'))
        self.assert_(hasattr(self.helditem, 'holdingFor'))
        self.assert_(hasattr(self.helditem, 'identifier'))
        self.assert_(hasattr(self.helditem, 'itemId'))
        self.assert_(hasattr(self.helditem, 'label'))
        self.assert_(hasattr(self.helditem, 'lendingPolicy'))
        self.assert_(hasattr(self.helditem, 'relatedTo'))
        self.assert_(hasattr(self.helditem, 'reproductionPolicy'))
        self.assert_(hasattr(self.helditem, 'retentionPolicy'))
        self.assert_(hasattr(self.helditem, 'shelfMark'))
        self.assert_(hasattr(self.helditem, 'shelfMarkDdc'))
        self.assert_(hasattr(self.helditem, 'shelfMarkLcc'))
        self.assert_(hasattr(self.helditem, 'shelfMarkNlm'))
        self.assert_(hasattr(self.helditem, 'shelfMarkScheme'))
        self.assert_(hasattr(self.helditem, 'shelfMarkUdc'))
        self.assert_(hasattr(self.helditem, 'subLocation'))


    def tearDown(self):
        pass

class TestHeldMaterial(unittest.TestCase):
    def setUp(self):
        self.heldmaterial = HeldMaterial()


    def test_init(self):
        self.assertEquals(type(self.heldmaterial), HeldMaterial)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.heldmaterial, 'accessCondition'))
        self.assert_(hasattr(self.heldmaterial, 'annotates'))
        self.assert_(hasattr(self.heldmaterial, 'annotationAssertedBy'))
        self.assert_(hasattr(self.heldmaterial, 'annotationBody'))
        self.assert_(hasattr(self.heldmaterial, 'annotationSource'))
        self.assert_(hasattr(self.heldmaterial, 'assertionDate'))
        self.assert_(hasattr(self.heldmaterial, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.heldmaterial, 'enumerationAndChronology'))
        self.assert_(hasattr(self.heldmaterial, 'heldBy'))
        self.assert_(hasattr(self.heldmaterial, 'holdingFor'))
        self.assert_(hasattr(self.heldmaterial, 'identifier'))
        self.assert_(hasattr(self.heldmaterial, 'label'))
        self.assert_(hasattr(self.heldmaterial, 'lendingPolicy'))
        self.assert_(hasattr(self.heldmaterial, 'relatedTo'))
        self.assert_(hasattr(self.heldmaterial, 'reproductionPolicy'))
        self.assert_(hasattr(self.heldmaterial, 'retentionPolicy'))
        self.assert_(hasattr(self.heldmaterial, 'subLocation'))


    def tearDown(self):
        pass


class TestIdentifier(unittest.TestCase):
    def setUp(self):
        self.identifier = Identifier()


    def test_init(self):
        self.assertEquals(type(self.identifier), Identifier)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.identifier, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.identifier, 'identifier'))
        self.assert_(hasattr(self.identifier, 'identifierAssigner'))
        self.assert_(hasattr(self.identifier, 'identifierQualifier'))
        self.assert_(hasattr(self.identifier, 'identifierScheme'))
        self.assert_(hasattr(self.identifier, 'identifierStatus'))
        self.assert_(hasattr(self.identifier, 'identifierValue'))
        self.assert_(hasattr(self.identifier, 'label'))
        self.assert_(hasattr(self.identifier, 'relatedTo'))


    def tearDown(self):
        pass

class TestInstance(unittest.TestCase):
    def setUp(self):
        self.instance = Instance()


    def test_init(self):
        self.assertEquals(type(self.instance), Instance)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.instance, 'abbreviatedTitle'))
        self.assert_(hasattr(self.instance, 'ansi'))
        self.assert_(hasattr(self.instance, 'arrangement'))
        self.assert_(hasattr(self.instance, 'aspectRatio'))
        self.assert_(hasattr(self.instance, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.instance, 'awardNote'))
        self.assert_(hasattr(self.instance, 'carrierCategory'))
        self.assert_(hasattr(self.instance, 'coden'))
        self.assert_(hasattr(self.instance, 'colorContent'))
        self.assert_(hasattr(self.instance, 'contentAccessibility'))
        self.assert_(hasattr(self.instance, 'contentsNote'))
        self.assert_(hasattr(self.instance, 'custodialHistory'))
        self.assert_(hasattr(self.instance, 'dimensions'))
        self.assert_(hasattr(self.instance, 'distribution'))
        self.assert_(hasattr(self.instance, 'doi'))
        self.assert_(hasattr(self.instance, 'duration'))
        self.assert_(hasattr(self.instance, 'ean'))
        self.assert_(hasattr(self.instance, 'edition'))
        self.assert_(hasattr(self.instance, 'editionResponsibility'))
        self.assert_(hasattr(self.instance, 'extent'))
        self.assert_(hasattr(self.instance, 'fingerprint'))
        self.assert_(hasattr(self.instance, 'formatOfMusic'))
        self.assert_(hasattr(self.instance, 'frequency'))
        self.assert_(hasattr(self.instance, 'frequencyNote'))
        self.assert_(hasattr(self.instance, 'graphicScaleNote'))
        self.assert_(hasattr(self.instance, 'hasEquivalent'))
        self.assert_(hasattr(self.instance, 'hdl'))
        self.assert_(hasattr(self.instance, 'identifier'))
        self.assert_(hasattr(self.instance, 'illustrationNote'))
        self.assert_(hasattr(self.instance, 'instanceOf'))
        self.assert_(hasattr(self.instance, 'instanceTitle'))
        self.assert_(hasattr(self.instance, 'isbn'))
        self.assert_(hasattr(self.instance, 'isbn10'))
        self.assert_(hasattr(self.instance, 'isbn13'))
        self.assert_(hasattr(self.instance, 'ismn'))
        self.assert_(hasattr(self.instance, 'iso'))
        self.assert_(hasattr(self.instance, 'isrc'))
        self.assert_(hasattr(self.instance, 'issn'))
        self.assert_(hasattr(self.instance, 'issueNumber'))
        self.assert_(hasattr(self.instance, 'issuedWith'))
        self.assert_(hasattr(self.instance, 'keyTitle'))
        self.assert_(hasattr(self.instance, 'label'))
        self.assert_(hasattr(self.instance, 'lcOverseasAcq'))
        self.assert_(hasattr(self.instance, 'lccn'))
        self.assert_(hasattr(self.instance, 'legalDeposit'))
        self.assert_(hasattr(self.instance, 'local'))
        self.assert_(hasattr(self.instance, 'manufacture'))
        self.assert_(hasattr(self.instance, 'matrixNumber'))
        self.assert_(hasattr(self.instance, 'mediaCategory'))
        self.assert_(hasattr(self.instance, 'modeOfIssuance'))
        self.assert_(hasattr(self.instance, 'musicPlate'))
        self.assert_(hasattr(self.instance, 'musicPublisherNumber'))
        self.assert_(hasattr(self.instance, 'nban'))
        self.assert_(hasattr(self.instance, 'nbn'))
        self.assert_(hasattr(self.instance, 'notation'))
        self.assert_(hasattr(self.instance, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.instance, 'postalRegistration'))
        self.assert_(hasattr(self.instance, 'preferredCitation'))
        self.assert_(hasattr(self.instance, 'production'))
        self.assert_(hasattr(self.instance, 'provider'))
        self.assert_(hasattr(self.instance, 'providerStatement'))
        self.assert_(hasattr(self.instance, 'publication'))
        self.assert_(hasattr(self.instance, 'publisherNumber'))
        self.assert_(hasattr(self.instance, 'relatedInstance'))
        self.assert_(hasattr(self.instance, 'relatedTo'))
        self.assert_(hasattr(self.instance, 'reportNumber'))
        self.assert_(hasattr(self.instance, 'reproduction'))
        self.assert_(hasattr(self.instance, 'responsibilityStatement'))
        self.assert_(hasattr(self.instance, 'serialFirstIssue'))
        self.assert_(hasattr(self.instance, 'serialLastIssue'))
        self.assert_(hasattr(self.instance, 'sici'))
        self.assert_(hasattr(self.instance, 'soundContent'))
        self.assert_(hasattr(self.instance, 'stockNumber'))
        self.assert_(hasattr(self.instance, 'strn'))
        self.assert_(hasattr(self.instance, 'studyNumber'))
        self.assert_(hasattr(self.instance, 'supplementaryContentNote'))
        self.assert_(hasattr(self.instance, 'titleStatement'))
        self.assert_(hasattr(self.instance, 'upc'))
        self.assert_(hasattr(self.instance, 'uri'))
        self.assert_(hasattr(self.instance, 'urn'))
        self.assert_(hasattr(self.instance, 'videorecordingNumber'))


    def tearDown(self):
        pass

class TestIntegrating(unittest.TestCase):
    def setUp(self):
        self.integrating = Integrating()


    def test_init(self):
        self.assertEquals(type(self.integrating), Integrating)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.integrating, 'abbreviatedTitle'))
        self.assert_(hasattr(self.integrating, 'ansi'))
        self.assert_(hasattr(self.integrating, 'arrangement'))
        self.assert_(hasattr(self.integrating, 'aspectRatio'))
        self.assert_(hasattr(self.integrating, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.integrating, 'awardNote'))
        self.assert_(hasattr(self.integrating, 'carrierCategory'))
        self.assert_(hasattr(self.integrating, 'coden'))
        self.assert_(hasattr(self.integrating, 'colorContent'))
        self.assert_(hasattr(self.integrating, 'contentAccessibility'))
        self.assert_(hasattr(self.integrating, 'contentsNote'))
        self.assert_(hasattr(self.integrating, 'custodialHistory'))
        self.assert_(hasattr(self.integrating, 'dimensions'))
        self.assert_(hasattr(self.integrating, 'distribution'))
        self.assert_(hasattr(self.integrating, 'doi'))
        self.assert_(hasattr(self.integrating, 'duration'))
        self.assert_(hasattr(self.integrating, 'ean'))
        self.assert_(hasattr(self.integrating, 'edition'))
        self.assert_(hasattr(self.integrating, 'editionResponsibility'))
        self.assert_(hasattr(self.integrating, 'extent'))
        self.assert_(hasattr(self.integrating, 'fingerprint'))
        self.assert_(hasattr(self.integrating, 'formatOfMusic'))
        self.assert_(hasattr(self.integrating, 'frequency'))
        self.assert_(hasattr(self.integrating, 'frequencyNote'))
        self.assert_(hasattr(self.integrating, 'graphicScaleNote'))
        self.assert_(hasattr(self.integrating, 'hasEquivalent'))
        self.assert_(hasattr(self.integrating, 'hdl'))
        self.assert_(hasattr(self.integrating, 'identifier'))
        self.assert_(hasattr(self.integrating, 'illustrationNote'))
        self.assert_(hasattr(self.integrating, 'instanceOf'))
        self.assert_(hasattr(self.integrating, 'instanceTitle'))
        self.assert_(hasattr(self.integrating, 'isbn'))
        self.assert_(hasattr(self.integrating, 'isbn10'))
        self.assert_(hasattr(self.integrating, 'isbn13'))
        self.assert_(hasattr(self.integrating, 'ismn'))
        self.assert_(hasattr(self.integrating, 'iso'))
        self.assert_(hasattr(self.integrating, 'isrc'))
        self.assert_(hasattr(self.integrating, 'issn'))
        self.assert_(hasattr(self.integrating, 'issueNumber'))
        self.assert_(hasattr(self.integrating, 'issuedWith'))
        self.assert_(hasattr(self.integrating, 'keyTitle'))
        self.assert_(hasattr(self.integrating, 'label'))
        self.assert_(hasattr(self.integrating, 'lcOverseasAcq'))
        self.assert_(hasattr(self.integrating, 'lccn'))
        self.assert_(hasattr(self.integrating, 'legalDeposit'))
        self.assert_(hasattr(self.integrating, 'local'))
        self.assert_(hasattr(self.integrating, 'manufacture'))
        self.assert_(hasattr(self.integrating, 'matrixNumber'))
        self.assert_(hasattr(self.integrating, 'mediaCategory'))
        self.assert_(hasattr(self.integrating, 'modeOfIssuance'))
        self.assert_(hasattr(self.integrating, 'musicPlate'))
        self.assert_(hasattr(self.integrating, 'musicPublisherNumber'))
        self.assert_(hasattr(self.integrating, 'nban'))
        self.assert_(hasattr(self.integrating, 'nbn'))
        self.assert_(hasattr(self.integrating, 'notation'))
        self.assert_(hasattr(self.integrating, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.integrating, 'postalRegistration'))
        self.assert_(hasattr(self.integrating, 'preferredCitation'))
        self.assert_(hasattr(self.integrating, 'production'))
        self.assert_(hasattr(self.integrating, 'provider'))
        self.assert_(hasattr(self.integrating, 'providerStatement'))
        self.assert_(hasattr(self.integrating, 'publication'))
        self.assert_(hasattr(self.integrating, 'publisherNumber'))
        self.assert_(hasattr(self.integrating, 'relatedInstance'))
        self.assert_(hasattr(self.integrating, 'relatedTo'))
        self.assert_(hasattr(self.integrating, 'reportNumber'))
        self.assert_(hasattr(self.integrating, 'reproduction'))
        self.assert_(hasattr(self.integrating, 'responsibilityStatement'))
        self.assert_(hasattr(self.integrating, 'serialFirstIssue'))
        self.assert_(hasattr(self.integrating, 'serialLastIssue'))
        self.assert_(hasattr(self.integrating, 'sici'))
        self.assert_(hasattr(self.integrating, 'soundContent'))
        self.assert_(hasattr(self.integrating, 'stockNumber'))
        self.assert_(hasattr(self.integrating, 'strn'))
        self.assert_(hasattr(self.integrating, 'studyNumber'))
        self.assert_(hasattr(self.integrating, 'supplementaryContentNote'))
        self.assert_(hasattr(self.integrating, 'titleStatement'))
        self.assert_(hasattr(self.integrating, 'upc'))
        self.assert_(hasattr(self.integrating, 'uri'))
        self.assert_(hasattr(self.integrating, 'urn'))
        self.assert_(hasattr(self.integrating, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestIntendedAudience(unittest.TestCase):
    def setUp(self):
        self.intendedaudience = IntendedAudience()


    def test_init(self):
        self.assertEquals(type(self.intendedaudience), IntendedAudience)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.intendedaudience, 'audience'))
        self.assert_(hasattr(self.intendedaudience, 'audienceAssigner'))
        self.assert_(hasattr(self.intendedaudience, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.intendedaudience, 'identifier'))
        self.assert_(hasattr(self.intendedaudience, 'label'))
        self.assert_(hasattr(self.intendedaudience, 'relatedTo'))

    def tearDown(self):
        pass


class TestJurisdiction(unittest.TestCase):

    def setUp(self):
        self.jurisdiction = Jurisdiction()


    def test_init(self):
        self.assertEquals(type(self.jurisdiction), Jurisdiction)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.jurisdiction, 'authorityAssigner'))
        self.assert_(hasattr(self.jurisdiction, 'authoritySource'))
        self.assert_(hasattr(self.jurisdiction, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.jurisdiction, 'hasAuthority'))
        self.assert_(hasattr(self.jurisdiction, 'identifier'))
        self.assert_(hasattr(self.jurisdiction, 'label'))
        self.assert_(hasattr(self.jurisdiction, 'relatedTo'))

    def tearDown(self):
        pass

class TestLanguage(unittest.TestCase):
    def setUp(self):
        self.language = Language()


    def test_init(self):
        self.assertEquals(type(self.language), Language)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.language, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.language, 'identifier'))
        self.assert_(hasattr(self.language, 'label'))
        self.assert_(hasattr(self.language, 'languageOfPart'))
        self.assert_(hasattr(self.language, 'languageOfPartUri'))
        self.assert_(hasattr(self.language, 'languageSource'))
        self.assert_(hasattr(self.language, 'relatedTo'))
        self.assert_(hasattr(self.language, 'resourcePart'))

    def tearDown(self):
        pass

class TestManuscript(unittest.TestCase):
    def setUp(self):
        self.manuscript = Manuscript()


    def test_init(self):
        self.assertEquals(type(self.manuscript), Manuscript)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.manuscript, 'abbreviatedTitle'))
        self.assert_(hasattr(self.manuscript, 'ansi'))
        self.assert_(hasattr(self.manuscript, 'arrangement'))
        self.assert_(hasattr(self.manuscript, 'aspectRatio'))
        self.assert_(hasattr(self.manuscript, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.manuscript, 'awardNote'))
        self.assert_(hasattr(self.manuscript, 'carrierCategory'))
        self.assert_(hasattr(self.manuscript, 'coden'))
        self.assert_(hasattr(self.manuscript, 'colorContent'))
        self.assert_(hasattr(self.manuscript, 'contentAccessibility'))
        self.assert_(hasattr(self.manuscript, 'contentsNote'))
        self.assert_(hasattr(self.manuscript, 'custodialHistory'))
        self.assert_(hasattr(self.manuscript, 'dimensions'))
        self.assert_(hasattr(self.manuscript, 'distribution'))
        self.assert_(hasattr(self.manuscript, 'doi'))
        self.assert_(hasattr(self.manuscript, 'duration'))
        self.assert_(hasattr(self.manuscript, 'ean'))
        self.assert_(hasattr(self.manuscript, 'edition'))
        self.assert_(hasattr(self.manuscript, 'editionResponsibility'))
        self.assert_(hasattr(self.manuscript, 'extent'))
        self.assert_(hasattr(self.manuscript, 'fingerprint'))
        self.assert_(hasattr(self.manuscript, 'formatOfMusic'))
        self.assert_(hasattr(self.manuscript, 'frequency'))
        self.assert_(hasattr(self.manuscript, 'frequencyNote'))
        self.assert_(hasattr(self.manuscript, 'graphicScaleNote'))
        self.assert_(hasattr(self.manuscript, 'hasEquivalent'))
        self.assert_(hasattr(self.manuscript, 'hdl'))
        self.assert_(hasattr(self.manuscript, 'identifier'))
        self.assert_(hasattr(self.manuscript, 'illustrationNote'))
        self.assert_(hasattr(self.manuscript, 'instanceOf'))
        self.assert_(hasattr(self.manuscript, 'instanceTitle'))
        self.assert_(hasattr(self.manuscript, 'isbn'))
        self.assert_(hasattr(self.manuscript, 'isbn10'))
        self.assert_(hasattr(self.manuscript, 'isbn13'))
        self.assert_(hasattr(self.manuscript, 'ismn'))
        self.assert_(hasattr(self.manuscript, 'iso'))
        self.assert_(hasattr(self.manuscript, 'isrc'))
        self.assert_(hasattr(self.manuscript, 'issn'))
        self.assert_(hasattr(self.manuscript, 'issueNumber'))
        self.assert_(hasattr(self.manuscript, 'issuedWith'))
        self.assert_(hasattr(self.manuscript, 'keyTitle'))
        self.assert_(hasattr(self.manuscript, 'label'))
        self.assert_(hasattr(self.manuscript, 'lcOverseasAcq'))
        self.assert_(hasattr(self.manuscript, 'lccn'))
        self.assert_(hasattr(self.manuscript, 'legalDeposit'))
        self.assert_(hasattr(self.manuscript, 'local'))
        self.assert_(hasattr(self.manuscript, 'manufacture'))
        self.assert_(hasattr(self.manuscript, 'matrixNumber'))
        self.assert_(hasattr(self.manuscript, 'mediaCategory'))
        self.assert_(hasattr(self.manuscript, 'modeOfIssuance'))
        self.assert_(hasattr(self.manuscript, 'musicPlate'))
        self.assert_(hasattr(self.manuscript, 'musicPublisherNumber'))
        self.assert_(hasattr(self.manuscript, 'nban'))
        self.assert_(hasattr(self.manuscript, 'nbn'))
        self.assert_(hasattr(self.manuscript, 'notation'))
        self.assert_(hasattr(self.manuscript, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.manuscript, 'postalRegistration'))
        self.assert_(hasattr(self.manuscript, 'preferredCitation'))
        self.assert_(hasattr(self.manuscript, 'production'))
        self.assert_(hasattr(self.manuscript, 'provider'))
        self.assert_(hasattr(self.manuscript, 'providerStatement'))
        self.assert_(hasattr(self.manuscript, 'publication'))
        self.assert_(hasattr(self.manuscript, 'publisherNumber'))
        self.assert_(hasattr(self.manuscript, 'relatedInstance'))
        self.assert_(hasattr(self.manuscript, 'relatedTo'))
        self.assert_(hasattr(self.manuscript, 'reportNumber'))
        self.assert_(hasattr(self.manuscript, 'reproduction'))
        self.assert_(hasattr(self.manuscript, 'responsibilityStatement'))
        self.assert_(hasattr(self.manuscript, 'serialFirstIssue'))
        self.assert_(hasattr(self.manuscript, 'serialLastIssue'))
        self.assert_(hasattr(self.manuscript, 'sici'))
        self.assert_(hasattr(self.manuscript, 'soundContent'))
        self.assert_(hasattr(self.manuscript, 'stockNumber'))
        self.assert_(hasattr(self.manuscript, 'strn'))
        self.assert_(hasattr(self.manuscript, 'studyNumber'))
        self.assert_(hasattr(self.manuscript, 'supplementaryContentNote'))
        self.assert_(hasattr(self.manuscript, 'titleStatement'))
        self.assert_(hasattr(self.manuscript, 'upc'))
        self.assert_(hasattr(self.manuscript, 'uri'))
        self.assert_(hasattr(self.manuscript, 'urn'))
        self.assert_(hasattr(self.manuscript, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestMeeting(unittest.TestCase):
    def setUp(self):
        self.meeting = Meeting()


    def test_init(self):
        self.assertEquals(type(self.meeting), Meeting)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.meeting, 'authorityAssigner'))
        self.assert_(hasattr(self.meeting, 'authoritySource'))
        self.assert_(hasattr(self.meeting, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.meeting, 'hasAuthority'))
        self.assert_(hasattr(self.meeting, 'identifier'))
        self.assert_(hasattr(self.meeting, 'label'))
        self.assert_(hasattr(self.meeting, 'relatedTo'))


    def tearDown(self):
        pass


class TestMixedMaterial(unittest.TestCase):

    def setUp(self):
        self.mixedmaterial = MixedMaterial()

    def test_init(self):
        self.assertEquals(type(self.mixedmaterial), MixedMaterial)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.mixedmaterial, 'absorbed'))
        self.assert_(hasattr(self.mixedmaterial, 'absorbedBy'))
        self.assert_(hasattr(self.mixedmaterial, 'absorbedInPart'))
        self.assert_(hasattr(self.mixedmaterial, 'absorbedInPartBy'))
        self.assert_(hasattr(self.mixedmaterial, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.mixedmaterial, 'classification'))
        self.assert_(hasattr(self.mixedmaterial, 'classificationDdc'))
        self.assert_(hasattr(self.mixedmaterial, 'classificationLcc'))
        self.assert_(hasattr(self.mixedmaterial, 'classificationNlm'))
        self.assert_(hasattr(self.mixedmaterial, 'classificationUdc'))
        self.assert_(hasattr(self.mixedmaterial, 'containedIn'))
        self.assert_(hasattr(self.mixedmaterial, 'contains'))
        self.assert_(hasattr(self.mixedmaterial, 'contentCategory'))
        self.assert_(hasattr(self.mixedmaterial, 'continuedBy'))
        self.assert_(hasattr(self.mixedmaterial, 'continuedInPartBy'))
        self.assert_(hasattr(self.mixedmaterial, 'continues'))
        self.assert_(hasattr(self.mixedmaterial, 'continuesInPart'))
        self.assert_(hasattr(self.mixedmaterial, 'dataSource'))
        self.assert_(hasattr(self.mixedmaterial, 'dissertationDegree'))
        self.assert_(hasattr(self.mixedmaterial, 'dissertationIdentifier'))
        self.assert_(hasattr(self.mixedmaterial, 'dissertationInstitution'))
        self.assert_(hasattr(self.mixedmaterial, 'dissertationNote'))
        self.assert_(hasattr(self.mixedmaterial, 'dissertationYear'))
        self.assert_(hasattr(self.mixedmaterial, 'event'))
        self.assert_(hasattr(self.mixedmaterial, 'expressionOf'))
        self.assert_(hasattr(self.mixedmaterial, 'findingAid'))
        self.assert_(hasattr(self.mixedmaterial, 'geographicCoverageNote'))
        self.assert_(hasattr(self.mixedmaterial, 'hasDerivative'))
        self.assert_(hasattr(self.mixedmaterial, 'hasExpression'))
        self.assert_(hasattr(self.mixedmaterial, 'hasInstance'))
        self.assert_(hasattr(self.mixedmaterial, 'identifier'))
        self.assert_(hasattr(self.mixedmaterial, 'index'))
        self.assert_(hasattr(self.mixedmaterial, 'isDerivativeOf'))
        self.assert_(hasattr(self.mixedmaterial, 'isan'))
        self.assert_(hasattr(self.mixedmaterial, 'issnL'))
        self.assert_(hasattr(self.mixedmaterial, 'istc'))
        self.assert_(hasattr(self.mixedmaterial, 'iswc'))
        self.assert_(hasattr(self.mixedmaterial, 'label'))
        self.assert_(hasattr(self.mixedmaterial, 'languageNote'))
        self.assert_(hasattr(self.mixedmaterial, 'mergedToForm'))
        self.assert_(hasattr(self.mixedmaterial, 'originDate'))
        self.assert_(hasattr(self.mixedmaterial, 'originPlace'))
        self.assert_(hasattr(self.mixedmaterial, 'originalVersion'))
        self.assert_(hasattr(self.mixedmaterial, 'otherEdition'))
        self.assert_(hasattr(self.mixedmaterial, 'precedes'))
        self.assert_(hasattr(self.mixedmaterial, 'relatedTo'))
        self.assert_(hasattr(self.mixedmaterial, 'relatedWork'))
        self.assert_(hasattr(self.mixedmaterial, 'separatedFrom'))
        self.assert_(hasattr(self.mixedmaterial, 'series'))
        self.assert_(hasattr(self.mixedmaterial, 'splitInto'))
        self.assert_(hasattr(self.mixedmaterial, 'subject'))
        self.assert_(hasattr(self.mixedmaterial, 'subseries'))
        self.assert_(hasattr(self.mixedmaterial, 'subseriesOf'))
        self.assert_(hasattr(self.mixedmaterial, 'succeeds'))
        self.assert_(hasattr(self.mixedmaterial, 'supersededBy'))
        self.assert_(hasattr(self.mixedmaterial, 'supersededInPartBy'))
        self.assert_(hasattr(self.mixedmaterial, 'supersedes'))
        self.assert_(hasattr(self.mixedmaterial, 'supersedesInPart'))
        self.assert_(hasattr(self.mixedmaterial, 'supplement'))
        self.assert_(hasattr(self.mixedmaterial, 'supplementTo'))
        self.assert_(hasattr(self.mixedmaterial, 'temporalCoverageNote'))
        self.assert_(hasattr(self.mixedmaterial, 'translation'))
        self.assert_(hasattr(self.mixedmaterial, 'translationOf'))
        self.assert_(hasattr(self.mixedmaterial, 'unionOf'))
        self.assert_(hasattr(self.mixedmaterial, 'workTitle'))

    def tearDown(self):
        pass

class TestMonograph(unittest.TestCase):
    def setUp(self):
        self.monograph = Monograph()


    def test_init(self):
        self.assertEquals(type(self.monograph), Monograph)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.monograph, 'abbreviatedTitle'))
        self.assert_(hasattr(self.monograph, 'ansi'))
        self.assert_(hasattr(self.monograph, 'arrangement'))
        self.assert_(hasattr(self.monograph, 'aspectRatio'))
        self.assert_(hasattr(self.monograph, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.monograph, 'awardNote'))
        self.assert_(hasattr(self.monograph, 'carrierCategory'))
        self.assert_(hasattr(self.monograph, 'coden'))
        self.assert_(hasattr(self.monograph, 'colorContent'))
        self.assert_(hasattr(self.monograph, 'contentAccessibility'))
        self.assert_(hasattr(self.monograph, 'contentsNote'))
        self.assert_(hasattr(self.monograph, 'custodialHistory'))
        self.assert_(hasattr(self.monograph, 'dimensions'))
        self.assert_(hasattr(self.monograph, 'distribution'))
        self.assert_(hasattr(self.monograph, 'doi'))
        self.assert_(hasattr(self.monograph, 'duration'))
        self.assert_(hasattr(self.monograph, 'ean'))
        self.assert_(hasattr(self.monograph, 'edition'))
        self.assert_(hasattr(self.monograph, 'editionResponsibility'))
        self.assert_(hasattr(self.monograph, 'extent'))
        self.assert_(hasattr(self.monograph, 'fingerprint'))
        self.assert_(hasattr(self.monograph, 'formatOfMusic'))
        self.assert_(hasattr(self.monograph, 'frequency'))
        self.assert_(hasattr(self.monograph, 'frequencyNote'))
        self.assert_(hasattr(self.monograph, 'graphicScaleNote'))
        self.assert_(hasattr(self.monograph, 'hasEquivalent'))
        self.assert_(hasattr(self.monograph, 'hdl'))
        self.assert_(hasattr(self.monograph, 'identifier'))
        self.assert_(hasattr(self.monograph, 'illustrationNote'))
        self.assert_(hasattr(self.monograph, 'instanceOf'))
        self.assert_(hasattr(self.monograph, 'instanceTitle'))
        self.assert_(hasattr(self.monograph, 'isbn'))
        self.assert_(hasattr(self.monograph, 'isbn10'))
        self.assert_(hasattr(self.monograph, 'isbn13'))
        self.assert_(hasattr(self.monograph, 'ismn'))
        self.assert_(hasattr(self.monograph, 'iso'))
        self.assert_(hasattr(self.monograph, 'isrc'))
        self.assert_(hasattr(self.monograph, 'issn'))
        self.assert_(hasattr(self.monograph, 'issueNumber'))
        self.assert_(hasattr(self.monograph, 'issuedWith'))
        self.assert_(hasattr(self.monograph, 'keyTitle'))
        self.assert_(hasattr(self.monograph, 'label'))
        self.assert_(hasattr(self.monograph, 'lcOverseasAcq'))
        self.assert_(hasattr(self.monograph, 'lccn'))
        self.assert_(hasattr(self.monograph, 'legalDeposit'))
        self.assert_(hasattr(self.monograph, 'local'))
        self.assert_(hasattr(self.monograph, 'manufacture'))
        self.assert_(hasattr(self.monograph, 'matrixNumber'))
        self.assert_(hasattr(self.monograph, 'mediaCategory'))
        self.assert_(hasattr(self.monograph, 'modeOfIssuance'))
        self.assert_(hasattr(self.monograph, 'musicPlate'))
        self.assert_(hasattr(self.monograph, 'musicPublisherNumber'))
        self.assert_(hasattr(self.monograph, 'nban'))
        self.assert_(hasattr(self.monograph, 'nbn'))
        self.assert_(hasattr(self.monograph, 'notation'))
        self.assert_(hasattr(self.monograph, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.monograph, 'postalRegistration'))
        self.assert_(hasattr(self.monograph, 'preferredCitation'))
        self.assert_(hasattr(self.monograph, 'production'))
        self.assert_(hasattr(self.monograph, 'provider'))
        self.assert_(hasattr(self.monograph, 'providerStatement'))
        self.assert_(hasattr(self.monograph, 'publication'))
        self.assert_(hasattr(self.monograph, 'publisherNumber'))
        self.assert_(hasattr(self.monograph, 'relatedInstance'))
        self.assert_(hasattr(self.monograph, 'relatedTo'))
        self.assert_(hasattr(self.monograph, 'reportNumber'))
        self.assert_(hasattr(self.monograph, 'reproduction'))
        self.assert_(hasattr(self.monograph, 'responsibilityStatement'))
        self.assert_(hasattr(self.monograph, 'serialFirstIssue'))
        self.assert_(hasattr(self.monograph, 'serialLastIssue'))
        self.assert_(hasattr(self.monograph, 'sici'))
        self.assert_(hasattr(self.monograph, 'soundContent'))
        self.assert_(hasattr(self.monograph, 'stockNumber'))
        self.assert_(hasattr(self.monograph, 'strn'))
        self.assert_(hasattr(self.monograph, 'studyNumber'))
        self.assert_(hasattr(self.monograph, 'supplementaryContentNote'))
        self.assert_(hasattr(self.monograph, 'titleStatement'))
        self.assert_(hasattr(self.monograph, 'upc'))
        self.assert_(hasattr(self.monograph, 'uri'))
        self.assert_(hasattr(self.monograph, 'urn'))
        self.assert_(hasattr(self.monograph, 'videorecordingNumber'))


    def tearDown(self):
        pass

class TestMovingImage(unittest.TestCase):

    def setUp(self):
        self.movingimage = MovingImage()


    def test_init(self):
        self.assertEquals(type(self.movingimage), MovingImage)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.movingimage, 'absorbed'))
        self.assert_(hasattr(self.movingimage, 'absorbedBy'))
        self.assert_(hasattr(self.movingimage, 'absorbedInPart'))
        self.assert_(hasattr(self.movingimage, 'absorbedInPartBy'))
        self.assert_(hasattr(self.movingimage, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.movingimage, 'classification'))
        self.assert_(hasattr(self.movingimage, 'classificationDdc'))
        self.assert_(hasattr(self.movingimage, 'classificationLcc'))
        self.assert_(hasattr(self.movingimage, 'classificationNlm'))
        self.assert_(hasattr(self.movingimage, 'classificationUdc'))
        self.assert_(hasattr(self.movingimage, 'containedIn'))
        self.assert_(hasattr(self.movingimage, 'contains'))
        self.assert_(hasattr(self.movingimage, 'contentCategory'))
        self.assert_(hasattr(self.movingimage, 'continuedBy'))
        self.assert_(hasattr(self.movingimage, 'continuedInPartBy'))
        self.assert_(hasattr(self.movingimage, 'continues'))
        self.assert_(hasattr(self.movingimage, 'continuesInPart'))
        self.assert_(hasattr(self.movingimage, 'dataSource'))
        self.assert_(hasattr(self.movingimage, 'dissertationDegree'))
        self.assert_(hasattr(self.movingimage, 'dissertationIdentifier'))
        self.assert_(hasattr(self.movingimage, 'dissertationInstitution'))
        self.assert_(hasattr(self.movingimage, 'dissertationNote'))
        self.assert_(hasattr(self.movingimage, 'dissertationYear'))
        self.assert_(hasattr(self.movingimage, 'event'))
        self.assert_(hasattr(self.movingimage, 'expressionOf'))
        self.assert_(hasattr(self.movingimage, 'findingAid'))
        self.assert_(hasattr(self.movingimage, 'geographicCoverageNote'))
        self.assert_(hasattr(self.movingimage, 'hasDerivative'))
        self.assert_(hasattr(self.movingimage, 'hasExpression'))
        self.assert_(hasattr(self.movingimage, 'hasInstance'))
        self.assert_(hasattr(self.movingimage, 'identifier'))
        self.assert_(hasattr(self.movingimage, 'index'))
        self.assert_(hasattr(self.movingimage, 'isDerivativeOf'))
        self.assert_(hasattr(self.movingimage, 'isan'))
        self.assert_(hasattr(self.movingimage, 'issnL'))
        self.assert_(hasattr(self.movingimage, 'istc'))
        self.assert_(hasattr(self.movingimage, 'iswc'))
        self.assert_(hasattr(self.movingimage, 'label'))
        self.assert_(hasattr(self.movingimage, 'languageNote'))
        self.assert_(hasattr(self.movingimage, 'mergedToForm'))
        self.assert_(hasattr(self.movingimage, 'originDate'))
        self.assert_(hasattr(self.movingimage, 'originPlace'))
        self.assert_(hasattr(self.movingimage, 'originalVersion'))
        self.assert_(hasattr(self.movingimage, 'otherEdition'))
        self.assert_(hasattr(self.movingimage, 'precedes'))
        self.assert_(hasattr(self.movingimage, 'relatedTo'))
        self.assert_(hasattr(self.movingimage, 'relatedWork'))
        self.assert_(hasattr(self.movingimage, 'separatedFrom'))
        self.assert_(hasattr(self.movingimage, 'series'))
        self.assert_(hasattr(self.movingimage, 'splitInto'))
        self.assert_(hasattr(self.movingimage, 'subject'))
        self.assert_(hasattr(self.movingimage, 'subseries'))
        self.assert_(hasattr(self.movingimage, 'subseriesOf'))
        self.assert_(hasattr(self.movingimage, 'succeeds'))
        self.assert_(hasattr(self.movingimage, 'supersededBy'))
        self.assert_(hasattr(self.movingimage, 'supersededInPartBy'))
        self.assert_(hasattr(self.movingimage, 'supersedes'))
        self.assert_(hasattr(self.movingimage, 'supersedesInPart'))
        self.assert_(hasattr(self.movingimage, 'supplement'))
        self.assert_(hasattr(self.movingimage, 'supplementTo'))
        self.assert_(hasattr(self.movingimage, 'temporalCoverageNote'))
        self.assert_(hasattr(self.movingimage, 'translation'))
        self.assert_(hasattr(self.movingimage, 'translationOf'))
        self.assert_(hasattr(self.movingimage, 'unionOf'))
        self.assert_(hasattr(self.movingimage, 'workTitle'))

    def tearDown(self):
        pass


class TestMultimedia(unittest.TestCase):

    def setUp(self):
        self.multimedia = Multimedia()

    def test_init(self):
        self.assertEquals(type(self.multimedia), Multimedia)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.multimedia, 'absorbed'))
        self.assert_(hasattr(self.multimedia, 'absorbedBy'))
        self.assert_(hasattr(self.multimedia, 'absorbedInPart'))
        self.assert_(hasattr(self.multimedia, 'absorbedInPartBy'))
        self.assert_(hasattr(self.multimedia, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.multimedia, 'classification'))
        self.assert_(hasattr(self.multimedia, 'classificationDdc'))
        self.assert_(hasattr(self.multimedia, 'classificationLcc'))
        self.assert_(hasattr(self.multimedia, 'classificationNlm'))
        self.assert_(hasattr(self.multimedia, 'classificationUdc'))
        self.assert_(hasattr(self.multimedia, 'containedIn'))
        self.assert_(hasattr(self.multimedia, 'contains'))
        self.assert_(hasattr(self.multimedia, 'contentCategory'))
        self.assert_(hasattr(self.multimedia, 'continuedBy'))
        self.assert_(hasattr(self.multimedia, 'continuedInPartBy'))
        self.assert_(hasattr(self.multimedia, 'continues'))
        self.assert_(hasattr(self.multimedia, 'continuesInPart'))
        self.assert_(hasattr(self.multimedia, 'dataSource'))
        self.assert_(hasattr(self.multimedia, 'dissertationDegree'))
        self.assert_(hasattr(self.multimedia, 'dissertationIdentifier'))
        self.assert_(hasattr(self.multimedia, 'dissertationInstitution'))
        self.assert_(hasattr(self.multimedia, 'dissertationNote'))
        self.assert_(hasattr(self.multimedia, 'dissertationYear'))
        self.assert_(hasattr(self.multimedia, 'event'))
        self.assert_(hasattr(self.multimedia, 'expressionOf'))
        self.assert_(hasattr(self.multimedia, 'findingAid'))
        self.assert_(hasattr(self.multimedia, 'geographicCoverageNote'))
        self.assert_(hasattr(self.multimedia, 'hasDerivative'))
        self.assert_(hasattr(self.multimedia, 'hasExpression'))
        self.assert_(hasattr(self.multimedia, 'hasInstance'))
        self.assert_(hasattr(self.multimedia, 'identifier'))
        self.assert_(hasattr(self.multimedia, 'index'))
        self.assert_(hasattr(self.multimedia, 'isDerivativeOf'))
        self.assert_(hasattr(self.multimedia, 'isan'))
        self.assert_(hasattr(self.multimedia, 'issnL'))
        self.assert_(hasattr(self.multimedia, 'istc'))
        self.assert_(hasattr(self.multimedia, 'iswc'))
        self.assert_(hasattr(self.multimedia, 'label'))
        self.assert_(hasattr(self.multimedia, 'languageNote'))
        self.assert_(hasattr(self.multimedia, 'mergedToForm'))
        self.assert_(hasattr(self.multimedia, 'originDate'))
        self.assert_(hasattr(self.multimedia, 'originPlace'))
        self.assert_(hasattr(self.multimedia, 'originalVersion'))
        self.assert_(hasattr(self.multimedia, 'otherEdition'))
        self.assert_(hasattr(self.multimedia, 'precedes'))
        self.assert_(hasattr(self.multimedia, 'relatedTo'))
        self.assert_(hasattr(self.multimedia, 'relatedWork'))
        self.assert_(hasattr(self.multimedia, 'separatedFrom'))
        self.assert_(hasattr(self.multimedia, 'series'))
        self.assert_(hasattr(self.multimedia, 'splitInto'))
        self.assert_(hasattr(self.multimedia, 'subject'))
        self.assert_(hasattr(self.multimedia, 'subseries'))
        self.assert_(hasattr(self.multimedia, 'subseriesOf'))
        self.assert_(hasattr(self.multimedia, 'succeeds'))
        self.assert_(hasattr(self.multimedia, 'supersededBy'))
        self.assert_(hasattr(self.multimedia, 'supersededInPartBy'))
        self.assert_(hasattr(self.multimedia, 'supersedes'))
        self.assert_(hasattr(self.multimedia, 'supersedesInPart'))
        self.assert_(hasattr(self.multimedia, 'supplement'))
        self.assert_(hasattr(self.multimedia, 'supplementTo'))
        self.assert_(hasattr(self.multimedia, 'temporalCoverageNote'))
        self.assert_(hasattr(self.multimedia, 'translation'))
        self.assert_(hasattr(self.multimedia, 'translationOf'))
        self.assert_(hasattr(self.multimedia, 'unionOf'))
        self.assert_(hasattr(self.multimedia, 'workTitle'))

    def tearDown(self):
        pass

class TestMultipartMonograph(unittest.TestCase):
    def setUp(self):
        self.multipartmonograph = MultipartMonograph()


    def test_init(self):
        self.assertEquals(type(self.multipartmonograph), MultipartMonograph)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.multipartmonograph, 'abbreviatedTitle'))
        self.assert_(hasattr(self.multipartmonograph, 'ansi'))
        self.assert_(hasattr(self.multipartmonograph, 'arrangement'))
        self.assert_(hasattr(self.multipartmonograph, 'aspectRatio'))
        self.assert_(hasattr(self.multipartmonograph, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.multipartmonograph, 'awardNote'))
        self.assert_(hasattr(self.multipartmonograph, 'carrierCategory'))
        self.assert_(hasattr(self.multipartmonograph, 'coden'))
        self.assert_(hasattr(self.multipartmonograph, 'colorContent'))
        self.assert_(hasattr(self.multipartmonograph, 'contentAccessibility'))
        self.assert_(hasattr(self.multipartmonograph, 'contentsNote'))
        self.assert_(hasattr(self.multipartmonograph, 'custodialHistory'))
        self.assert_(hasattr(self.multipartmonograph, 'dimensions'))
        self.assert_(hasattr(self.multipartmonograph, 'distribution'))
        self.assert_(hasattr(self.multipartmonograph, 'doi'))
        self.assert_(hasattr(self.multipartmonograph, 'duration'))
        self.assert_(hasattr(self.multipartmonograph, 'ean'))
        self.assert_(hasattr(self.multipartmonograph, 'edition'))
        self.assert_(hasattr(self.multipartmonograph, 'editionResponsibility'))
        self.assert_(hasattr(self.multipartmonograph, 'extent'))
        self.assert_(hasattr(self.multipartmonograph, 'fingerprint'))
        self.assert_(hasattr(self.multipartmonograph, 'formatOfMusic'))
        self.assert_(hasattr(self.multipartmonograph, 'frequency'))
        self.assert_(hasattr(self.multipartmonograph, 'frequencyNote'))
        self.assert_(hasattr(self.multipartmonograph, 'graphicScaleNote'))
        self.assert_(hasattr(self.multipartmonograph, 'hasEquivalent'))
        self.assert_(hasattr(self.multipartmonograph, 'hdl'))
        self.assert_(hasattr(self.multipartmonograph, 'identifier'))
        self.assert_(hasattr(self.multipartmonograph, 'illustrationNote'))
        self.assert_(hasattr(self.multipartmonograph, 'instanceOf'))
        self.assert_(hasattr(self.multipartmonograph, 'instanceTitle'))
        self.assert_(hasattr(self.multipartmonograph, 'isbn'))
        self.assert_(hasattr(self.multipartmonograph, 'isbn10'))
        self.assert_(hasattr(self.multipartmonograph, 'isbn13'))
        self.assert_(hasattr(self.multipartmonograph, 'ismn'))
        self.assert_(hasattr(self.multipartmonograph, 'iso'))
        self.assert_(hasattr(self.multipartmonograph, 'isrc'))
        self.assert_(hasattr(self.multipartmonograph, 'issn'))
        self.assert_(hasattr(self.multipartmonograph, 'issueNumber'))
        self.assert_(hasattr(self.multipartmonograph, 'issuedWith'))
        self.assert_(hasattr(self.multipartmonograph, 'keyTitle'))
        self.assert_(hasattr(self.multipartmonograph, 'label'))
        self.assert_(hasattr(self.multipartmonograph, 'lcOverseasAcq'))
        self.assert_(hasattr(self.multipartmonograph, 'lccn'))
        self.assert_(hasattr(self.multipartmonograph, 'legalDeposit'))
        self.assert_(hasattr(self.multipartmonograph, 'local'))
        self.assert_(hasattr(self.multipartmonograph, 'manufacture'))
        self.assert_(hasattr(self.multipartmonograph, 'matrixNumber'))
        self.assert_(hasattr(self.multipartmonograph, 'mediaCategory'))
        self.assert_(hasattr(self.multipartmonograph, 'modeOfIssuance'))
        self.assert_(hasattr(self.multipartmonograph, 'musicPlate'))
        self.assert_(hasattr(self.multipartmonograph, 'musicPublisherNumber'))
        self.assert_(hasattr(self.multipartmonograph, 'nban'))
        self.assert_(hasattr(self.multipartmonograph, 'nbn'))
        self.assert_(hasattr(self.multipartmonograph, 'notation'))
        self.assert_(hasattr(self.multipartmonograph, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.multipartmonograph, 'postalRegistration'))
        self.assert_(hasattr(self.multipartmonograph, 'preferredCitation'))
        self.assert_(hasattr(self.multipartmonograph, 'production'))
        self.assert_(hasattr(self.multipartmonograph, 'provider'))
        self.assert_(hasattr(self.multipartmonograph, 'providerStatement'))
        self.assert_(hasattr(self.multipartmonograph, 'publication'))
        self.assert_(hasattr(self.multipartmonograph, 'publisherNumber'))
        self.assert_(hasattr(self.multipartmonograph, 'relatedInstance'))
        self.assert_(hasattr(self.multipartmonograph, 'relatedTo'))
        self.assert_(hasattr(self.multipartmonograph, 'reportNumber'))
        self.assert_(hasattr(self.multipartmonograph, 'reproduction'))
        self.assert_(hasattr(self.multipartmonograph, 'responsibilityStatement'))
        self.assert_(hasattr(self.multipartmonograph, 'serialFirstIssue'))
        self.assert_(hasattr(self.multipartmonograph, 'serialLastIssue'))
        self.assert_(hasattr(self.multipartmonograph, 'sici'))
        self.assert_(hasattr(self.multipartmonograph, 'soundContent'))
        self.assert_(hasattr(self.multipartmonograph, 'stockNumber'))
        self.assert_(hasattr(self.multipartmonograph, 'strn'))
        self.assert_(hasattr(self.multipartmonograph, 'studyNumber'))
        self.assert_(hasattr(self.multipartmonograph, 'supplementaryContentNote'))
        self.assert_(hasattr(self.multipartmonograph, 'titleStatement'))
        self.assert_(hasattr(self.multipartmonograph, 'upc'))
        self.assert_(hasattr(self.multipartmonograph, 'uri'))
        self.assert_(hasattr(self.multipartmonograph, 'urn'))
        self.assert_(hasattr(self.multipartmonograph, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestOrganization(unittest.TestCase):

    def setUp(self):
        self.organization = Organization()

    def test_init(self):
        self.assertEquals(type(self.organization), Organization)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.organization, 'authorityAssigner'))
        self.assert_(hasattr(self.organization, 'authoritySource'))
        self.assert_(hasattr(self.organization, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.organization, 'hasAuthority'))
        self.assert_(hasattr(self.organization, 'identifier'))
        self.assert_(hasattr(self.organization, 'label'))
        self.assert_(hasattr(self.organization, 'relatedTo'))

    def tearDown(self):
        pass

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person()


    def test_init(self):
        self.assertEquals(type(self.person), Person)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.person, 'authorityAssigner'))
        self.assert_(hasattr(self.person, 'authoritySource'))
        self.assert_(hasattr(self.person, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.person, 'hasAuthority'))
        self.assert_(hasattr(self.person, 'identifier'))
        self.assert_(hasattr(self.person, 'label'))
        self.assert_(hasattr(self.person, 'relatedTo'))


    def tearDown(self):
        pass

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()


    def test_init(self):
        self.assertEquals(type(self.place), Place)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.place, 'authorityAssigner'))
        self.assert_(hasattr(self.place, 'authoritySource'))
        self.assert_(hasattr(self.place, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.place, 'hasAuthority'))
        self.assert_(hasattr(self.place, 'identifier'))
        self.assert_(hasattr(self.place, 'label'))
        self.assert_(hasattr(self.place, 'relatedTo'))


    def tearDown(self):
        pass

class TestPrint(unittest.TestCase):
    def setUp(self):
        self.print_ = Print()


    def test_init(self):
        self.assertEquals(type(self.print_), Print)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.print_, 'abbreviatedTitle'))
        self.assert_(hasattr(self.print_, 'ansi'))
        self.assert_(hasattr(self.print_, 'arrangement'))
        self.assert_(hasattr(self.print_, 'aspectRatio'))
        self.assert_(hasattr(self.print_, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.print_, 'awardNote'))
        self.assert_(hasattr(self.print_, 'carrierCategory'))
        self.assert_(hasattr(self.print_, 'coden'))
        self.assert_(hasattr(self.print_, 'colorContent'))
        self.assert_(hasattr(self.print_, 'contentAccessibility'))
        self.assert_(hasattr(self.print_, 'contentsNote'))
        self.assert_(hasattr(self.print_, 'custodialHistory'))
        self.assert_(hasattr(self.print_, 'dimensions'))
        self.assert_(hasattr(self.print_, 'distribution'))
        self.assert_(hasattr(self.print_, 'doi'))
        self.assert_(hasattr(self.print_, 'duration'))
        self.assert_(hasattr(self.print_, 'ean'))
        self.assert_(hasattr(self.print_, 'edition'))
        self.assert_(hasattr(self.print_, 'editionResponsibility'))
        self.assert_(hasattr(self.print_, 'extent'))
        self.assert_(hasattr(self.print_, 'fingerprint'))
        self.assert_(hasattr(self.print_, 'formatOfMusic'))
        self.assert_(hasattr(self.print_, 'frequency'))
        self.assert_(hasattr(self.print_, 'frequencyNote'))
        self.assert_(hasattr(self.print_, 'graphicScaleNote'))
        self.assert_(hasattr(self.print_, 'hasEquivalent'))
        self.assert_(hasattr(self.print_, 'hdl'))
        self.assert_(hasattr(self.print_, 'identifier'))
        self.assert_(hasattr(self.print_, 'illustrationNote'))
        self.assert_(hasattr(self.print_, 'instanceOf'))
        self.assert_(hasattr(self.print_, 'instanceTitle'))
        self.assert_(hasattr(self.print_, 'isbn'))
        self.assert_(hasattr(self.print_, 'isbn10'))
        self.assert_(hasattr(self.print_, 'isbn13'))
        self.assert_(hasattr(self.print_, 'ismn'))
        self.assert_(hasattr(self.print_, 'iso'))
        self.assert_(hasattr(self.print_, 'isrc'))
        self.assert_(hasattr(self.print_, 'issn'))
        self.assert_(hasattr(self.print_, 'issueNumber'))
        self.assert_(hasattr(self.print_, 'issuedWith'))
        self.assert_(hasattr(self.print_, 'keyTitle'))
        self.assert_(hasattr(self.print_, 'label'))
        self.assert_(hasattr(self.print_, 'lcOverseasAcq'))
        self.assert_(hasattr(self.print_, 'lccn'))
        self.assert_(hasattr(self.print_, 'legalDeposit'))
        self.assert_(hasattr(self.print_, 'local'))
        self.assert_(hasattr(self.print_, 'manufacture'))
        self.assert_(hasattr(self.print_, 'matrixNumber'))
        self.assert_(hasattr(self.print_, 'mediaCategory'))
        self.assert_(hasattr(self.print_, 'modeOfIssuance'))
        self.assert_(hasattr(self.print_, 'musicPlate'))
        self.assert_(hasattr(self.print_, 'musicPublisherNumber'))
        self.assert_(hasattr(self.print_, 'nban'))
        self.assert_(hasattr(self.print_, 'nbn'))
        self.assert_(hasattr(self.print_, 'notation'))
        self.assert_(hasattr(self.print_, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.print_, 'postalRegistration'))
        self.assert_(hasattr(self.print_, 'preferredCitation'))
        self.assert_(hasattr(self.print_, 'production'))
        self.assert_(hasattr(self.print_, 'provider'))
        self.assert_(hasattr(self.print_, 'providerStatement'))
        self.assert_(hasattr(self.print_, 'publication'))
        self.assert_(hasattr(self.print_, 'publisherNumber'))
        self.assert_(hasattr(self.print_, 'relatedInstance'))
        self.assert_(hasattr(self.print_, 'relatedTo'))
        self.assert_(hasattr(self.print_, 'reportNumber'))
        self.assert_(hasattr(self.print_, 'reproduction'))
        self.assert_(hasattr(self.print_, 'responsibilityStatement'))
        self.assert_(hasattr(self.print_, 'serialFirstIssue'))
        self.assert_(hasattr(self.print_, 'serialLastIssue'))
        self.assert_(hasattr(self.print_, 'sici'))
        self.assert_(hasattr(self.print_, 'soundContent'))
        self.assert_(hasattr(self.print_, 'stockNumber'))
        self.assert_(hasattr(self.print_, 'strn'))
        self.assert_(hasattr(self.print_, 'studyNumber'))
        self.assert_(hasattr(self.print_, 'supplementaryContentNote'))
        self.assert_(hasattr(self.print_, 'titleStatement'))
        self.assert_(hasattr(self.print_, 'upc'))
        self.assert_(hasattr(self.print_, 'uri'))
        self.assert_(hasattr(self.print_, 'urn'))
        self.assert_(hasattr(self.print_, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestProvider(unittest.TestCase):

    def setUp(self):
        self.provider = Provider()


    def test_init(self):
        self.assertEquals(type(self.provider), Provider)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.provider, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.provider, 'copyrightDate'))
        self.assert_(hasattr(self.provider, 'identifier'))
        self.assert_(hasattr(self.provider, 'label'))
        self.assert_(hasattr(self.provider, 'providerDate'))
        self.assert_(hasattr(self.provider, 'providerName'))
        self.assert_(hasattr(self.provider, 'providerPlace'))
        self.assert_(hasattr(self.provider, 'providerRole'))
        self.assert_(hasattr(self.provider, 'relatedTo'))


    def tearDown(self):
        pass

class TestRelated(unittest.TestCase):

    def setUp(self):
        self.related = Related()


    def test_init(self):
        self.assertEquals(type(self.related), Related)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.related, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.related, 'identifier'))
        self.assert_(hasattr(self.related, 'label'))
        self.assert_(hasattr(self.related, 'relatedTo'))
        self.assert_(hasattr(self.related, 'relationship'))
        self.assert_(hasattr(self.related, 'relationshipUri'))


    def tearDown(self):
        pass


##def test_frame(bf_class):
##    print_("""class Test{}(unittest.TestCase):""".format(bf_class))
##    print_("""    def setUp(self):
##        self.{} = {}()""".format(bf_class.lower(), bf_class))
##    print_("\n")
##    print_("""    def test_init(self):
##        self.assertEquals(type(self.{}), {})""".format(bf_class.lower(), bf_class))
##    print_("\n")
##    print_("""    def test_rdf_properties(self):""")
##    for row in dir(getattr(models, bf_class)):
##        if type(row) == unicode:
##            print_("""        self.assert_(hasattr(self.{}, '{}'))""".format(bf_class.lower(), row))
##    print_("\n")
##    print_("""    def tearDown(self):
##        pass""")

class TestResource(unittest.TestCase):

    def setUp(self):
        self.resource = Resource()

    def test_init(self):
        self.assertEquals(type(self.resource), Resource)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.resource, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.resource, 'identifier'))
        self.assert_(hasattr(self.resource, 'label'))
        self.assert_(hasattr(self.resource, 'relatedTo'))

    def tearDown(self):
        pass

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()


    def test_init(self):
        self.assertEquals(type(self.review), Review)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.review, 'annotates'))
        self.assert_(hasattr(self.review, 'annotationAssertedBy'))
        self.assert_(hasattr(self.review, 'annotationBody'))
        self.assert_(hasattr(self.review, 'annotationSource'))
        self.assert_(hasattr(self.review, 'assertionDate'))
        self.assert_(hasattr(self.review, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.review, 'identifier'))
        self.assert_(hasattr(self.review, 'label'))
        self.assert_(hasattr(self.review, 'relatedTo'))
        self.assert_(hasattr(self.review, 'review'))
        self.assert_(hasattr(self.review, 'reviewOf'))
        self.assert_(hasattr(self.review, 'startOfReview'))


    def tearDown(self):
        pass

class TestSerial(unittest.TestCase):

    def setUp(self):
        self.serial = Serial()

    def test_init(self):
        self.assertEquals(type(self.serial), Serial)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.serial, 'abbreviatedTitle'))
        self.assert_(hasattr(self.serial, 'ansi'))
        self.assert_(hasattr(self.serial, 'arrangement'))
        self.assert_(hasattr(self.serial, 'aspectRatio'))
        self.assert_(hasattr(self.serial, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.serial, 'awardNote'))
        self.assert_(hasattr(self.serial, 'carrierCategory'))
        self.assert_(hasattr(self.serial, 'coden'))
        self.assert_(hasattr(self.serial, 'colorContent'))
        self.assert_(hasattr(self.serial, 'contentAccessibility'))
        self.assert_(hasattr(self.serial, 'contentsNote'))
        self.assert_(hasattr(self.serial, 'custodialHistory'))
        self.assert_(hasattr(self.serial, 'dimensions'))
        self.assert_(hasattr(self.serial, 'distribution'))
        self.assert_(hasattr(self.serial, 'doi'))
        self.assert_(hasattr(self.serial, 'duration'))
        self.assert_(hasattr(self.serial, 'ean'))
        self.assert_(hasattr(self.serial, 'edition'))
        self.assert_(hasattr(self.serial, 'editionResponsibility'))
        self.assert_(hasattr(self.serial, 'extent'))
        self.assert_(hasattr(self.serial, 'fingerprint'))
        self.assert_(hasattr(self.serial, 'formatOfMusic'))
        self.assert_(hasattr(self.serial, 'frequency'))
        self.assert_(hasattr(self.serial, 'frequencyNote'))
        self.assert_(hasattr(self.serial, 'graphicScaleNote'))
        self.assert_(hasattr(self.serial, 'hasEquivalent'))
        self.assert_(hasattr(self.serial, 'hdl'))
        self.assert_(hasattr(self.serial, 'identifier'))
        self.assert_(hasattr(self.serial, 'illustrationNote'))
        self.assert_(hasattr(self.serial, 'instanceOf'))
        self.assert_(hasattr(self.serial, 'instanceTitle'))
        self.assert_(hasattr(self.serial, 'isbn'))
        self.assert_(hasattr(self.serial, 'isbn10'))
        self.assert_(hasattr(self.serial, 'isbn13'))
        self.assert_(hasattr(self.serial, 'ismn'))
        self.assert_(hasattr(self.serial, 'iso'))
        self.assert_(hasattr(self.serial, 'isrc'))
        self.assert_(hasattr(self.serial, 'issn'))
        self.assert_(hasattr(self.serial, 'issueNumber'))
        self.assert_(hasattr(self.serial, 'issuedWith'))
        self.assert_(hasattr(self.serial, 'keyTitle'))
        self.assert_(hasattr(self.serial, 'label'))
        self.assert_(hasattr(self.serial, 'lcOverseasAcq'))
        self.assert_(hasattr(self.serial, 'lccn'))
        self.assert_(hasattr(self.serial, 'legalDeposit'))
        self.assert_(hasattr(self.serial, 'local'))
        self.assert_(hasattr(self.serial, 'manufacture'))
        self.assert_(hasattr(self.serial, 'matrixNumber'))
        self.assert_(hasattr(self.serial, 'mediaCategory'))
        self.assert_(hasattr(self.serial, 'modeOfIssuance'))
        self.assert_(hasattr(self.serial, 'musicPlate'))
        self.assert_(hasattr(self.serial, 'musicPublisherNumber'))
        self.assert_(hasattr(self.serial, 'nban'))
        self.assert_(hasattr(self.serial, 'nbn'))
        self.assert_(hasattr(self.serial, 'notation'))
        self.assert_(hasattr(self.serial, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.serial, 'postalRegistration'))
        self.assert_(hasattr(self.serial, 'preferredCitation'))
        self.assert_(hasattr(self.serial, 'production'))
        self.assert_(hasattr(self.serial, 'provider'))
        self.assert_(hasattr(self.serial, 'providerStatement'))
        self.assert_(hasattr(self.serial, 'publication'))
        self.assert_(hasattr(self.serial, 'publisherNumber'))
        self.assert_(hasattr(self.serial, 'relatedInstance'))
        self.assert_(hasattr(self.serial, 'relatedTo'))
        self.assert_(hasattr(self.serial, 'reportNumber'))
        self.assert_(hasattr(self.serial, 'reproduction'))
        self.assert_(hasattr(self.serial, 'responsibilityStatement'))
        self.assert_(hasattr(self.serial, 'serialFirstIssue'))
        self.assert_(hasattr(self.serial, 'serialLastIssue'))
        self.assert_(hasattr(self.serial, 'sici'))
        self.assert_(hasattr(self.serial, 'soundContent'))
        self.assert_(hasattr(self.serial, 'stockNumber'))
        self.assert_(hasattr(self.serial, 'strn'))
        self.assert_(hasattr(self.serial, 'studyNumber'))
        self.assert_(hasattr(self.serial, 'supplementaryContentNote'))
        self.assert_(hasattr(self.serial, 'titleStatement'))
        self.assert_(hasattr(self.serial, 'upc'))
        self.assert_(hasattr(self.serial, 'uri'))
        self.assert_(hasattr(self.serial, 'urn'))
        self.assert_(hasattr(self.serial, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestStillImage(unittest.TestCase):

    def setUp(self):
        self.stillimage = StillImage()

    def test_init(self):
        self.assertEquals(type(self.stillimage), StillImage)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.stillimage, 'absorbed'))
        self.assert_(hasattr(self.stillimage, 'absorbedBy'))
        self.assert_(hasattr(self.stillimage, 'absorbedInPart'))
        self.assert_(hasattr(self.stillimage, 'absorbedInPartBy'))
        self.assert_(hasattr(self.stillimage, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.stillimage, 'classification'))
        self.assert_(hasattr(self.stillimage, 'classificationDdc'))
        self.assert_(hasattr(self.stillimage, 'classificationLcc'))
        self.assert_(hasattr(self.stillimage, 'classificationNlm'))
        self.assert_(hasattr(self.stillimage, 'classificationUdc'))
        self.assert_(hasattr(self.stillimage, 'containedIn'))
        self.assert_(hasattr(self.stillimage, 'contains'))
        self.assert_(hasattr(self.stillimage, 'contentCategory'))
        self.assert_(hasattr(self.stillimage, 'continuedBy'))
        self.assert_(hasattr(self.stillimage, 'continuedInPartBy'))
        self.assert_(hasattr(self.stillimage, 'continues'))
        self.assert_(hasattr(self.stillimage, 'continuesInPart'))
        self.assert_(hasattr(self.stillimage, 'dataSource'))
        self.assert_(hasattr(self.stillimage, 'dissertationDegree'))
        self.assert_(hasattr(self.stillimage, 'dissertationIdentifier'))
        self.assert_(hasattr(self.stillimage, 'dissertationInstitution'))
        self.assert_(hasattr(self.stillimage, 'dissertationNote'))
        self.assert_(hasattr(self.stillimage, 'dissertationYear'))
        self.assert_(hasattr(self.stillimage, 'event'))
        self.assert_(hasattr(self.stillimage, 'expressionOf'))
        self.assert_(hasattr(self.stillimage, 'findingAid'))
        self.assert_(hasattr(self.stillimage, 'geographicCoverageNote'))
        self.assert_(hasattr(self.stillimage, 'hasDerivative'))
        self.assert_(hasattr(self.stillimage, 'hasExpression'))
        self.assert_(hasattr(self.stillimage, 'hasInstance'))
        self.assert_(hasattr(self.stillimage, 'identifier'))
        self.assert_(hasattr(self.stillimage, 'index'))
        self.assert_(hasattr(self.stillimage, 'isDerivativeOf'))
        self.assert_(hasattr(self.stillimage, 'isan'))
        self.assert_(hasattr(self.stillimage, 'issnL'))
        self.assert_(hasattr(self.stillimage, 'istc'))
        self.assert_(hasattr(self.stillimage, 'iswc'))
        self.assert_(hasattr(self.stillimage, 'label'))
        self.assert_(hasattr(self.stillimage, 'languageNote'))
        self.assert_(hasattr(self.stillimage, 'mergedToForm'))
        self.assert_(hasattr(self.stillimage, 'originDate'))
        self.assert_(hasattr(self.stillimage, 'originPlace'))
        self.assert_(hasattr(self.stillimage, 'originalVersion'))
        self.assert_(hasattr(self.stillimage, 'otherEdition'))
        self.assert_(hasattr(self.stillimage, 'precedes'))
        self.assert_(hasattr(self.stillimage, 'relatedTo'))
        self.assert_(hasattr(self.stillimage, 'relatedWork'))
        self.assert_(hasattr(self.stillimage, 'separatedFrom'))
        self.assert_(hasattr(self.stillimage, 'series'))
        self.assert_(hasattr(self.stillimage, 'splitInto'))
        self.assert_(hasattr(self.stillimage, 'subject'))
        self.assert_(hasattr(self.stillimage, 'subseries'))
        self.assert_(hasattr(self.stillimage, 'subseriesOf'))
        self.assert_(hasattr(self.stillimage, 'succeeds'))
        self.assert_(hasattr(self.stillimage, 'supersededBy'))
        self.assert_(hasattr(self.stillimage, 'supersededInPartBy'))
        self.assert_(hasattr(self.stillimage, 'supersedes'))
        self.assert_(hasattr(self.stillimage, 'supersedesInPart'))
        self.assert_(hasattr(self.stillimage, 'supplement'))
        self.assert_(hasattr(self.stillimage, 'supplementTo'))
        self.assert_(hasattr(self.stillimage, 'temporalCoverageNote'))
        self.assert_(hasattr(self.stillimage, 'translation'))
        self.assert_(hasattr(self.stillimage, 'translationOf'))
        self.assert_(hasattr(self.stillimage, 'unionOf'))
        self.assert_(hasattr(self.stillimage, 'workTitle'))

    def tearDown(self):
        pass

class TestSummary(unittest.TestCase):

    def setUp(self):
        self.summary = Summary()

    def test_init(self):
        self.assertEquals(type(self.summary), Summary)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.summary, 'annotates'))
        self.assert_(hasattr(self.summary, 'annotationAssertedBy'))
        self.assert_(hasattr(self.summary, 'annotationBody'))
        self.assert_(hasattr(self.summary, 'annotationSource'))
        self.assert_(hasattr(self.summary, 'assertionDate'))
        self.assert_(hasattr(self.summary, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.summary, 'identifier'))
        self.assert_(hasattr(self.summary, 'label'))
        self.assert_(hasattr(self.summary, 'relatedTo'))
        self.assert_(hasattr(self.summary, 'startOfSummary'))
        self.assert_(hasattr(self.summary, 'summary'))
        self.assert_(hasattr(self.summary, 'summaryOf'))

    def tearDown(self):
        pass

class TestTableOfContents(unittest.TestCase):

    def setUp(self):
        self.tableofcontents = TableOfContents()

    def test_init(self):
        self.assertEquals(type(self.tableofcontents), TableOfContents)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.tableofcontents, 'annotates'))
        self.assert_(hasattr(self.tableofcontents, 'annotationAssertedBy'))
        self.assert_(hasattr(self.tableofcontents, 'annotationBody'))
        self.assert_(hasattr(self.tableofcontents, 'annotationSource'))
        self.assert_(hasattr(self.tableofcontents, 'assertionDate'))
        self.assert_(hasattr(self.tableofcontents, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.tableofcontents, 'identifier'))
        self.assert_(hasattr(self.tableofcontents, 'label'))
        self.assert_(hasattr(self.tableofcontents, 'relatedTo'))
        self.assert_(hasattr(self.tableofcontents, 'tableOfContents'))
        self.assert_(hasattr(self.tableofcontents, 'tableOfContentsFor'))

    def tearDown(self):
        pass

class TestTactile(unittest.TestCase):
    def setUp(self):
        self.tactile = Tactile()


    def test_init(self):
        self.assertEquals(type(self.tactile), Tactile)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.tactile, 'abbreviatedTitle'))
        self.assert_(hasattr(self.tactile, 'ansi'))
        self.assert_(hasattr(self.tactile, 'arrangement'))
        self.assert_(hasattr(self.tactile, 'aspectRatio'))
        self.assert_(hasattr(self.tactile, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.tactile, 'awardNote'))
        self.assert_(hasattr(self.tactile, 'carrierCategory'))
        self.assert_(hasattr(self.tactile, 'coden'))
        self.assert_(hasattr(self.tactile, 'colorContent'))
        self.assert_(hasattr(self.tactile, 'contentAccessibility'))
        self.assert_(hasattr(self.tactile, 'contentsNote'))
        self.assert_(hasattr(self.tactile, 'custodialHistory'))
        self.assert_(hasattr(self.tactile, 'dimensions'))
        self.assert_(hasattr(self.tactile, 'distribution'))
        self.assert_(hasattr(self.tactile, 'doi'))
        self.assert_(hasattr(self.tactile, 'duration'))
        self.assert_(hasattr(self.tactile, 'ean'))
        self.assert_(hasattr(self.tactile, 'edition'))
        self.assert_(hasattr(self.tactile, 'editionResponsibility'))
        self.assert_(hasattr(self.tactile, 'extent'))
        self.assert_(hasattr(self.tactile, 'fingerprint'))
        self.assert_(hasattr(self.tactile, 'formatOfMusic'))
        self.assert_(hasattr(self.tactile, 'frequency'))
        self.assert_(hasattr(self.tactile, 'frequencyNote'))
        self.assert_(hasattr(self.tactile, 'graphicScaleNote'))
        self.assert_(hasattr(self.tactile, 'hasEquivalent'))
        self.assert_(hasattr(self.tactile, 'hdl'))
        self.assert_(hasattr(self.tactile, 'identifier'))
        self.assert_(hasattr(self.tactile, 'illustrationNote'))
        self.assert_(hasattr(self.tactile, 'instanceOf'))
        self.assert_(hasattr(self.tactile, 'instanceTitle'))
        self.assert_(hasattr(self.tactile, 'isbn'))
        self.assert_(hasattr(self.tactile, 'isbn10'))
        self.assert_(hasattr(self.tactile, 'isbn13'))
        self.assert_(hasattr(self.tactile, 'ismn'))
        self.assert_(hasattr(self.tactile, 'iso'))
        self.assert_(hasattr(self.tactile, 'isrc'))
        self.assert_(hasattr(self.tactile, 'issn'))
        self.assert_(hasattr(self.tactile, 'issueNumber'))
        self.assert_(hasattr(self.tactile, 'issuedWith'))
        self.assert_(hasattr(self.tactile, 'keyTitle'))
        self.assert_(hasattr(self.tactile, 'label'))
        self.assert_(hasattr(self.tactile, 'lcOverseasAcq'))
        self.assert_(hasattr(self.tactile, 'lccn'))
        self.assert_(hasattr(self.tactile, 'legalDeposit'))
        self.assert_(hasattr(self.tactile, 'local'))
        self.assert_(hasattr(self.tactile, 'manufacture'))
        self.assert_(hasattr(self.tactile, 'matrixNumber'))
        self.assert_(hasattr(self.tactile, 'mediaCategory'))
        self.assert_(hasattr(self.tactile, 'modeOfIssuance'))
        self.assert_(hasattr(self.tactile, 'musicPlate'))
        self.assert_(hasattr(self.tactile, 'musicPublisherNumber'))
        self.assert_(hasattr(self.tactile, 'nban'))
        self.assert_(hasattr(self.tactile, 'nbn'))
        self.assert_(hasattr(self.tactile, 'notation'))
        self.assert_(hasattr(self.tactile, 'otherPhysicalFormat'))
        self.assert_(hasattr(self.tactile, 'postalRegistration'))
        self.assert_(hasattr(self.tactile, 'preferredCitation'))
        self.assert_(hasattr(self.tactile, 'production'))
        self.assert_(hasattr(self.tactile, 'provider'))
        self.assert_(hasattr(self.tactile, 'providerStatement'))
        self.assert_(hasattr(self.tactile, 'publication'))
        self.assert_(hasattr(self.tactile, 'publisherNumber'))
        self.assert_(hasattr(self.tactile, 'relatedInstance'))
        self.assert_(hasattr(self.tactile, 'relatedTo'))
        self.assert_(hasattr(self.tactile, 'reportNumber'))
        self.assert_(hasattr(self.tactile, 'reproduction'))
        self.assert_(hasattr(self.tactile, 'responsibilityStatement'))
        self.assert_(hasattr(self.tactile, 'serialFirstIssue'))
        self.assert_(hasattr(self.tactile, 'serialLastIssue'))
        self.assert_(hasattr(self.tactile, 'sici'))
        self.assert_(hasattr(self.tactile, 'soundContent'))
        self.assert_(hasattr(self.tactile, 'stockNumber'))
        self.assert_(hasattr(self.tactile, 'strn'))
        self.assert_(hasattr(self.tactile, 'studyNumber'))
        self.assert_(hasattr(self.tactile, 'supplementaryContentNote'))
        self.assert_(hasattr(self.tactile, 'titleStatement'))
        self.assert_(hasattr(self.tactile, 'upc'))
        self.assert_(hasattr(self.tactile, 'uri'))
        self.assert_(hasattr(self.tactile, 'urn'))
        self.assert_(hasattr(self.tactile, 'videorecordingNumber'))

    def tearDown(self):
        pass

class TestTemporal(unittest.TestCase):

    def setUp(self):
        self.temporal = Temporal()

    def test_init(self):
        self.assertEquals(type(self.temporal), Temporal)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.temporal, 'authorityAssigner'))
        self.assert_(hasattr(self.temporal, 'authoritySource'))
        self.assert_(hasattr(self.temporal, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.temporal, 'hasAuthority'))
        self.assert_(hasattr(self.temporal, 'identifier'))
        self.assert_(hasattr(self.temporal, 'label'))
        self.assert_(hasattr(self.temporal, 'relatedTo'))

    def tearDown(self):
        pass

class TestText(unittest.TestCase):
    def setUp(self):
        self.text = Text()


    def test_init(self):
        self.assertEquals(type(self.text), Text)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.text, 'absorbed'))
        self.assert_(hasattr(self.text, 'absorbedBy'))
        self.assert_(hasattr(self.text, 'absorbedInPart'))
        self.assert_(hasattr(self.text, 'absorbedInPartBy'))
        self.assert_(hasattr(self.text, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.text, 'classification'))
        self.assert_(hasattr(self.text, 'classificationDdc'))
        self.assert_(hasattr(self.text, 'classificationLcc'))
        self.assert_(hasattr(self.text, 'classificationNlm'))
        self.assert_(hasattr(self.text, 'classificationUdc'))
        self.assert_(hasattr(self.text, 'containedIn'))
        self.assert_(hasattr(self.text, 'contains'))
        self.assert_(hasattr(self.text, 'contentCategory'))
        self.assert_(hasattr(self.text, 'continuedBy'))
        self.assert_(hasattr(self.text, 'continuedInPartBy'))
        self.assert_(hasattr(self.text, 'continues'))
        self.assert_(hasattr(self.text, 'continuesInPart'))
        self.assert_(hasattr(self.text, 'dataSource'))
        self.assert_(hasattr(self.text, 'dissertationDegree'))
        self.assert_(hasattr(self.text, 'dissertationIdentifier'))
        self.assert_(hasattr(self.text, 'dissertationInstitution'))
        self.assert_(hasattr(self.text, 'dissertationNote'))
        self.assert_(hasattr(self.text, 'dissertationYear'))
        self.assert_(hasattr(self.text, 'event'))
        self.assert_(hasattr(self.text, 'expressionOf'))
        self.assert_(hasattr(self.text, 'findingAid'))
        self.assert_(hasattr(self.text, 'geographicCoverageNote'))
        self.assert_(hasattr(self.text, 'hasDerivative'))
        self.assert_(hasattr(self.text, 'hasExpression'))
        self.assert_(hasattr(self.text, 'hasInstance'))
        self.assert_(hasattr(self.text, 'identifier'))
        self.assert_(hasattr(self.text, 'index'))
        self.assert_(hasattr(self.text, 'isDerivativeOf'))
        self.assert_(hasattr(self.text, 'isan'))
        self.assert_(hasattr(self.text, 'issnL'))
        self.assert_(hasattr(self.text, 'istc'))
        self.assert_(hasattr(self.text, 'iswc'))
        self.assert_(hasattr(self.text, 'label'))
        self.assert_(hasattr(self.text, 'languageNote'))
        self.assert_(hasattr(self.text, 'mergedToForm'))
        self.assert_(hasattr(self.text, 'originDate'))
        self.assert_(hasattr(self.text, 'originPlace'))
        self.assert_(hasattr(self.text, 'originalVersion'))
        self.assert_(hasattr(self.text, 'otherEdition'))
        self.assert_(hasattr(self.text, 'precedes'))
        self.assert_(hasattr(self.text, 'relatedTo'))
        self.assert_(hasattr(self.text, 'relatedWork'))
        self.assert_(hasattr(self.text, 'separatedFrom'))
        self.assert_(hasattr(self.text, 'series'))
        self.assert_(hasattr(self.text, 'splitInto'))
        self.assert_(hasattr(self.text, 'subject'))
        self.assert_(hasattr(self.text, 'subseries'))
        self.assert_(hasattr(self.text, 'subseriesOf'))
        self.assert_(hasattr(self.text, 'succeeds'))
        self.assert_(hasattr(self.text, 'supersededBy'))
        self.assert_(hasattr(self.text, 'supersededInPartBy'))
        self.assert_(hasattr(self.text, 'supersedes'))
        self.assert_(hasattr(self.text, 'supersedesInPart'))
        self.assert_(hasattr(self.text, 'supplement'))
        self.assert_(hasattr(self.text, 'supplementTo'))
        self.assert_(hasattr(self.text, 'temporalCoverageNote'))
        self.assert_(hasattr(self.text, 'translation'))
        self.assert_(hasattr(self.text, 'translationOf'))
        self.assert_(hasattr(self.text, 'unionOf'))
        self.assert_(hasattr(self.text, 'workTitle'))

    def tearDown(self):
        pass

class TestThreeDimensionalObject(unittest.TestCase):

    def setUp(self):
        self.threedimensionalobject = ThreeDimensionalObject()

    def test_init(self):
        self.assertEquals(type(self.threedimensionalobject), ThreeDimensionalObject)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.threedimensionalobject, 'absorbed'))
        self.assert_(hasattr(self.threedimensionalobject, 'absorbedBy'))
        self.assert_(hasattr(self.threedimensionalobject, 'absorbedInPart'))
        self.assert_(hasattr(self.threedimensionalobject, 'absorbedInPartBy'))
        self.assert_(hasattr(self.threedimensionalobject, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.threedimensionalobject, 'classification'))
        self.assert_(hasattr(self.threedimensionalobject, 'classificationDdc'))
        self.assert_(hasattr(self.threedimensionalobject, 'classificationLcc'))
        self.assert_(hasattr(self.threedimensionalobject, 'classificationNlm'))
        self.assert_(hasattr(self.threedimensionalobject, 'classificationUdc'))
        self.assert_(hasattr(self.threedimensionalobject, 'containedIn'))
        self.assert_(hasattr(self.threedimensionalobject, 'contains'))
        self.assert_(hasattr(self.threedimensionalobject, 'contentCategory'))
        self.assert_(hasattr(self.threedimensionalobject, 'continuedBy'))
        self.assert_(hasattr(self.threedimensionalobject, 'continuedInPartBy'))
        self.assert_(hasattr(self.threedimensionalobject, 'continues'))
        self.assert_(hasattr(self.threedimensionalobject, 'continuesInPart'))
        self.assert_(hasattr(self.threedimensionalobject, 'dataSource'))
        self.assert_(hasattr(self.threedimensionalobject, 'dissertationDegree'))
        self.assert_(hasattr(self.threedimensionalobject, 'dissertationIdentifier'))
        self.assert_(hasattr(self.threedimensionalobject, 'dissertationInstitution'))
        self.assert_(hasattr(self.threedimensionalobject, 'dissertationNote'))
        self.assert_(hasattr(self.threedimensionalobject, 'dissertationYear'))
        self.assert_(hasattr(self.threedimensionalobject, 'event'))
        self.assert_(hasattr(self.threedimensionalobject, 'expressionOf'))
        self.assert_(hasattr(self.threedimensionalobject, 'findingAid'))
        self.assert_(hasattr(self.threedimensionalobject, 'geographicCoverageNote'))
        self.assert_(hasattr(self.threedimensionalobject, 'hasDerivative'))
        self.assert_(hasattr(self.threedimensionalobject, 'hasExpression'))
        self.assert_(hasattr(self.threedimensionalobject, 'hasInstance'))
        self.assert_(hasattr(self.threedimensionalobject, 'identifier'))
        self.assert_(hasattr(self.threedimensionalobject, 'index'))
        self.assert_(hasattr(self.threedimensionalobject, 'isDerivativeOf'))
        self.assert_(hasattr(self.threedimensionalobject, 'isan'))
        self.assert_(hasattr(self.threedimensionalobject, 'issnL'))
        self.assert_(hasattr(self.threedimensionalobject, 'istc'))
        self.assert_(hasattr(self.threedimensionalobject, 'iswc'))
        self.assert_(hasattr(self.threedimensionalobject, 'label'))
        self.assert_(hasattr(self.threedimensionalobject, 'languageNote'))
        self.assert_(hasattr(self.threedimensionalobject, 'mergedToForm'))
        self.assert_(hasattr(self.threedimensionalobject, 'originDate'))
        self.assert_(hasattr(self.threedimensionalobject, 'originPlace'))
        self.assert_(hasattr(self.threedimensionalobject, 'originalVersion'))
        self.assert_(hasattr(self.threedimensionalobject, 'otherEdition'))
        self.assert_(hasattr(self.threedimensionalobject, 'precedes'))
        self.assert_(hasattr(self.threedimensionalobject, 'relatedTo'))
        self.assert_(hasattr(self.threedimensionalobject, 'relatedWork'))
        self.assert_(hasattr(self.threedimensionalobject, 'separatedFrom'))
        self.assert_(hasattr(self.threedimensionalobject, 'series'))
        self.assert_(hasattr(self.threedimensionalobject, 'splitInto'))
        self.assert_(hasattr(self.threedimensionalobject, 'subject'))
        self.assert_(hasattr(self.threedimensionalobject, 'subseries'))
        self.assert_(hasattr(self.threedimensionalobject, 'subseriesOf'))
        self.assert_(hasattr(self.threedimensionalobject, 'succeeds'))
        self.assert_(hasattr(self.threedimensionalobject, 'supersededBy'))
        self.assert_(hasattr(self.threedimensionalobject, 'supersededInPartBy'))
        self.assert_(hasattr(self.threedimensionalobject, 'supersedes'))
        self.assert_(hasattr(self.threedimensionalobject, 'supersedesInPart'))
        self.assert_(hasattr(self.threedimensionalobject, 'supplement'))
        self.assert_(hasattr(self.threedimensionalobject, 'supplementTo'))
        self.assert_(hasattr(self.threedimensionalobject, 'temporalCoverageNote'))
        self.assert_(hasattr(self.threedimensionalobject, 'translation'))
        self.assert_(hasattr(self.threedimensionalobject, 'translationOf'))
        self.assert_(hasattr(self.threedimensionalobject, 'unionOf'))
        self.assert_(hasattr(self.threedimensionalobject, 'workTitle'))

    def tearDown(self):
        pass

class TestTitle(unittest.TestCase):

    def setUp(self):
        self.title = Title()

    def test_init(self):
        self.assertEquals(type(self.title), Title)

    def test_rdf_properties(self):
        self.assert_(hasattr(self.title, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.title, 'identifier'))
        self.assert_(hasattr(self.title, 'label'))
        self.assert_(hasattr(self.title, 'partNumber'))
        self.assert_(hasattr(self.title, 'partTitle'))
        self.assert_(hasattr(self.title, 'relatedTo'))
        self.assert_(hasattr(self.title, 'subtitle'))
        self.assert_(hasattr(self.title, 'titleAttribute'))
        self.assert_(hasattr(self.title, 'titleQualifier'))
        self.assert_(hasattr(self.title, 'titleSource'))
        self.assert_(hasattr(self.title, 'titleType'))
        self.assert_(hasattr(self.title, 'titleValue'))
        self.assert_(hasattr(self.title, 'titleVariationDate'))

    def tearDown(self):
        pass

class TestTopic(unittest.TestCase):
    def setUp(self):
        self.topic = Topic()


    def test_init(self):
        self.assertEquals(type(self.topic), Topic)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.topic, 'authorityAssigner'))
        self.assert_(hasattr(self.topic, 'authoritySource'))
        self.assert_(hasattr(self.topic, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.topic, 'hasAuthority'))
        self.assert_(hasattr(self.topic, 'identifier'))
        self.assert_(hasattr(self.topic, 'label'))
        self.assert_(hasattr(self.topic, 'relatedTo'))


    def tearDown(self):
        pass

class TestWork(unittest.TestCase):
    def setUp(self):
        self.work = Work()


    def test_init(self):
        self.assertEquals(type(self.work), Work)


    def test_rdf_properties(self):
        self.assert_(hasattr(self.work, 'absorbed'))
        self.assert_(hasattr(self.work, 'absorbedBy'))
        self.assert_(hasattr(self.work, 'absorbedInPart'))
        self.assert_(hasattr(self.work, 'absorbedInPartBy'))
        self.assert_(hasattr(self.work, 'authorizedAccessPoint'))
        self.assert_(hasattr(self.work, 'classification'))
        self.assert_(hasattr(self.work, 'classificationDdc'))
        self.assert_(hasattr(self.work, 'classificationLcc'))
        self.assert_(hasattr(self.work, 'classificationNlm'))
        self.assert_(hasattr(self.work, 'classificationUdc'))
        self.assert_(hasattr(self.work, 'containedIn'))
        self.assert_(hasattr(self.work, 'contains'))
        self.assert_(hasattr(self.work, 'contentCategory'))
        self.assert_(hasattr(self.work, 'continuedBy'))
        self.assert_(hasattr(self.work, 'continuedInPartBy'))
        self.assert_(hasattr(self.work, 'continues'))
        self.assert_(hasattr(self.work, 'continuesInPart'))
        self.assert_(hasattr(self.work, 'dataSource'))
        self.assert_(hasattr(self.work, 'dissertationDegree'))
        self.assert_(hasattr(self.work, 'dissertationIdentifier'))
        self.assert_(hasattr(self.work, 'dissertationInstitution'))
        self.assert_(hasattr(self.work, 'dissertationNote'))
        self.assert_(hasattr(self.work, 'dissertationYear'))
        self.assert_(hasattr(self.work, 'event'))
        self.assert_(hasattr(self.work, 'expressionOf'))
        self.assert_(hasattr(self.work, 'findingAid'))
        self.assert_(hasattr(self.work, 'geographicCoverageNote'))
        self.assert_(hasattr(self.work, 'hasDerivative'))
        self.assert_(hasattr(self.work, 'hasExpression'))
        self.assert_(hasattr(self.work, 'hasInstance'))
        self.assert_(hasattr(self.work, 'identifier'))
        self.assert_(hasattr(self.work, 'index'))
        self.assert_(hasattr(self.work, 'isDerivativeOf'))
        self.assert_(hasattr(self.work, 'isan'))
        self.assert_(hasattr(self.work, 'issnL'))
        self.assert_(hasattr(self.work, 'istc'))
        self.assert_(hasattr(self.work, 'iswc'))
        self.assert_(hasattr(self.work, 'label'))
        self.assert_(hasattr(self.work, 'languageNote'))
        self.assert_(hasattr(self.work, 'mergedToForm'))
        self.assert_(hasattr(self.work, 'originDate'))
        self.assert_(hasattr(self.work, 'originPlace'))
        self.assert_(hasattr(self.work, 'originalVersion'))
        self.assert_(hasattr(self.work, 'otherEdition'))
        self.assert_(hasattr(self.work, 'precedes'))
        self.assert_(hasattr(self.work, 'relatedTo'))
        self.assert_(hasattr(self.work, 'relatedWork'))
        self.assert_(hasattr(self.work, 'separatedFrom'))
        self.assert_(hasattr(self.work, 'series'))
        self.assert_(hasattr(self.work, 'splitInto'))
        self.assert_(hasattr(self.work, 'subject'))
        self.assert_(hasattr(self.work, 'subseries'))
        self.assert_(hasattr(self.work, 'subseriesOf'))
        self.assert_(hasattr(self.work, 'succeeds'))
        self.assert_(hasattr(self.work, 'supersededBy'))
        self.assert_(hasattr(self.work, 'supersededInPartBy'))
        self.assert_(hasattr(self.work, 'supersedes'))
        self.assert_(hasattr(self.work, 'supersedesInPart'))
        self.assert_(hasattr(self.work, 'supplement'))
        self.assert_(hasattr(self.work, 'supplementTo'))
        self.assert_(hasattr(self.work, 'temporalCoverageNote'))
        self.assert_(hasattr(self.work, 'translation'))
        self.assert_(hasattr(self.work, 'translationOf'))
        self.assert_(hasattr(self.work, 'unionOf'))
        self.assert_(hasattr(self.work, 'workTitle'))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
