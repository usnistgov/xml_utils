""" XSD tree operation, build, parse
"""
import lxml.etree as etree
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
