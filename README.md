# Seabird-SBE

Python bindings for executing Seabird SBE processing tools.

## Description

This library contains an API for executing seabird SBE processing modules on Seabird
data files (hex and cnv). The modules all accept text as input which allows for more
convenient access to the command line functions which would normally require a file path
as input. Under the hood, this library simply saves temporary files which are then
processed through SBE, read into memory, and returned as in-memory text.

## Installation

### Pre-requisites

An installation of
the [Seabird Processing Suite](http://www.seabird.com/software/software) is required to
run these modules since they simply provide an abstraction of the command line tools
provided by Seabird.

### Install with pip

To install this tool in your current python environment do:

```pip install seabirdSBE```

Configure the tool with the location of your Seabird Processing Suite installation by
setting the `SEABIRD_SBE_PATH` environment variable. For example, if you installed the
software to `C:\Program Files (x86)\Seabird\SBEDataProcessing-Win32` then you would set
the environment
variable `SEABIRD_SBE_PATH=C:\Program Files (x86)\Seabird\SBEDataProcessing-Win32\`.
By default, it is assumed that the software is installed
to `C:\Program Files (x86)\Seabird\SBEDataProcessing-Win32`.

## Usage

There are two ways to use this library. The first is to use individual functions which
correspond one-to-one with the SBE processing modules. The second is to use
the `Pipeline`
class which allows you to chain together multiple processing modules.

### Command line functions

```python
from seabird_processing import sbe_dat_cnv, sbe_filter

xmlcon = './xmlcon/19-7467.xmlcon'

cnvfile = sbe_dat_cnv('./seabird_data_file.hex', './output/dir', xmlcon, './psa/DatCnv.psa')
filtered = sbe_filter(cnvfile, './output/dir', xmlcon, './psa/AlignCTD.psa')
# ...
```

### Pipeline processing

```python
from seabird_processing import Batch, configs

xmlcon = './path/to/xmlcon/12-3456.xmlcon'

# Create a pipeline with some config files
pipeline = Batch([
    configs.DatCnvConfig(
        output_dir="./datcnv", output_file_suffix="_datcnv",
        xmlcon=xmlcon, psa='./path/to/DatCnv.psa'),
    configs.FilterConfig(
        output_dir="./filter", output_file_suffix="_filter",
        xmlcon=xmlcon, psa='./path/to/Filter.psa'),
    configs.AlignCTDConfig(
        output_dir="./alignctd", output_file_suffix="_alignctd",
        xmlcon=xmlcon, psa='./path/to/AlignCTD.psa'),
    configs.CellTMConfig(
        output_dir="./celltm", output_file_suffix="_celltm",
        xmlcon=xmlcon, psa='./path/to/CellTM.psa'),
    configs.LoopEditConfig(
        output_dir="./loopedit", output_file_suffix="_loopedit",
        xmlcon=xmlcon, psa='./path/to/LoopEdit.psa'),
    configs.DeriveConfig(
        output_dir="./derive", output_file_suffix="_derive",
        xmlcon=xmlcon, psa='./path/to/Derive.psa'),
    configs.DeriveTEOS10Config(
        output_dir="./deriveteos10", output_file_suffix="_deriveteos10",
        xmlcon=xmlcon, psa='./path/to/DeriveTEOS_10.psa'),
    configs.BinAvgConfig(
        output_dir="./binavg", output_file_suffix="_binavg",
        xmlcon=xmlcon, psa='./path/to/BinAvg.psa'),
])

pipeline("./*.hex")
```

### Copyright and Licensing Information

See [LICENSE](./LICENSE) for details.

### Bugs / Feature requests

Please file bug reports and feature requests on GitHub. We also welcome pull requests
to add functionality or fix bugs!
