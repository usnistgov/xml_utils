"""Predefined xml entities operations
"""
import re


class XmlEntities:
    """Xml Entities"""

    def __init__(self):
        """Escape all the predefined xml entities

        Args:
            xml_string:

        """
        self.number_of_subs_made = 0
        self.unescaped_xml_string = ""
        self.escaped_xml_string = ""

    def escape_xml_entities(self, xml_string):
        """escape_xml_entities

        Args:
            xml_string:

        Returns:

        """

        self.unescaped_xml_string = xml_string
        self.escaped_xml_string = xml_string

        # table which match a escaped predefined xml entities with a regex to find those occurence
        regex_match_table = [
            {
                "escape_char": "&amp;",
                "regex": "(&)(?!amp;)(?!gt;)(?!lt;)(?!apos;)(?!quot;)",
            },
            {"escape_char": "&gt;", "regex": "(>)"},
            {"escape_char": "&lt;", "regex": "(<)"},
            {"escape_char": "&apos;", "regex": "(')"},
            {"escape_char": "&quot;", "regex": '(")'},
        ]

        # for all predefined xml entities in the match table
        for subn_regex in regex_match_table:

            # compile the regex
            regex = re.compile(subn_regex["regex"])

            # substitute the predefined xml entities found by this escaped version
            subn_tuple = re.subn(
                regex, subn_regex["escape_char"], self.escaped_xml_string
            )

            # get the escaped xml string and the number of substitution
            self.escaped_xml_string = subn_tuple[0]
            self.number_of_subs_made += subn_tuple[1]

        return self.escaped_xml_string

    @staticmethod
    def unescape_xml_entities(xml_string):
        """Unescape all the predefined xml entities

        Args:
            xml_string:

        Returns:
            tuple<string, number>: Tuple with the unescaped string and the number of substitutions done

        """

        unescape_string = xml_string
        subs_number = 0
        # table which match a escaped predefined xml entities with a regex to find those occurence
        regex_match_table = [
            {"char": "&", "regex": "(&amp;)"},
            {"char": ">", "regex": "(&gt;)"},
            {"char": "<", "regex": "(&lt;)"},
            {"char": "'", "regex": "(&apos;)"},
            {"char": '"', "regex": "(&quot;)"},
        ]

        # for all escaped predefined xml entities in the match table
        for subn_regex in regex_match_table:

            # compile the regex
            regex = re.compile(subn_regex["regex"])

            # substitute the predefined xml entities found by this unescaped version
            subn_tuple = re.subn(regex, subn_regex["char"], unescape_string)

            unescape_string = subn_tuple[0]
            subs_number += subn_tuple[1]

        return unescape_string, subs_number
