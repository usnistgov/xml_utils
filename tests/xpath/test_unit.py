""" Unit test for xpath module
"""
from unittest import TestCase

from xml_utils.commons.exceptions import XPathError
from xml_utils.xpath import validate_xpath


class TestValidateXpath(TestCase):
    """Test validate_xpath function"""

    def test_xpath_is_striped(self):
        """test_xpath_is_striped"""
        mock_xpath = "  mock_xpath   "

        self.assertEqual(
            validate_xpath(mock_xpath), validate_xpath(mock_xpath.strip())
        )

    def test_dollar_start_xpath_raises_error(self):
        """test_dollar_start_xpath_raises_error"""
        mock_xpath = "$mock_xpath/tag"

        with self.assertRaises(XPathError):
            validate_xpath(mock_xpath)

    def test_dollar_middle_xpath_raises_error(self):
        """test_dollar_middle_xpath_raises_error"""
        mock_xpath = "/tag/$mock_xpath@attr"

        with self.assertRaises(XPathError):
            validate_xpath(mock_xpath)

    def test_invalid_xpath_raises_error(self):
        """test_invalid_xpath_raises_error"""
        mock_xpath = "/@+mock_xpath@attr"

        with self.assertRaises(XPathError):
            validate_xpath(mock_xpath)

    def test_valid_xpath_returns_none(self):
        """test_valid_xpath_returns_none"""
        mock_xpath = "/mock_xpath/tag/@attr"

        validate_xpath(mock_xpath)
