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
import sys
from rdflib import Graph, URIRef

BIBFRAME_URL = 'http://bibframe.org/vocab.rdf'
CLASS_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#Class')
DOMAIN_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#domain')
SUBCLASS_URI = URIRef(u'http://www.w3.org/2000/01/rdf-schema#subClassOf')

def __get_properties__(graph, uri):
    """Recursive function goes through BIBFRAME class inheritance and returns
    all current uri and parent properties as a dictionary.

    :param graph: BIBFRAME RDF graph
    :param uri: URIRef of BIBFRAME entity
    """
    properties = {}
    for property_uri in graph.subjects(DOMAIN_URI,
                                                    uri):
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
                         (object,),
                         class_properties)
        setattr(sys.modules[__name__],
                str(class_name),
                new_class)




main()
