#!/usr/bin/python3
"""Test script for saving and reloading BaseModel objects."""

import os
import unittest
from models.base_model import BaseModel
from models import storage


class TestSaveReloadBaseModel(unittest.TestCase):
    """Test cases for saving and reloading BaseModel objects."""

    def setUp(self):
        """Set up test environment."""
        pass

    def tearDown(self):
        """Tear down test environment."""
        self.reset_storage()
        pass

    def reset_storage(self):
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_save_reload(self):
        """Test saving and reloading BaseModel objects."""
        # Reloaded objects
        print("-- Reloaded objects --")
        objs = storage.all()
        for key, value in objs.items():
            print(f"[{value.__class__.__name__}] ({value.id}) {value.to_dict()}")

        # Create a new object
        print("-- Create a new object --")
        new_obj = BaseModel()
        new_obj.save()
        print(f"[{new_obj.__class__.__name__}] ({new_obj.id}) {new_obj.to_dict()}")

        # Ensure the new object is saved and can be reloaded
        self.assertTrue(storage.all().get(f"{new_obj.__class__.__name__}.{new_obj.id}") is not None)


if __name__ == "__main__":
    unittest.main()
