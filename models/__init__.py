#!/usr/bin/python3
''' creates a static FileStorage instance '''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
