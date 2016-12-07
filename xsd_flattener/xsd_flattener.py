"""XSD Flattener abstract class
"""
import lxml.etree as etree
from io import BytesIO
from abc import ABCMeta, abstractmethod

# FIXME: refactor duplicated code from core
SCHEMA_NAMESPACE = "http://www.w3.org/2001/XMLSchema"
LXML_SCHEMA_NAMESPACE = "{" + SCHEMA_NAMESPACE + "}"


class XSDFlattener(object):
    """Abstract XSD Flattener class
    """
    __metaclass__ = ABCMeta

    def __init__(self, xml_string, download_enabled=True):
        """Initializes the flattener

        :param xml_string:
        :param download_enabled:
        """
        self.xml_string = xml_string
        self.dependencies = []
        self.download_enabled = download_enabled

    def get_flat(self):
        """Returns the flattened file

        :return:
        """
        # builds the parser
        parser = etree.XMLParser(remove_blank_text=True, remove_comments=True, remove_pis=True)
        # sets the parser
        etree.set_default_parser(parser=parser)

        # parse the XML String removing blanks, comments, processing instructions
        xml_tree = _build_tree(self.xml_string)

        # replace the includes by their content
        return self._replace_all_includes_by_content(xml_tree)

    def get_flat_dependency(self, uri):
        try:
            # if the same uri has not already been added to the main tree
            if uri not in self.dependencies:
                self.dependencies.append(uri)
                # get the content of the dependency
                dependency_content = self.get_dependency_content(uri)
                # build the tree
                xml_tree = _build_tree(dependency_content)
                # replace the includes by their content
                return self._replace_all_includes_by_content(xml_tree)
            else:
                return None
        except:
            return None

    def _replace_all_includes_by_content(self, xml_tree):
        """Replace all includes by their content

        :param xml_tree:
        :return:
        """
        # get the includes
        includes = xml_tree.findall("{}include".format(LXML_SCHEMA_NAMESPACE))
        # check if it has includes
        if len(includes) > 0:
            # browse includes
            for include_element in includes:
                # get the schema location uri
                uri = include_element.attrib['schemaLocation']
                # get the flattened dependency
                flat_dependency = self.get_flat_dependency(uri)
                # replace the include by its content
                XSDFlattener._replace_include_by_content(xml_tree, include_element, flat_dependency)
        return etree.tostring(xml_tree)

    @staticmethod
    def _replace_include_by_content(xml_tree, include_element, dependency_content):
        """Replace an include by its content

        :param xml_tree:
        :param include_element:
        :param dependency_content:
        :return:
        """
        if dependency_content is not None:
            # build the tree of the dependency
            dependency_tree = etree.fromstring(dependency_content)
            # get elements from dependency
            dependency_elements = dependency_tree.getchildren()
            # appends elements from dependency to tree
            for element in dependency_elements:
                xml_tree.getroot().append(element)
        # remove the include element
        include_element.getparent().remove(include_element)

    @abstractmethod
    def get_dependency_content(self, uri):
        pass


# FIXME: refactor duplicated code from core
def _build_tree(xml_string):
    """
        Return a lxml etree from an XML string (xml, xsd...)
        :param xml_string:
        :return:
    """
    try:
        xml_tree = etree.parse(BytesIO(xml_string.encode('utf-8')))
    except Exception:
        xml_tree = etree.parse(BytesIO(xml_string))

    return xml_tree
