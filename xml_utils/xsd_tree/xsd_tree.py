""" XSD tree operation, build, parse
"""
import lxml.etree as etree
import xml_utils.commons.constants as xml_constants
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
    def transform_to_xslt(xml_parsed):
        """ Turn an XML document into an XSLT object.

        Args:
            xml_parsed:

        Returns:

        """
        try:
            return etree.XSLT(xml_parsed)
        except:
            return etree.XSLT(xml_parsed.encode('utf-8'))

    @staticmethod
    def transform_to_xml(xml_string):
        """ Turn an XML document into an XML object.

        Args:
            xml_string:

        Returns:

        """
        try:
            return etree.XML(xml_string)
        except:
            return etree.XML(xml_string.encode('utf-8'))

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

    @staticmethod
    def iterparse(xml_string, events):
        """ Returns etree.iterparse

        Args:
            xml_string:
            events:

        Returns:

        """
        try:
            xml_file = BytesIO(str(xml_string))
            return etree.iterparse(xml_file, events)
        except Exception as e:
            raise exceptions.XMLError(e.message)

    @staticmethod
    def get_extension(xml_tree):
        """ Returns the extension file from a parsed xml

        Args:
            xml_tree: result of build_tree

        Returns:

        """
        try:
            return xml_tree.find("//xsl:output",
                                 namespaces={'xsl': xml_constants.XSL_NAMESPACE}).attrib['method']
        except Exception as e:
            raise exceptions.XMLError(e.message)
