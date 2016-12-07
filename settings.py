import json
import os.path


class Settings(object):
    """
    Allows usage of settings files

    :param file_path: __file__ or custom location
    :type file_path: String
    :param filename:(optional) name of settings file
    :type filename: String
    :param create:(optional) create the settings file if not found
    :type create: True
    :raises: OSError if create == False, and file not found
    :returns: Settings instance
    :rtype: Settings instance
    """
    def __init__(self, file_path, filename='settings.ini', create=True):
        if os.path.isfile(file_path):
            self.path = os.path.dirname(file_path)
        else:
            self.path = file_path
        self.file_path = os.path.abspath(os.path.join(self.path, file_name))
        self._contents = {}
        
        if not os.path.exists(self.path):
            if create:
                os.makedirs(self.path)
        
        if not os.path.isfile(self.file_path):
            if create:
                self._write_file()
            else:
                raise OSError('File {} not found'.format(self.file_path))
        # read the file contents
        self._contents = self._read_file()
        # write it out to re-order
        self._write_file()
    
    def update(self):
        """ 
        update the internal data structure from the file.
        
        :returns: None
        """
        self._contents = self._read_file()
    
    def set(self, key, value):
        """
        Set a value in the file
        
        :param key: name of setting
        :type key: String
        :param value: value of setting 
        :type value: Any
        :returns: None
        """
        self._contents = self._read_file()
        self._contents[key] = value
        self._write_file()
        
    def get(self, key, default=None, add=False, update=False):
        """
        Get a value of a setting
        
        :param key: name of setting
        :type key: String
        :param default: (Optional) what to return if key not found.
        :type default: Any
        :param add: (Optional) if not found, add the default to the settings 
        :type add: Boolean
        :param update: (Optional) refresh stored settings before getting
        :type update: Boolean
        """
        if update:
            self._contents = self._read_file()
        value = default
        try:
            value = self._contents[key]
        except KeyError:
            if add:
                self.set(key, value)
        return value
        
    def delete(self, key, update=True):
        """ 
        Remove a setting
        
        :param key: setting to remove 
        :type key: String
        :param update: update the file after removing
        :type update: Boolean
        :returns: Success
        :rtype: Boolean
        """
        try:
            del self._contents[key]
            if update:
                self._write_file()
            success = True
        except KeyError:
            success = False
        return success
        
    def dump(self):
        """ returns the contents of settings"""
        return self._contents
    
    def _read_file(self):
        """ 
        reads the settings file from disk 
        Returns: decoded settings file
        """
        json_contents = None
        with open(self.file_path) as file_obj:
            contents = file_obj.read()
            try:
                json_contents = json.loads(contents)    
            except ValueError as err:
                print('Error reading settings file: {}'.format(err))
        return json_contents
        
    def _write_file(self):
        """ write the internal settings to disk """
        with open(self.file_path, 'w') as file_obj:
            contents = json.dumps(self._contents, sort_keys=True, indent=4)
            file_obj.write(contents)
