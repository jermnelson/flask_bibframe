#-------------------------------------------------------------------------------
# Name:        models
# Purpose:     Provides Python BIBFRAME models using
#              <http://bibframe.org:8282/vocab.rdf>
#
# Author:      Jeremy Nelson
#
# Created:     2014-02-06
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     MIT
#-------------------------------------------------------------------------------

import json
import sys
from rdflib import Graph, URIRef

BIBFRAME_RDF = None
BIBFRAME_URL = 'http://bibframe.org/vocab.rdf'
CLASS_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#Class')
DOMAIN_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#domain')
SUBCLASS_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#subClassOf')

class BibframeEntity(object):
    """BibframeEntity is a the base class for Flask-BIBFRAME Python Classes used
    in Flask applications"""

    def __init__(self, **kwargs):
        "Initializes an instance and sets parameters for the instance"
        self.identifiers = kwargs.get('identifiers', {})
        self.semantic_stores = kwargs.get('semantic_stores', [])
        # Populates RDF properties
        for key in kwargs.keys():
            if hasattr(self, key):
                setattr(self, key, kwargs.get(key))

    def as_json(self):
        "Returns the entity's BIBFRAME properties in JSON-LD"
        output = self.identifiers
        for name in dir(self):
            if not name.startswith("_"):
                rdf_property = getattr(self, name)
                if type(rdf_property) == instancemethod:
                    continue
                else:
                    output[name] = rdf_property
        print(output)
        return json.dumps(output, indent=2, sort_keys=True)


    def save(self):
        """Interaties through the entity's semantic data-stores and saves JSON
        to each semantic store. The semantic data-store decides what and how to
        store the entity's representation."""
        for store in self.semantic_stores:
            store.update(self.as_json())


def __get_properties__(graph, uri):
    """Recursive function goes through BIBFRAME class inheritance and returns
    all current uri and parent properties as a dictionary.

    :param graph: BIBFRAME RDF graph
    :param uri: URIRef of BIBFRAME entity
    """
    properties = {}
    for property_uri in graph.subjects(DOMAIN_URI, uri):
        property_name = property_uri.split("/")[-1]
        properties[property_name] = None
    parent_uri = graph.value(uri, SUBCLASS_URI)
    if parent_uri is not None:
        properties.update(__get_properties__(graph, parent_uri))
    return properties


def main():
    bibframe_graph = Graph()
    bibframe_graph.parse(BIBFRAME_URL)
    for uri in bibframe_graph.subjects(None, CLASS_URI):
        class_name = uri.split("/")[-1]
        class_properties = __get_properties__(bibframe_graph, uri)
        new_class = type(str(class_name),
                         (BibframeEntity,),
                         class_properties)
        setattr(sys.modules[__name__],
                str(class_name),
                new_class)
    BIBFRAME_RDF = bibframe_graph




main()
