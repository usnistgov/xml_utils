""" Unit tests for appinfo operations
"""
from unittest import TestCase

from lxml import etree

from xml_utils.commons.exceptions import XMLError
from xml_utils.xsd_tree.operations.appinfo import (
    add_appinfo_element,
    delete_appinfo_element,
)
from xml_utils.xsd_tree.xsd_tree import XSDTree


class TestAddAppInfoElement(TestCase):
    """Test Add App Info Element"""

    def test_add_app_info_element_invalid_xsd_raises_xsd_error(self):
        """test_add_app_info_element_invalid_xsd_raises_xsd_error"""

        xsd_string = "invalid"
        with self.assertRaises(etree.XMLSyntaxError):
            add_appinfo_element(xsd_string, "", "", "")

    def test_add_app_info_element_invalid_xpath_raises_xsd_error(self):
        """test_add_app_info_element_invalid_xpath_raises_xsd_error"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <root><test></test></root>
            </xs:schema>
        """
        xpath = "invalid"
        with self.assertRaises(XMLError):
            add_appinfo_element(xsd_string, xpath, "attribute", "value")

    def test_add_app_info_element_no_annotation_adds_it(self):
        """test_add_app_info_element_no_annotation_adds_it"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root"/>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "value"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>value</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_no_app_info_adds_it(self):
        """test_add_app_info_element_no_app_info_adds_it"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation></xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "value"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>value</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_no_element_adds_it(self):
        """test_add_app_info_element_no_element_adds_it"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
            <xs:element name="root"><xs:annotation>
            <xs:appinfo></xs:appinfo></xs:annotation></xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "value"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>value</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_annotation_present_updates_it(self):
        """test_add_app_info_element_annotation_present_updates_it"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation></xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "value"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>value</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_app_info_present_updates_it(self):
        """test_add_app_info_element_app_info_present_updates_it"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation><xs:appinfo></xs:appinfo></xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "value"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>value</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_present_updates_it(self):
        """test_add_app_info_element_present_updates_it"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "new"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>new</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_absent_from_two_app_info(self):
        """test_add_app_info_element_absent_from_two_appinfo"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo></xs:appinfo>
                        <xs:appinfo></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        xpath = "xs:element"
        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "new"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>new</attribute></xs:appinfo>
                        <xs:appinfo/>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_present_in_first_of_two_app_info(self):
        """test_add_app_info_element_present_in_first_of_two_app_info"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                        <xs:appinfo></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "new"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>new</attribute></xs:appinfo>
                        <xs:appinfo/>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_present_in_second_of_two_app_info(self):
        """test_add_app_info_element_present_in_second_of_two_app_info"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo></xs:appinfo>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = add_appinfo_element(
            xsd_string, xpath, "attribute", "new"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo/>
                        <xs:appinfo><attribute>new</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_present_in_two_app_info_raises_exception(
        self,
    ):
        """test_add_app_info_element_present_in_two_app_info_raises_exception"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        with self.assertRaises(XMLError):
            add_appinfo_element(xsd_string, xpath, "attribute", "new")


class TestDeleteAppInfoElement(TestCase):
    """Test Delete App Info Element"""

    def test_delete_app_info_element_invalid_xsd_raises_xsd_error(self):
        """test_delete_app_info_element_invalid_xsd_raises_xsd_error"""

        xsd_string = "invalid"
        with self.assertRaises(etree.XMLSyntaxError):
            delete_appinfo_element(xsd_string, "", "")

    def test_delete_app_info_element_invalid_xpath_raises_xsd_error(self):
        """test_delete_app_info_element_invalid_xpath_raises_xsd_error"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <root><test></test></root>
            </xs:schema>
        """
        xpath = "invalid"
        with self.assertRaises(XMLError):
            delete_appinfo_element(xsd_string, xpath, "")

    def test_delete_app_info_element_removed_if_exists(self):
        """test_delete_app_info_element_removed_if_exists"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>value</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"
        attribute_name = "attribute"
        updated_xsd_string = delete_appinfo_element(
            xsd_string, xpath, attribute_name
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation><xs:appinfo/></xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_delete_attribute_does_not_fail_if_not_present(self):
        """test_delete_attribute_does_not_fail_if_not_present"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation><xs:appinfo></xs:appinfo></xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"
        attribute_name = "attribute"
        delete_appinfo_element(xsd_string, xpath, attribute_name)

    def test_delete_app_info_element_absent_from_two_appinfo_does_not_fail(
        self,
    ):
        """test_delete_app_info_element_absent_from_two_appinfo_does_not_fail"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo></xs:appinfo>
                        <xs:appinfo></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        delete_appinfo_element(xsd_string, xpath, "attribute")

    def test_delete_app_info_element_present_in_first_of_two_app_info(self):
        """test_delete_app_info_element_present_in_first_of_two_appinfo"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                        <xs:appinfo></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = delete_appinfo_element(
            xsd_string, xpath, "attribute"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo/><xs:appinfo/>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_present_in_second_of_two_app_info(self):
        """test_add_app_info_element_present_in_second_of_two_app_info"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo></xs:appinfo>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        updated_xsd_string = delete_appinfo_element(
            xsd_string, xpath, "attribute"
        )

        expected_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation><xs:appinfo/><xs:appinfo/></xs:annotation>
                </xs:element>
            </xs:schema>
        """

        updated_tree = XSDTree.fromstring(updated_xsd_string)
        updated_xsd_string = XSDTree.tostring(updated_tree)

        expected_tree = XSDTree.fromstring(expected_string)
        expected_string = XSDTree.tostring(expected_tree)

        self.assertEqual(updated_xsd_string, expected_string)

    def test_add_app_info_element_present_in_two_app_info_raises_exception(
        self,
    ):
        """test_add_app_info_element_present_in_two_app_info_raises_exception"""

        xsd_string = """
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                <xs:element name="root">
                    <xs:annotation>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                        <xs:appinfo><attribute>old</attribute></xs:appinfo>
                    </xs:annotation>
                </xs:element>
            </xs:schema>
        """
        xpath = "xs:element"

        with self.assertRaises(XMLError):
            delete_appinfo_element(xsd_string, xpath, "attribute")
