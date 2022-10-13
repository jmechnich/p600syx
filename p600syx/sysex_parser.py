"""
This module contains the abstract base class for all parsers in p600syx.
"""
from abc import ABCMeta, abstractmethod


class SysExParser(metaclass=ABCMeta):
    """
    This class is the abstract base for all parsers in p600syx.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def can_decode(self, msg: bytes) -> bool:
        """
        This function checks if the parser can decode a given MIDI SysEx dump
        using the header of the data.

        Parameters:
                msg (bytes): Midi SysEx dump

        Returns:
                True if parser can decode dump, False otherwise.
        """

    @abstractmethod
    def decode(
        self, msg: bytes
    ) -> tuple[int, list[tuple[str, int]], list[int]]:
        """
        This function decodes a MIDI SysEx dump. created using

        Parameter:
                msg (bytes): MIDI SysEx dump

        Returns:
                A tuple containing the program number, a list of parameters,
                and (possibly) a list of remaining integer data that was not or
                could not be decoded.
        """
