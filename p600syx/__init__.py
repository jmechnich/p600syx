from .SequentialSysExParser import SequentialSysExParser
from .GliGliSysExParser import GliGliSysExParser
from .Imogen7SysExParser import Imogen7SysExParser
from .Imogen8SysExParser import Imogen8SysExParser

class SysExParserFactory:
    def __init__(self):
        self.parsers = {}
    def register_parser(self, parser):
        if not parser.name in self.parsers:
            self.parsers[parser.name] = parser
    def get_parser(self, msg):
        for name, parser in self.parsers.items():
            if parser.can_parse(msg):
                return parser
        return None

factory = SysExParserFactory()
factory.register_parser(SequentialSysExParser())
factory.register_parser(GliGliSysExParser())
factory.register_parser(Imogen7SysExParser())
factory.register_parser(Imogen8SysExParser())
