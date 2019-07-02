#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8


class TestBaseModel(unittest.TestCase):
    """Tests BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up test cases"""
        cls.base = BaseModel()

    @classmethod
    def teardown(cls):
        """Cleans memory after tests"""
        del cls.base
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_init(self):
        """Tests for the __init__"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_check_attributes(self):
        """Check if the attributes of the instance exist"""
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "created_at"))
        self.assertTrue(hasattr(BaseModel, "updated_at"))

if __name__ == "__main__":
    unittest.main()
