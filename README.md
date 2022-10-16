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
* The updated dump formats by Imogen (versions
  [7](https://github.com/image-et-son/p600fw/blob/master/syxmgmt/storage_7.spec)
  and
  [8](https://github.com/image-et-son/p600fw/blob/master/syxmgmt/storage_8.spec))

The available executable programs are:

* `p600_decode` - decode patch data to human readable form
* `p600_recv` - receive patch data via MIDI
* `p600_send` - send patch and other SysEx data (i.e. firmware files) via MIDI

### Installation and usage

The easiest way is to install the software from https://pypi.org using `pip`:

```
pip install p600syx
```

After installing the package, check `p600_SCRIPTNAME -h` for further usage instructions.
