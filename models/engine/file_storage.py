#!/usr/bin/python3
"""
file storage modules
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """
        File Storage Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        since __object is private class attribute
        we access it like so
        :return:
        """
        return self.__objects

    def new(self, obj):
        """
               sets in  __objects the obj with key <obj class name>.id
               :param obj: the class object
               :type obj: dictionary
               :return: dictionary
               :rtype: dictionary
        """
        self.__objects[__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
            each object/instance in the private class att __objects
            we serialise the instance (by creating a newDict of
            key and dict of attrs)
            then write the newDict to the file.json
        """
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file, indent=2)

    def reload(self):
        """
        read from the file, deserialize the dict obtained from the file
        each val from the dict is a dict of args and kwargs of an instance
        each key found represent an instance we check if it
        exit else we create new one
        and append if to the __objects
        :return: None
        """
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                content = file.read()
                dict_from_file = {}
                if content != "":
                    dict_from_file = json.loads(content)  # type = dict

                for file_key, dict_obj in dict_from_file.items():
                    # if the key_file is not in the storage.keys()
                    # create a new instance and pass it argument and kwargs
                    if file_key not in FileStorage.__objects.keys():
                        className = dict_obj["__class__"]
                        newInst = eval("{}(**dict_obj)".format(className))
                        self.new(newInst)
        except FileNotFoundError:
            pass
