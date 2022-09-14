""" Unit tests for additional methods
"""
from unittest import TestCase
from unittest import skip

from xml_utils.commons.exceptions import XMLError
from xml_utils.xsd_tree.xsd_tree import XSDTree


class TestAdditionalMethods(TestCase):
    """Test Additional Methods"""

    def test_iterparse_method_without_unicode(self):
        """test_iterparse_method_without_unicode"""

        xsd_string = """
            <xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'>
                <root><test></test></root>
            </xs:schema>
        """
        XSDTree.iterparse(xsd_string, ("end",))

    def test_iterparse_method_with_unicode(self):
        """test_iterparse_method_with_unicode"""

        xsd_string = """
            <xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'>
                <\u0192-root><test></test></\u0192-root>
            </xs:schema>
        """
        XSDTree.iterparse(xsd_string, ("end",))

    @skip("Exception not raised since py3 migration")
    def test_iterparse_method_without_decoded_symbols(self):
        """test_iterparse_method_without_decoded_symbols"""

        xsd_string = """
            <xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'>
                <ƒ-root><test></test></ƒ-root>
            </xs:schema>
        """

        with self.assertRaises(XMLError):
            XSDTree.iterparse(xsd_string, ("end",))
