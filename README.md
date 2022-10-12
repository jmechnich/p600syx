[![PyPI versio](https://img.shields.io/pypi/v/p600syx)](https://pypi.org/project/p600syx/)
[![PyPi format](https://img.shields.io/pypi/format/p600syx)](https://pypi.org/project/p600syx/)
[![PyPI license](https://img.shields.io/pypi/l/p600syx)](https://pypi.org/project/p600syx/)
[![PyPi weekly downloads](https://img.shields.io/pypi/dw/p600syx)](https://pypi.org/project/p600syx/)

## p600syx

This is a collection of python modules for handling MIDI SysEx patch
dumps for the Sequential Circuits Prophet-600 analog synthesizer.

The following formats are supported:

* The original patch format documented in the owner's manual
* The custom format introduced by GliGli ([documentation](https://github.com/gligli/p600fw/blob/master/documentation/sysex_format.ods))
* The updated dump formats by Imogen (versions [7]() and [8]())

Currently, it is possible to dump SysEx data using the script `p600_syxdump`.

### Installation and usage

The easiest way is to install the software from https://pypi.org using `pip`:

```
pip install p600syx
```

After installation, the script can be used as follows:

```
usage: p600_syxdump [-h] [-d] [-p PROGRAM] [infile]

Print preset contents of Prophet-600 MIDI SysEx dumps.

positional arguments:
  infile                input sysex file. If no file is given, the script will read from
                        standard input.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           turn on debug output
  -p PROGRAM, --program PROGRAM
                        filter for program number
```
