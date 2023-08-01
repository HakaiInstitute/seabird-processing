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

# Execute a SBE method on some file data
with open('./seabird_data_file.hex', 'r') as hexfile:
    hexdata = hexfile.read()

cnvfile = sbe_dat_cnv(hexdata, xmlcon, './psa/DatCnv.psa')
print(cnvfile)

# * Sea-Bird SBE19plus  Data File:
# * FileName = C:\Users\Jimbo\Desktop\seabird_data_file.hex
# * Software version 2.4.1
# ...

# Continue executing SBE methods on the same file data
filtered = sbe_filter(cnvfile, xmlcon, './psa/AlignCTD.psa')
# ...
```

### Pipeline processing

```python
from seabird_processing import Pipeline, configs

xmlcon = './path/to/xmlcon/12-3456.xmlcon'

# Create a pipeline with some config files
pipeline = Pipeline([    
    configs.DatCnvConfig(xmlcon, './path/to/DatCnv.psa'),
    configs.FilterConfig(xmlcon, './path/to/Filter.psa'),
    configs.AlignCTDConfig(xmlcon, './path/to/AlignCTD.psa'),
    configs.CellTMConfig(xmlcon, './path/to/CellTM.psa'),
    configs.LoopEditConfig(xmlcon, './path/to/LoopEdit.psa'),
    configs.DeriveConfig(xmlcon, './path/to/Derive.psa'),
    configs.DeriveTEOS10Config(xmlcon, './path/to/DeriveTEOS_10.psa'),
    configs.BinAvgConfig(xmlcon, './path/to/BinAvg.psa'),
])

# Execute the entire pipeline on a file
with open('./seabird_data_file.hex', 'r') as hexfile:
    hexdata = hexfile.read()

processed_data = pipeline(hexdata)

# Write the data to disk, upload to a database, etc.
with open('./processed_data.cnv', 'w') as f:
    f.write(processed_data)
```

### Copyright and Licensing Information

See [LICENSE](./LICENSE) for details.

### Bugs / Feature requests

Please file bug reports and feature requests on GitHub. We also welcome pull requests
to add functionality or fix bugs!
