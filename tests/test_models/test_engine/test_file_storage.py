#!/usr/bin/python3

import unittest
import json
from datetime import datetime
from time import sleep
from models.engine.file_storage import FileStorage

class TestFileStorge(unittest.TestCase) :
    "     test file storge"
    def test_instances(self):
        """chequeamos instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()
