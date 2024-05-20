#!/usr/bin/env python3
import json

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass
    def all(self):
        return self.__objects
    def new(self, obj):
        key = self.__objects.__class__.__name__+"."+    self.obj.id
        self.__objects.update({key:obj})
    def save(self):
        with open(self.__file_path, "w") as serialized:
            json.dump(self.__objects, serialized)
    def reload(self):
        try:
            with open(self.__file_path, "r") as deserialized:
                self.__objects = json.load(deserialized)
        except:
            pass