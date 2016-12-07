import unittest
import os
from settings import Settings


class TestCreation(unittest.TestCase):
    """ Test the setup of the settings file """
    def test_default_creation(self):
        """ Test the we can create a file using defaults """
        if os.path.exists('settings.ini'):
            os.remove('settings.ini')
        Settings(__file__)
        self.assertTrue(os.path.exists('settings.ini'))
        
    def test_custom_filename(self):
        """ test we can create a file with a custom name """
        custom_name = 'custom_settings.ini'
        if os.path.exists(custom_name):
            os.remove(custom_name)
        Settings(__file__, filename=custom_name)
        self.assertTrue(os.path.exists(custom_name))
        
    def test_custom_path(self):
        """ test we can create a file with a custom path """
        custom_file_path = os.path.abspath('custom')
        output_file = os.path.join(custom_file_path, 'settings.ini')
        if os.path.exists(output_file):
            os.remove(output_file)
        Settings(custom_file_path)
        self.assertTrue(os.path.exists(output_file))
    
    def test_custom_file_path(self):
        """ test we can create a file with a custom path and file name """
        custom_file_path = os.path.abspath('custom')
        custom_name = 'custom_settings.ini'
        if os.path.exists(custom_name):
            os.remove(custom_name)
        output_file = os.path.join(custom_file_path, custom_name)
        if os.path.exists(output_file):
            os.remove(output_file)
        Settings(custom_file_path, filename=custom_name)
        self.assertTrue(os.path.exists(output_file))
    
    def test_create_false(self):
        """ test the file isn't created if told not to """
        if os.path.exists('settings.ini'):
            os.remove('settings.ini')
        self.assertRaises(OSError, Settings, __file__, create=False)
        self.assertFalse(os.path.exists('settings.ini'))


class TestUsage(unittest.TestCase):
    """ test the usage of the settings file """
    def setUp(self):
        """ setup the tests"""
        if os.path.exists('settings.ini'):
            os.remove('settings.ini')
        self.local_settings = Settings(__file__)
        
    def test_set_get(self):
        """ test we can set, and get back a value """
        key = 'key'
        value = 'value'
        self.local_settings.set(key, value)
        response = self.local_settings.get(key)
        self.assertTrue(value == response)
        
    def test_default_none(self):
        """ test None is returned on a key that doesn't exist """
        key = 'key'
        response = self.local_settings.get(key)
        self.assertIsNone(response)

    def test_default(self):
        """ test a specified default is returned on a key that doesn't exist"""
        key = 'key'
        default = 'default'
        response = self.local_settings.get(key, default=default)
        self.assertTrue(response == default)
        
    def test_add(self):
        """ test we can add a value to the settings from get """
        key = 'key'
        default = 'default'
        # check not there
        response = self.local_settings.get(key)
        self.assertIsNone(response)
        
        # add
        response = self.local_settings.get(key, default=default, add=True)
        self.assertTrue(response == default)
        
        # check there
        response = self.local_settings.get(key)
        self.assertTrue(response == default)
        
    def test_delete(self):
        """ test a key can be removed """
        key = 'key'
        value = 'value'
        self.local_settings.set(key, value)
        response = self.local_settings.get(key)
        self.assertTrue(value == response)
        
        self.local_settings.delete(key)
        response = self.local_settings.get(key)
        self.assertIsNone(response)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
