[![PyPI versio](https://img.shields.io/pypi/v/p600syx)](https://pypi.org/project/p600syx/)
[![PyPi format](https://img.shields.io/pypi/format/p600syx)](https://pypi.org/project/p600syx/)
[![PyPI license](https://img.shields.io/pypi/l/p600syx)](https://pypi.org/project/p600syx/)
[![PyPi weekly downloads](https://img.shields.io/pypi/dw/p600syx)](https://pypi.org/project/p600syx/)

## p600syx

This is a python modules for handling MIDI SysEx patch dumps for the
Sequential Circuits Prophet-600 analog synthesizer.

The following formats are supported:

* The original patch format documented in the owner's manual
* The custom format introduced by GliGli ([documentation](https://github.com/gligli/p600fw/blob/master/documentation/sysex_format.ods))
* The updated dump formats by Imogen (versions [7]() and [8]())

Currently, it is possible to dump SysEx data using the script `p600_syxdump`.
