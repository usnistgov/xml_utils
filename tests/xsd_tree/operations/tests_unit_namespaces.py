""" Unit tests for namespaces operations
"""
from unittest import TestCase

from lxml import etree

from xml_utils.xsd_tree.operations.namespaces import (
    get_namespaces,
    get_default_prefix,
    get_target_namespace,
)
from xml_utils.xsd_tree.xsd_tree import XSDTree


class TestGetNamespaces(TestCase):
    """Test Get Namespaces"""

    def test_get_namespaces_one_namespace_prefix_is_key(self):
        """test_get_namespaces_one_namespace_prefix_is_key"""

        xsd_string = """
            <xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'></xs:schema>
        """
        namespaces = get_namespaces(xsd_string)
        self.assertTrue("xs" in list(namespaces.keys()))

    def test_get_namespaces_one_namespace_namespace_is_value(self):
        """test_get_namespaces_one_namespace_namespace_is_value"""

        xsd_string = "<xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'></xs:schema>"
        namespaces = get_namespaces(xsd_string)
        self.assertTrue(namespaces["xs"] == "http://www.w3.org/2001/XMLSchema")

    def test_get_namespaces_two_namespaces(self):
        """test_get_namespaces_two_namespaces"""

        xsd_string = """
            <xs:schema
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:test="test">
            </xs:schema>
        """
        namespaces = get_namespaces(xsd_string)
        self.assertTrue(
            "xs" in list(namespaces.keys())
            and "test" in list(namespaces.keys())
        )

    def test_get_namespaces_invalid_file(self):
        """test_get_namespaces_invalid_file"""

        xsd_string = "invalid"
        with self.assertRaises(etree.XMLSyntaxError):
            get_namespaces(xsd_string)

    def test_get_namespaces_xml_namespace(self):
        """test_get_namespaces_xml_namespace"""

        xsd_string = "<xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'></xs:schema>"
        namespaces = get_namespaces(xsd_string)
        self.assertTrue("xml" in list(namespaces.keys()))


class TestGetDefaultPrefix(TestCase):
    """Test Get Default Prefix"""

    def test_get_xs_prefix(self):
        """test_get_xs_prefix"""

        xsd_string = "<xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema'></xs:schema>"
        namespaces = get_namespaces(xsd_string)
        prefix = get_default_prefix(namespaces)
        self.assertTrue(prefix == "xs")

    def test_get_xsd_prefix(self):
        """test_get_xsd_prefix"""

        xsd_string = "<xsd:schema xmlns:xsd='http://www.w3.org/2001/XMLSchema'></xsd:schema>"
        namespaces = get_namespaces(xsd_string)
        prefix = get_default_prefix(namespaces)
        self.assertTrue(prefix == "xsd")

    def test_get_no_prefix(self):
        """test_get_no_prefix"""

        xsd_string = "<schema></schema>"
        namespaces = get_namespaces(xsd_string)
        prefix = get_default_prefix(namespaces)
        self.assertTrue(prefix == "")


class TestGetTargetNamespace(TestCase):
    """Test Get Target Namespace"""

    def test_no_target_namespace_returns_none_values(self):
        """test_no_target_namespace_returns_none_values"""

        xsd_string = "<schema></schema>"
        xsd_tree = XSDTree.build_tree(xsd_string)
        namespaces = get_namespaces(xsd_string)
        self.assertEqual(
            (None, ""), get_target_namespace(xsd_tree, namespaces)
        )

    def test_target_namespace_no_prefix_returns_target_namespace_only(self):
        """test_target_namespace_no_prefix_returns_target_namespace_only"""

        xsd_string = "<schema targetNamespace='namespace'></schema>"
        xsd_tree = XSDTree.build_tree(xsd_string)
        namespaces = get_namespaces(xsd_string)
        self.assertEqual(
            ("namespace", ""), get_target_namespace(xsd_tree, namespaces)
        )

    def test_target_namespace_with_prefix_returns_target_namespace_and_prefix(
        self,
    ):
        """test_target_namespace_with_prefix_returns_target_namespace_and_prefix"""

        xsd_string = "<schema targetNamespace='namespace' xmlns:ns='namespace'></schema>"
        xsd_tree = XSDTree.build_tree(xsd_string)
        namespaces = get_namespaces(xsd_string)
        self.assertEqual(
            ("namespace", "ns"), get_target_namespace(xsd_tree, namespaces)
        )
