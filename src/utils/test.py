# src/tests/test_file_operations.py

import unittest
from utils.file_operations import open_file, save_file

class TestFileOperations(unittest.TestCase):
    
    def test_open_file(self):
        content = open_file("test.txt")
        self.assertIsInstance(content, str)

    def test_save_file(self):
        result = save_file("test.txt", "Hello, World!")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
