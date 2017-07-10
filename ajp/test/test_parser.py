__author__ = 'ademarizu'
import unittest
import datetime
from ajp.parser import AdvancedJsonParser as ajp

class ComplexObject:
    """
    Simple Complex Object
    """

    def __init__(self, name, other_object=None):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.other_object = other_object


class AdvancedJsonParserTestCase(unittest.TestCase):

    def test_dumps(self):
        co = ComplexObject("Complex")
        dumpped = ajp.dumps(co)
        self.assertTrue(str, type(dumpped))

        co = ComplexObject("Complex", ComplexObject("Inner Complex"))
        dumpped = ajp.dumps(co)
        self.assertTrue(str, type(dumpped))

    def test_loads(self):
        json_str = '{"name": "Value"}'
        loaded = ajp.loads(json_str)
        self.assertTrue(dict, type(loaded))
        self.assertEquals("Value", loaded.get("name"))

        json_str = ajp.dumps(ComplexObject("Complex"))
        loaded = ajp.loads(json_str)
        self.assertTrue(dict, type(loaded))
        self.assertTrue(bool(loaded.get("creation_date")))
        self.assertFalse(bool(loaded.get("other_object")))
        self.assertEquals("Complex", loaded.get("name"))


        json_str = ajp.dumps(ComplexObject("Complex", ComplexObject("Inner Complex")))
        loaded = ajp.loads(json_str)
        self.assertTrue(dict, type(loaded))
        self.assertTrue(bool(loaded.get("creation_date")))
        self.assertTrue(bool(loaded.get("other_object")))
        self.assertEquals("Complex", loaded.get("name"))
        self.assertEquals("Inner Complex", loaded.get("other_object").get("name"))

