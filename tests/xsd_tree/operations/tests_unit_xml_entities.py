"""Unit tests for XmlEntities operation
"""
from unittest import TestCase

from xml_utils.xsd_tree.operations.xml_entities import XmlEntities


class TestEscapeXmlEntities(TestCase):
    """Test Escape Xml Entities"""

    def test_escape_with_predefined_xml_entities(self):
        """test_escape_with_predefined_xml_entities"""

        string = "aaa<bbb>ccc&ddd'eee\"fff"

        xml_entities = XmlEntities()

        self.assertTrue(
            xml_entities.escape_xml_entities(string)
            == "aaa&lt;bbb&gt;ccc&amp;ddd&apos;eee&quot;fff"
        )
        self.assertTrue(xml_entities.unescaped_xml_string == string)
        self.assertTrue(xml_entities.number_of_subs_made == 5)

    def test_escape_already_escaped_string(self):
        """test_escape_already_escaped_string"""

        string = "aaa&lt;bbb&gt;ccc&amp;ddd&apos;eee&quot;fff"
        xml_entities = XmlEntities()

        self.assertTrue(xml_entities.escape_xml_entities(string) == string)
        self.assertTrue(xml_entities.unescaped_xml_string == string)
        self.assertTrue(xml_entities.number_of_subs_made == 0)

    def test_escape_full_predefined_xml_entities(self):
        """test_escape_full_predefined_xml_entities"""

        string = "<<<\"\"'''''''\"\"\">>>"

        xml_entities = XmlEntities()

        self.assertTrue(
            xml_entities.escape_xml_entities(string)
            == "&lt;&lt;&lt;&quot;&quot;&apos;&apos;&apos;&apos;&apos;&apos;&apos;&quot;&quot;&quot;&gt;&gt;&gt;"
        )
        self.assertTrue(xml_entities.unescaped_xml_string == string)
        self.assertTrue(xml_entities.number_of_subs_made == 18)

    def test_unescaped_and_already_escaped_predefined_xml_entities(self):
        """test_unescaped_and_already_escaped_predefined_xml_entities"""

        string = "<&lt;&quot;>&&&lt;"

        xml_entities = XmlEntities()

        self.assertTrue(
            xml_entities.escape_xml_entities(string)
            == "&lt;&lt;&quot;&gt;&amp;&amp;&lt;"
        )
        self.assertTrue(xml_entities.unescaped_xml_string == string)
        self.assertTrue(xml_entities.number_of_subs_made == 4)

    def test_unescaped_with_predefined_xml_entities(self):
        """test_unescaped_with_predefined_xml_entities"""

        string = "<&lt;&quot;>&&&lt;"

        self.assertTrue(
            XmlEntities.unescape_xml_entities(string)[0] == '<<">&&<'
        )
        self.assertTrue(XmlEntities.unescape_xml_entities(string)[1] == 3)

    def test_unescaped_without_predefined_xml_entities(self):
        """test_unescaped_without_predefined_xml_entities"""

        string = "aaabbbcccdddeee"

        self.assertTrue(
            XmlEntities.unescape_xml_entities(string)[0] == "aaabbbcccdddeee"
        )
        self.assertTrue(XmlEntities.unescape_xml_entities(string)[1] == 0)

    def test_unescaped_only_escaped_predefined_xml_entities(self):
        """test_unescaped_only_escaped_predefined_xml_entities"""

        string = "&lt;&lt;&lt;&quot;&quot;&apos;&apos;&apos;&apos;&apos;&apos;&apos;&quot;&quot;&quot;&gt;&gt;&gt;"

        self.assertTrue(
            XmlEntities.unescape_xml_entities(string)[0]
            == "<<<\"\"'''''''\"\"\">>>"
        )
        self.assertTrue(XmlEntities.unescape_xml_entities(string)[1] == 18)
