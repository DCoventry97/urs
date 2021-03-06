import unittest
from check_input import check_input, check_new_short_is_valid, check_new_short_is_unique
from shortened_url import add_url_to_xml
import xml.etree.ElementTree as ET
tree = ET.parse("test.xml")
root = tree.getroot()


class TestCheckInput(unittest.TestCase):

    def test_n_flag(self):
        args_list = ["./main.py", "-n", "t", "test.test"]
        self.assertEqual(check_input(args_list, root), 1)

    def test_new_flag(self):
        args_list = ["./main.py", "--new", "t", "test.test"]
        self.assertEqual(check_input(args_list, root), 1)

    def test_help_flag(self):
        args_list = ["./main.py", "help"]
        self.assertEqual(check_input(args_list, root), 2)

    def test_h_flag(self):
        args_list = ["./main.py", "-h"]
        self.assertEqual(check_input(args_list, root), 2)

    def test_dash_dash_help_flag(self):
        args_list = ["./main.py", "--help"]
        self.assertEqual(check_input(args_list, root), 2)

    def test_r_flag(self):
        args_list = ["./main.py", "-r", "A", "B"]
        self.assertEqual(check_input(args_list, root), 3)

    def test_rename_flag(self):
        args_list = ["./main.py", "--rename", "A", "B"]
        self.assertEqual(check_input(args_list, root), 3)

    def test_d_flag(self):
        args_list = ["./main.py", "-d", "A"]
        self.assertEqual(check_input(args_list, root), 4)

    def test_delete_flag(self):
        args_list = ["./main.py", "--delete", "A"]
        self.assertEqual(check_input(args_list, root), 4)

    def test_valid_shortened_url(self):
        args_list = ["./main.py", "g"]
        self.assertEqual(check_input(args_list, root), 0)

    def test_invalid_shortened_url(self):
        args_list = ["./main.py", "invalid_url"]
        self.assertEqual(check_input(args_list, root), -1)

    def test_v_flag(self):
        args_list = ["./main.py", "-v"]
        self.assertEqual(check_input(args_list, root), 5)

    def test_view_all_urls_flag(self):
        args_list = ["./main.py", "--view-all-urls"]
        self.assertEqual(check_input(args_list, root), 5)

    # Tests if new short uses a keyword
    def test_check_new_short_is_valid_valid(self):
        self.assertTrue(check_new_short_is_valid("q"))

    def test_check_new_short_is_valid_invalid(self):
        self.assertFalse(check_new_short_is_valid("help"))

    # Tests for checking if the new long is unique
    def test_check_new_short_is_unique_valid(self):
        self.assertTrue(check_new_short_is_unique("uniqueShort", root))

    def test_check_new_short_is_unique_invalid(self):
        add_url_to_xml("notUniqueShort", "www.notuniquelong.com", tree, "test.xml")
        self.assertFalse(check_new_short_is_unique("notUniqueShort", root))
