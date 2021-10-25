# -*- coding: utf-8 -*-
"""Defines the "HasMessage" mixin"""

class HasMessage(object):
    """Mixin for report components that have a message

    Defines a single attribute message, and associated setters and getters.
    Can be used to apply a "message" attribute to test cases, phases, etc.

    Attributes:
        message (str): message explaining status or outcome
    """

    def __initialize_message(self):
        self.message = ""
    
    def set_message(self, message):
        self.message = message
    
    def get_message(self):
        return self.message
