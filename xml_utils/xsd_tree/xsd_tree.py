""" XSD tree operation, build, parse
"""
import lxml.etree as etree
import xml_utils.commons.exceptions as exceptions
from io import BytesIO


class XSDTree(object):
    """ XSD tree class
    """

    @staticmethod
    def build_tree(xml_string):
        """ Returns a lxml etree from an XML string (xml, xsd...)

        Args:
            xml_string:

        Returns:

        """
        try:
            xml_tree = etree.parse(BytesIO(xml_string.encode('utf-8')))
        except Exception:
            xml_tree = etree.parse(BytesIO(xml_string))
        return xml_tree

    @staticmethod
    def tostring(xml_tree, pretty=False):
        """ Return an XML String from a lxml etree

        Args:
            xml_tree:
            pretty:

        Returns:

        """
        try:
            return etree.tostring(xml_tree, pretty_print=pretty)
        except Exception as e:
            raise exceptions.XMLError(e.message)

    @staticmethod
    def fromstring(xml_string):
        """ Convert a string to an XML tree

        Args:
            xml_string:

        Returns:

        """
        try:
            return etree.fromstring(xml_string)
        except Exception as e:
            raise exceptions.XMLError(e.message)

    @staticmethod
    def iterfind(xml_string, match):
        """ Finds all matching sub elements, by tag name or path.
        Args:
            xml_string: String xml.
            match: Pattern to match

        Returns:
            An iterable yielding all matching elements in document order.

        """
        try:
            xml_tree = XSDTree.build_tree(xml_string)
            return xml_tree.iterfind(match)
        except Exception as e:
            raise exceptions.XMLError(e.message)

