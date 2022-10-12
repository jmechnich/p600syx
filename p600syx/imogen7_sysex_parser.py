"""
This module contains the parser for decoding MIDI SysEx dumps created using
the Imogen mod (storage version 7) for the Sequential Circuits Prophet-600
analog synthesizer.
"""
from .gligli_sysex_parser import GliGliSysExParser


class Imogen7SysExParser(GliGliSysExParser):
    """
    This class implements the decoding of MIDI SysEx dumps created using
    the Imogen mod (storage version 7) for the Sequential Circuits Prophet-600
    analog synthesizer.
    """

    parameters = [
        ("Frequency A", 2),
        ("Volume A", 2),
        ("PWA", 2),
        ("Frequency B", 2),
        ("Volume B", 2),
        ("PWB", 2),
        ("Frequency Fine B", 2),
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
        ("Poly Mod Envelope Amount", 2),
        ("Poly Mod OSC B", 2),
        ("LFO Frequency", 2),
        ("LFO Amount", 2),
        ("Glide", 2),
        ("Amp Velocity", 2),
        ("Filter Velocity", 2),
        ("Saw A", 1),
        ("Tri A", 1),
        ("SQR A", 1),
        ("Saw B", 1),
        ("Tri B", 1),
        ("SQR B", 1),
        ("Sync", 1),
        ("Poly Mod Frequency A", 1),
        ("Poly Mod Filter", 1),
        ("LFO Shape", 1),
        ("LFO Shift", 1),
        ("LFO Targets", 1),
        ("Tracking Shift", 1),
        ("Filter Envelope Shape", 1),
        ("Filter Envelope Speed", 1),
        ("Amp Envelope Shape", 1),
        ("Amp Envelope Speed", 1),
        ("Unison", 1),
        ("Assigner Priority", 1),
        ("Bender Semitones", 1),
        ("Bender Target", 1),
        ("Mod Wheel Shift", 1),
        ("Chromatic Pitch", 1),
        ("Modulation Delay", 2),
        ("Vibrato Frequency", 2),
        ("Vibrato Amount", 2),
        ("Unison Detune", 2),
        ("(unused, arp/seq clock slot)", 2),
        ("Modulation Wheel Target", 1),
        ("Vibrato Target", 1),
        ("Voice Pattern (1/6 voices)", 1),
        ("Voice Pattern (2/6 voices)", 1),
        ("Voice Pattern (3/6 voices)", 1),
        ("Voice Pattern (4/6 voices)", 1),
        ("Voice Pattern (5/6 voices)", 1),
        ("Voice Pattern (6/6 voices)", 1),
        ("Tuning per Note  (1/12)", 2),
        ("Tuning per Note  (2/12)", 2),
        ("Tuning per Note  (3/12)", 2),
        ("Tuning per Note  (4/12)", 2),
        ("Tuning per Note  (5/12)", 2),
        ("Tuning per Note  (6/12)", 2),
        ("Tuning per Note  (7/12)", 2),
        ("Tuning per Note  (8/12)", 2),
        ("Tuning per Note  (9/12)", 2),
        ("Tuning per Note (10/12)", 2),
        ("Tuning per Note (11/12)", 2),
        ("Tuning per Note (12/12)", 2),
    ]

    def __init__(self) -> None:
        super().__init__("Imogen7SysExParser")
        self.format_version = b"\x07"
