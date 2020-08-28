""" XPath related functions
"""
from copy import deepcopy

from lxml import etree

from xml_utils.commons import exceptions


def validate_xpath(xpath):
    """Validate a provided xpath.

    Args:
        xpath:

    Raises:
        xml_utils.commons.exceptions.XPathError
    """
    try:
        etree.XPath(xpath.strip())
    except etree.XPathSyntaxError as e:
        raise exceptions.XPathError(str(e))


def create_tree_from_xpath(xpath, xml_tree, namespaces=None, default_xpath=""):
    """Create tree at a given xpath. Recursive function

    Args:
        xpath:
        xml_tree:
        namespaces:
        default_xpath:

    Returns:
        The resulting tree
    """
    # Make a copy of the input tree to avoid modifying it directly
    xml_tree = deepcopy(xml_tree)

    if xpath == "":  # If the Xpath is empty, return the current xml_tree
        return xml_tree

    # Split the xpath and extract the first element
    xpath_elements = xpath.split("/")
    xpath_element = ""

    while xpath_element == "":  # Avoid retrieving empty xpath elements
        xpath_element = xpath_elements.pop(0)

    new_xpath = "%s/%s" % (default_xpath, xpath_element)

    try:
        assert len(xml_tree.xpath(new_xpath, namespaces=namespaces)) == 1
    except AssertionError as assertionError:
        if default_xpath == "":  # If this is the root element, raise the error
            raise AssertionError(assertionError)

        element = xml_tree.xpath(default_xpath, namespaces=namespaces)

        if xpath_element.startswith("@"):
            element[0].set(xpath_element[1:], "")
        else:
            element[0].append(etree.Element(xpath_element))

    return create_tree_from_xpath(
        "/".join(xpath_elements),
        xml_tree,
        namespaces=namespaces,
        default_xpath=new_xpath,
    )
