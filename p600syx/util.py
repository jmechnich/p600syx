import argparse
import os
from typing import Any, Optional, Set

from .error import MIDIError


class SysEx:
    SYSEX_ID_0 = 0x00
    SYSEX_ID_1 = 0x61
    SYSEX_ID_2 = 0x16

    SYSEX_COMMAND_PATCH_DUMP = 1
    SYSEX_COMMAND_PATCH_DUMP_REQUEST = 2
    SYSEX_COMMAND_UPDATE_FW = 0x6B

    SYSEX_SUBID1_BULK_TUNING_DUMP = 0x08
    SYSEX_SUBID2_BULK_TUNING_DUMP_REQUEST = 0x00
    SYSEX_SUBID2_BULK_TUNING_DUMP = 0x01


def get_config(
    args: argparse.Namespace, configfiles: list[str] = []
) -> dict[str, str]:
    config = {}
    for configfile in configfiles:
        if not os.path.exists(configfile):
            continue
        with open(configfile) as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith("#"):
                    continue
                k, v = line.split("=")
                config[k.lower()] = v

    config.update(dict(vars(args)))
    return config


def get_port(ports: Set[Any], port: Optional[str] = None) -> Optional[str]:
    selected_port = None
    if port:
        if port in ports:
            selected_port = port
        else:
            raise MIDIError(f"Selected port {port!r} is not available")
    elif len(ports) > 1:
        raise MIDIError(
            f"More than one MIDI port found and none selected. Available: {ports}"
        )
    elif len(ports) == 0:
        raise MIDIError(f"No MIDI ports found")
    else:
        selected_port = ports.pop()

    return selected_port
