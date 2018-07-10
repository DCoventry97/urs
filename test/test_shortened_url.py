import unittest
from shortened_url import is_shortened_url, get_url, check_new_url,add_url_to_xml
import xml.etree.ElementTree as ET
tree = ET.parse("test.xml")
root = tree.getroot()


class TestShortenedUrl(unittest.TestCase):

    # Tests for is_shortened_url
    def test_is_shortened_url_valid(self):
        self.assertTrue(is_shortened_url("g", root))

    def test_is_shortened_url_invalid(self):
        self.assertFalse(is_shortened_url("s", root))

    # Tests for get_url
    def test_get_url(self):
        self.assertEquals(get_url("g", root), "http://www.python.org")

    # Tests for validating new url arguments
    def test_check_new_url_valid(self):
        args_list = ["./main.py", "-n", "p", "http://www.python.org"]
        self.assertTrue(check_new_url(args_list))

    def test_check_new_url_invalid_n(self):
        args_list = ["./main.py", "-n", "-n", "http://www.python.org"]
        self.assertFalse(check_new_url(args_list))

    def test_check_new_url_invalid_r(self):
        args_list = ["./main.py", "-n", "-r", "http://www.python.org"]
        self.assertFalse(check_new_url(args_list))

    def test_check_new_url_invalid_help(self):
        args_list = ["./main.py", "-n", "help", "http://www.python.org"]
        self.assertFalse(check_new_url(args_list))

    # Tests for adding a new url to the xml file
    def test_add_url_to_xml(self):
        add_url_to_xml("testShort", "www.test.long", tree, "test.xml")
        value_holder = None
        for child in root:
            if child.get("short") == "testShort" and child.find("url").text == "www.test.long":
                value_holder = (child.get("short"), child.find("url").text)
        self.assertEqual(("testShort", "www.test.long"), value_holder)