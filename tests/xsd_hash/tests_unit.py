""" Unit tests for XSD hash function
"""
from os.path import join, dirname, abspath
from unittest import TestCase

from xml_utils.xsd_hash import xsd_hash

RESOURCES_PATH = join(dirname(abspath(__file__)), "data")


class TestSimpleXSD(TestCase):
    """Test Simple XSD"""

    def setUp(self):
        """setUp"""

        with open(
            join(RESOURCES_PATH, "chemical-element.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            self.content = xsd_file.read()
            self.hash = xsd_hash.get_hash(self.content)

    def test_same_file(self):
        """test_same_file"""

        # Make sure that the same XSD produces the same hash
        with open(
            join(RESOURCES_PATH, "chemical-element.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)

        self.assertEqual(self.hash, content_hash)

    def test_different_spaces_01(self):
        """test_different_spaces_01"""

        # Make sure that an XSD with additional spaces produces the same hash
        with open(
            join(RESOURCES_PATH, "chemical-element-spaces-01.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)

        self.assertEqual(self.hash, content_hash)

    def test_different_spaces_02(self):
        """test_different_spaces_02"""

        # Make sure that an XSD with additional spaces, returns,tabs produces
        # the same hash
        with open(
            join(RESOURCES_PATH, "chemical-element-spaces-02.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)

        self.assertEqual(self.hash, content_hash)

    def test_different_documentation(self):
        """test_different_documentation"""

        # Make sure that an XSD with documentation tags produces different hash
        with open(
            join(RESOURCES_PATH, "chemical-element-documentation.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_different_annotations_01(self):
        """test_different_annotations_01"""

        # Make sure that an XSD with different comments produces the same hash
        with open(
            join(RESOURCES_PATH, "chemical-element-annot-01.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_different_annotations_02(self):
        """test_different_annotations_02"""

        # Make sure that an XSD with different comments produces the same hash
        with open(
            join(RESOURCES_PATH, "chemical-element-annot-02.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_different_namespace(self):
        """test_different_namespace"""

        # Make sure that an XSD with different comments produces the same hash
        with open(
            join(RESOURCES_PATH, "chemical-element-namespace.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)

    def test_wrong_enum(self):
        """test_wrong_enum"""

        # Make sure that an XSD with different enumeration does not produce
        # the same hash
        with open(
            join(RESOURCES_PATH, "chemical-element-enum.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)


class TestCommonXSD(TestCase):
    """Test Common XSD"""

    def setUp(self):
        """setUp"""

        with open(
            join(RESOURCES_PATH, "composition.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            self.content = xsd_file.read()
            self.hash = xsd_hash.get_hash(self.content)

    def test_same_file(self):
        """test_same_file"""

        # Make sure that the same XSD produces the same hash
        with open(
            join(RESOURCES_PATH, "composition.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_mixed_order(self):
        """test_mixed_order"""

        # Make sure that an XSD with elements in a different order produces
        # the same hash
        with open(
            join(RESOURCES_PATH, "composition-mixed.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_different_root(self):
        """test_different_root"""

        # Make sure that an XSD with different root names does not produce
        # the same hash
        with open(
            join(RESOURCES_PATH, "composition-root-name.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)

    def test_different_type(self):
        """test_different_type"""

        # Make sure that an XSD with different type names does not produce
        # the same hash
        with open(
            join(RESOURCES_PATH, "composition-type-name.xsd"),
            "r",
            encoding="utf-8",
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)


class TestComplexXSD(TestCase):
    """Test Complex XSD"""

    def setUp(self):
        """setUp"""

        with open(
            join(RESOURCES_PATH, "diffusion.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            self.content = xsd_file.read()
            self.hash = xsd_hash.get_hash(self.content)

    def test_same(self):
        """test_same"""

        # Make sure that the same XSD produces the same hash
        with open(
            join(RESOURCES_PATH, "diffusion.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_mixed_order(self):
        """test_mixed_order"""

        # Make sure that an XSD with elements in a different order produces
        # the same hash
        with open(
            join(RESOURCES_PATH, "diffusion-mixed.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)


class TestKnownXSD(TestCase):
    """Test Known XSD"""

    def test_registry_hash_value(self):
        """test_registry_hash_value"""

        res_md_hash = "4735069b4332ee196e95b4db7877b6dcea9692ec"

        with open(
            join(RESOURCES_PATH, "res-md.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(res_md_hash, content_hash)

    def test_ammd_hash_value(self):
        """test_ammd_hash_value"""

        ammd_hash = "b056869f2e87adbf6b56b0ec19e65f9761cc6826"

        with open(
            join(RESOURCES_PATH, "ammd-r2018a.xsd"), "r", encoding="utf-8"
        ) as xsd_file:
            content = xsd_file.read()
            content_hash = xsd_hash.get_hash(content)
        self.assertEqual(ammd_hash, content_hash)
