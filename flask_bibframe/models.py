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
import re
import sys

from types import MethodType
from rdflib import Graph, URIRef

BIBFRAME_RDF = None
BIBFRAME_URL = 'http://bibframe.org/vocab.rdf'
CLASS_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#Class')
DOMAIN_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#domain')
SUBCLASS_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#subClassOf')

MODEL_TYPE_RE = re.compile(r"models.(\w+)")

class BibframeEntity(object):
    """BibframeEntity is a the base class for Flask-BIBFRAME Python Classes used
    in Flask applications"""

    def __init__(self, **kwargs):
        "Initializes an instance and sets parameters for the instance"
        self.identifiers = kwargs.get('identifiers', {})
        self.semantic_stores = kwargs.get('semantic_stores', [])
        if MODEL_TYPE_RE.search(str(self.__class__)):
            model_type = MODEL_TYPE_RE.search(str(self.__class__)).groups()[0]
            setattr(self, '@type', model_type)

        # Populates RDF properties
        for key in kwargs.keys():
            if hasattr(self, key):
                setattr(self, key, kwargs.get(key))

    def as_dict(self, show_null=True):
        "Returns the entity's BIBFRAMe properties as a Python dictionary"
        output = {}#self.identifiers
        for name in dir(self):
            if not name.startswith("_") and not name.startswith("semantic_stores"):
                rdf_property = getattr(self, name)
                if type(rdf_property) == MethodType:
                    continue
                elif not show_null and rdf_property is None:
                    continue
                else:
                    output[name] = rdf_property
        return output

    def as_json(self, with_namespace=False):
        "Returns the entity's BIBFRAME properties in JSON-LD"
        output = self.as_dict()
        if with_namespace:
            for key in output.keys():
                value = output.pop(key)
                output['bf:{}'.format(key)] = value
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
