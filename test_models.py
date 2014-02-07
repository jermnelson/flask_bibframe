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

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()

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

##def test_frame(bf_class):
##    print("""class Test{}(unittest.TestCase):""".format(bf_class))
##    print("""    def setUp(self):
##        self.{} = {}()""".format(bf_class.lower(), bf_class))
##    print("\n")
##    print("""    def test_init(self):
##        self.assertEquals(type(self.{}), {})""".format(bf_class.lower(), bf_class))
##    print("\n")
##    print("""    def test_rdf_properties(self):""")
##    for row in dir(getattr(models, bf_class)):
##        if type(row) == unicode:
##            print("""        self.assert_(hasattr(self.{}, '{}'))""".format(bf_class.lower(), row))
##    print("\n")
##    print("""    def tearDown(self):
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


if __name__ == '__main__':
    unittest.main()
