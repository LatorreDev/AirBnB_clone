import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8

class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base1 = BaseModel()

    @classmethod
    def teardown(cls):
        del cls.base1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_check_attributes(self):
        self.assertTrue(hasattr(BaseModel, "id"))
        self.assertTrue(hasattr(BaseModel, "created_at"))
        self.assertTrue(hasattr(BaseModel, "updated_at"))

if __name__ == "__main__":
    unittest.main()
