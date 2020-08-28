""" Xml Utils Exceptions
"""


class XMLError(Exception):
    """Exception raised by XML validation"""

    def __init__(self, message):
        self.message = message


class XPathError(Exception):
    """Exception raised by XPath validation"""

    def __init__(self, message):
        self.message = message


class HTMLError(Exception):
    """Exception raised by HTML parsing"""

    def __init__(self, message):
        self.message = message
