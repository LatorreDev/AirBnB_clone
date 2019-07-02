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

    def test_pep8(self):
        """PEP8 style test"""
        guide = pep8.StyleGuide(quit=True)
        rev = guide.check_files(["models/base_model.py"])
        self.assertEqual(rev.total_errors, 0, "Fix Style")

    def test_docstring(self):
        """Checks for docs"""
        for doc_fun in dir(BaseModel):
            self.assertIsNotNone(doc_fun.__doc__)

    def test_init(self):
        """Tests for the __init__"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_check_attributes(self):
        """Check if the attributes of the instance exist"""
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "created_at"))
        self.assertTrue(hasattr(BaseModel, "updated_at"))

    def test_save(self):
        """Tests save method"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)


if __name__ == "__main__":
    unittest.main()
