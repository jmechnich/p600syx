"""
This module provides an interface to several MIDI SysEx dump formats for
the Sequential Circuits Prophet-600 analog synthesizer.
"""

from .sequential_sysex_parser import SequentialSysExParser
from .gligli_sysex_parser import GliGliSysExParser
from .imogen7_sysex_parser import Imogen7SysExParser
from .imogen8_sysex_parser import Imogen8SysExParser

class SysExParserFactory:
    """
    This factory class is the provider for all registered parser classes.
    """
    def __init__(self):
        self.parsers = {}
    def register_parser(self, parser):
        """
        This function takes a parser object as argument and registers it
        with the factory.

        Parameters:
                parser (object): An object implementing the functions
                'can_decode' and 'decode' (see already implemented classes)
        """
        if not parser.name in self.parsers:
            self.parsers[parser.name] = parser
    def get_parser(self, msg):
        """
        This function returns a suitable parser for decoding a SysEx
        messages if available, None otherwise.

        Parameters:
                msg (bytes): A MIDI SysEx message as a bytestring.

        Returns:
                parser object or None
        """
        for _, parser in self.parsers.items():
            if parser.can_decode(msg):
                return parser
        return None

factory = SysExParserFactory()
factory.register_parser(SequentialSysExParser())
factory.register_parser(GliGliSysExParser())
factory.register_parser(Imogen7SysExParser())
factory.register_parser(Imogen8SysExParser())
