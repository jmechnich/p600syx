"""
This module contains the parser for decoding MIDI SysEx dumps created using
the original GliGli mod for the Sequential Circuits Prophet-600 analog
synthesizer.
"""

from .sysex_parser import SysExParser
from .error import ParseError


class GliGliSysExParser(SysExParser):
    """
    This class implements the decoding of MIDI SysEx dumps created using
    the original GliGli mod for the Sequential Circuits Prophet-600 analog
    synthesizer.
    """

    parameters = [
        ("Osc A Frequency", 2),
        ("Osc A Volume", 2),
        ("Osc A Pulse Width", 2),
        ("Osc B Frequency", 2),
        ("Osc B Volume", 2),
        ("Osc B Pulse Width", 2),
        ("Osc B Fine", 2),
        ("Cutoff", 2),
        ("Resonance", 2),
        ("Filter Envelope Amount", 2),
        ("Filter Release", 2),
        ("Filter Sustain", 2),
        ("Filter Decay", 2),
        ("Filter Attack", 2),
        ("Amp Release", 2),
        ("Amp Sustain", 2),
        ("Amp Decay", 2),
        ("Amp Attack", 2),
        ("Poly Mod Filter Amount", 2),
        ("Poly Mod Osc B Amount", 2),
        ("LFO Frequency", 2),
        ("LFO Amount", 2),
        ("Glide", 2),
        ("Amp Velocity", 2),
        ("Filter Velocity", 2),
        ("Osc A Saw", 1),
        ("Osc A Triangle", 1),
        ("Osc A Sqr", 1),
        ("Osc A Saw", 1),
        ("Osc A Triangle", 1),
        ("Osc A Sqr", 1),
        ("Sync", 1),
        ("Poly Mod Osc A Destination", 1),
        ("Poly Mod Filter Destination", 1),
        ("LFO Shape", 1),
        ("LFO Speed Range", 1),
        ("LFO Mode Destination", 1),
        ("Keyboard Filter Tracking", 1),
        ("Filter EG Exponential/Linear", 1),
        ("Filter EG Fast/Slow", 1),
        ("Amp EG Exponential/Linear", 1),
        ("Amp EG Fast/Slow", 1),
        ("Unison", 1),
        ("Assigner Priority Mode", 1),
        ("Pitch Bender Semitones", 1),
        ("Pitch Bender Target", 1),
        ("Modulation Wheel Range", 1),
        ("Osc Pitch Mode", 1),
        ("Modulation Delay", 2),
        ("Vibrato Frequency", 2),
        ("Vibrato Amount", 2),
        ("Unison Detune", 2),
        ("Arpeggiator/Sequencer clock", 2),
        ("Modulation Wheel Target", 1),
        ("(padding)", 1),
        ("Voice Pattern (1/6 voices)", 1),
        ("Voice Pattern (2/6 voices)", 1),
        ("Voice Pattern (3/6 voices)", 1),
        ("Voice Pattern (4/6 voices)", 1),
        ("Voice Pattern (5/6 voices)", 1),
        ("Voice Pattern (6/6 voices)", 1),
    ]

    def __init__(self, name: str = "GliGliSysExParser"):
        super().__init__(name)
        self.header = b"\xf0\x00\x61\x16\x01"
        self.format_id = b"\xa5\x16\x61\x00"
        self.format_version = b"\x02"

    @classmethod
    def pop_and_format(
        cls, parameter: tuple[str, int], data: list[int]
    ) -> tuple[str, int]:
        """
        This internal function pops up to two bytes of data from a list and
        converts it to the appropriate format for a given parameter.

        Parameters:
                parameter (tuple): A tuple containing the parameter name and
                                   length in bytes.
                data (list): A list of integers containing parameter data.
        Returns:
                A tuple containing the parameter name and value.
        """
        name, nbytes = parameter
        try:
            lsb, msb = (
                data.pop(0) if len(data) else 0,
                data.pop(0) if len(data) and nbytes == 2 else 0,
            )
        except:
            print(f"Error while reading parameter {name}")
            raise
        value = msb << 8 | lsb
        return (name, value)

    @classmethod
    def unpack(cls, data: bytes) -> list[int]:
        """
        This internal function decodes five 7-bit bytes of raw data packed
        into four full 8-bit bytes.

        Parameters:
                data (list): A list of integers containing raw 7-bit data.
                             The length of the list is required to be a
                             multiple of five.
        Returns:
                A integer list of the unpacked data. The length will be a
                multiple of 4.
        """
        ret = []
        while len(data):
            for shift in range(4):
                ret.append(data[shift] + 128 * (data[4] >> shift & 1))
            data = data[5:]
        return ret

    def can_decode(self, msg: bytes) -> bool:
        """
        This function checks if the parser can decode a given MIDI SysEx dump
        using the header of the data.

        Parameters:
                msg (bytes): Midi SysEx dump

        Returns:
                True if parser can decode dump, False otherwise.
        """
        if msg.startswith(self.header):
            data = self.unpack(msg[len(self.header) : len(self.header) + 10])
            # pop program number
            _ = data.pop(0)
            magic = bytes(data[:5])
            if magic == self.format_id + self.format_version:
                return True
        return False

    def decode(
        self, msg: bytes
    ) -> tuple[int, list[tuple[str, int]], list[int]]:
        """
        This function decodes a MIDI SysEx dump created using
        the original GliGli mod for the Sequential Circuits Prophet-600 analog
        synthesizer.

        Parameter:
                msg (bytes): MIDI SysEx dump

        Returns:
                A tuple containing the program number, a list of parameters,
                and (possibly) a list of remaining integer data that was not or
                could not be decoded.
        """
        parameters = []
        if not msg.startswith(self.header):
            raise ParseError(
                f"Header mismatch: expected {self.header!r},"
                f"got {msg[:len(self.header)]!r}"
            )
        data = self.unpack(msg[len(self.header) :])
        program = data.pop(0)
        magic = bytes(data[:5])
        if magic != self.format_id + self.format_version:
            raise ParseError(
                f"Storage format ID mismatch:"
                f" expected {self.format_id + self.format_version!r}, got {magic!r}"
            )
        data = data[5:]
        for param in self.parameters:
            parameters.append(self.pop_and_format(param, data))
        return (program, parameters, data)
