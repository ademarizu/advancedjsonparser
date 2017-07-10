__author__ = 'ademarizu'
import json
from datetime import datetime


class AdvancedJsonParser:
    """
    A Json Parser for complex objects.
    """

    @staticmethod
    def dumps(obj):
        """
        Dumps complex objects as String JSON.
        :param obj: Complex Object
        :return: str
        """
        return json.dumps(obj, default=AdvancedJsonParser._default_parser)

    @staticmethod
    def loads(str_json):
        """
        Loads String JSON and returns a Dictionary
        :param str_json: JSON String
        :return: dict
        """
        return json.loads(str_json)

    @staticmethod
    def _default_parser(obj):
        """
        Default parser useful for parsing complex objects
        :param obj: Complex Object
        :return: parsed complex object
        """
        if getattr(obj, "__dict__", None):
            return obj.__dict__
        elif type(obj) == datetime:
            return obj.isoformat()
        else:
            return str(obj)