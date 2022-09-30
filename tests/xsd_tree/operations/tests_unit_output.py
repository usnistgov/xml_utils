""" Unit tests for output method
"""
import logging
from unittest import TestCase

from xml_utils.xsd_tree.xsd_tree import XSDTree

logger = logging.getLogger(__name__)


class TestOutputMethod(TestCase):
    """Test Output Method"""

    def test_output_with_method(self):
        """test_output_with_method"""
        xsd_string = (
            '<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"'
            ' xmlns:rsm="http://schema.nist.gov/xml/res-md/1.0wd-02-2017">'
            '<xsl:output xsl="http://www.w3.org/1999/XSL/Transform" '
            'method="text" indent="yes" encoding="UTF-8" /> </xsl:stylesheet>'
        )
        xslt_parsed = XSDTree.build_tree(xsd_string)
        extension_result = XSDTree.get_extension(xslt_parsed)
        self.assertEqual(extension_result, "text")

    def test_output_without_method_xml_default(self):
        """test_output_without_method_xml_default"""
        xsd_string = (
            '<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" '
            'xmlns:rsm="http://schema.nist.gov/xml/res-md/1.0wd-02-2017">'
            '<xsl:output xsl="http://www.w3.org/1999/XSL/Transform" indent="yes" encoding="UTF-8" /> </xsl:stylesheet>'
        )
        xslt_parsed = XSDTree.build_tree(xsd_string)
        extension_result = XSDTree.get_extension(xslt_parsed)
        self.assertEqual(extension_result, "xml")

    def test_output_without_method_html_default(self):
        """test_output_without_method_html_default"""
        xsd_string = (
            '<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" '
            'xmlns:rsm="http://schema.nist.gov/xml/res-md/1.0wd-02-2017">'
            '<html lang="en"><head></head><body></body></html> </xsl:stylesheet>'
        )
        xslt_parsed = XSDTree.build_tree(xsd_string)
        extension_result = XSDTree.get_extension(xslt_parsed)
        self.assertEqual(extension_result, "html")

    def test_output_without_default_method(self):
        """test_output_without_default_method"""
        xsd_string = (
            '<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" '
            'xmlns:rsm="http://schema.nist.gov/xml/res-md/1.0wd-02-2017"> </xsl:stylesheet>'
        )
        xslt_parsed = XSDTree.build_tree(xsd_string)
        extension_result = XSDTree.get_extension(xslt_parsed)
        self.assertEqual(extension_result, "xml")
