from unittest import TestCase
from os.path import join, dirname, abspath
from xml_utils.xsd_hash import xsd_hash

RESOURCES_PATH = join(dirname(abspath(__file__)), 'data')


class TestSimpleXSD(TestCase):
    def setUp(self):
        xsd_file = open(join(RESOURCES_PATH, 'chemical-element.xsd'), 'r')
        self.content = xsd_file.read()
        self.hash = xsd_hash.get_hash(self.content)

    def test_same(self):
        # makes sure that the same XSD produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'chemical-element.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_spaces(self):
        # makes sure that an XSD with additional spaces produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'spaces-in-element.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_spaces2(self):
        # makes sure that an XSD with additional spaces, returns,tabs produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'spaces-return-tab.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_comments(self):
        # makes sure that an XSD with documentation tags produces different hash
        xsd_file = open(join(RESOURCES_PATH, 'different-comments.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_different_annotations(self):
        # makes sure that an XSD with different comments produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'different-annotation.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_different_annotations_levels(self):
        # makes sure that an XSD with different comments produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'annotations-levels.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_different_namespace(self):
        # makes sure that an XSD with different comments produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'namespace.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)

    def test_wrong_enum(self):
        # makes sure that an XSD with different enumeration does not produce the same hash
        xsd_file = open(join(RESOURCES_PATH, 'wrong-enum.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)


class TestComplexXSD(TestCase):
    def setUp(self):
        xsd_file = open(join(RESOURCES_PATH, 'composition.xsd'), 'r')
        self.content = xsd_file.read()
        self.hash = xsd_hash.get_hash(self.content)

    def test_same(self):
        # makes sure that the same XSD produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'composition.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_order(self):
        # makes sure that an XSD with elements in a different order produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'order.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_root(self):
        # makes sure that an XSD with different root names does not produce the same hash
        xsd_file = open(join(RESOURCES_PATH, 'root-name.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)

    def test_type(self):
        # makes sure that an XSD with different type names does not produce the same hash
        xsd_file = open(join(RESOURCES_PATH, 'type-name.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertNotEqual(self.hash, content_hash)


class TestMoreComplexXSD(TestCase):
    def setUp(self):
        xsd_file = open(join(RESOURCES_PATH, 'demo.diffusion.xsd'), 'r')
        self.content = xsd_file.read()
        self.hash = xsd_hash.get_hash(self.content)

    def test_same(self):
        # makes sure that the same XSD produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'demo.diffusion.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)

    def test_order(self):
        # makes sure that an XSD with elements in a different order produces the same hash
        xsd_file = open(join(RESOURCES_PATH, 'order2.xsd'), 'r')
        content = xsd_file.read()
        content_hash = xsd_hash.get_hash(content)
        self.assertEqual(self.hash, content_hash)
