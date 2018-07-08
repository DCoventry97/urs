import unittest
from main import check_input

class TestCheckInput(unittest.TestCase):

    def test_n_flag(self):
        args_list = ["./main.py", "-n", "t", "test.test"]
        self.assertEqual(check_input(args_list), 1)

    def test_new_flag(self):
        args_list = ["./main.py", "--new", "t", "test.test"]
        self.assertEqual(check_input(args_list), 1)

    def test_help_flag(self):
        args_list = ["./main.py", "help"]
        self.assertEqual(check_input(args_list), 2)

    def test_h_flag(self):
        args_list = ["./main.py", "-h"]
        self.assertEqual(check_input(args_list), 2)

    def test_dash_dash_help_flag(self):
        args_list = ["./main.py", "--help"]
        self.assertEqual(check_input(args_list), 2)

    def test_r_flag(self):
        args_list = ["./main.py", "-r", "A", "B"]
        self.assertEqual(check_input(args_list), 3)

    def test_rename_flag(self):
        args_list = ["./main.py", "--rename", "A", "B"]
        self.assertEqual(check_input(args_list), 3)

    def test_d_flag(self):
        args_list = ["./main.py", "-d", "A"]
        self.assertEqual(check_input(args_list), 4)

    def test_delete_flag(self):
        args_list = ["./main.py", "--delete", "A"]
        self.assertEqual(check_input(args_list), 4)