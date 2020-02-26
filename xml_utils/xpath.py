""" XPath related functions
"""
from lxml import etree

from xml_utils.commons import exceptions


def validate_xpath(xpath):
    """ Validate a provided xpath.

    Args:
        xpath:

    Raises:
        xml_utils.commons.exceptions.XPathError
    """
    try:
        etree.XPath(xpath.strip())
    except etree.XPathSyntaxError as e:
        raise exceptions.XPathError(str(e))
