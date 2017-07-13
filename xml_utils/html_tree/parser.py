""" Package parsing HTML
"""
from lxml import etree, html
from xml_utils.commons.exceptions import HTMLError


def parse_html(html_text, parent_tag=''):
    """ Try to parse and unparse HTML to verify that is correctly formatted

    Params:
        html_text:
        parent_tag:

    Returns:

    Raises:
    """
    try:
        return etree.fromstring("<%s>%s</%s>" % (parent_tag, html_text, parent_tag))
    except Exception as e:
        raise HTMLError(e.message)


def safe_html(html_text):
    """ Returns safe HTML from input

    Parameters:
        html_text:

    Returns:
    """
    return etree.tostring(html.fragment_fromstring(html_text, create_parent='div'))
