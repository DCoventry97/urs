import unittest
from shortened_url import is_shortened_url, get_url, check_new_url
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
        self.assertEquals(get_url("g", root), "https://www.python.org")

    # Tests for adding a new url
    def test_check_new_url_valid(self):
        args_list = ["./main.py", "-n", "p", "https://www.python.org"]
        self.assertTrue(check_new_url(args_list))

    def test_check_new_url_invalid_n(self):
        args_list = ["./main.py", "-n", "-n", "https://www.python.org"]
        self.assertFalse(check_new_url(args_list))

