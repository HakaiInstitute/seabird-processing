# Seabird-SBE _beta_

Python bindings for executing Seabird SBE processing tools.

## Description

This library contains an API for executing seabird SBE processing modules on Seabird data files (hex and cnv). The modules all accept text as input which allows for more convenient access to the command line functions which require file input. Under the hood, this library simply saves temporary files which are then processed through SBE, and then returned as text information. Default locations for xmlcon and psa files can be defined so that each processing method uses those files by default.

The library exports a single class, SBE which on instantiation saves the locations of default file and directory locations. See [Example usage](#Example usage) for all constructor parameters.

The SBE class contains the following methods which correspond to seabird SBE processing modules:

```python
sbe.align_ctd(data, [xmlcon], [psa]):

sbe.bin_avg(data, [xmlcon], [psa]):

sbe.cell_thermal_mass(data, [xmlcon], [psa]):

sbe.dat_cnv(data, [xmlcon], [psa]):

sbe.derive(data, [xmlcon], [psa]):

sbe.derive_teos10(data, [xmlcon], [psa]):

sbe.filter(data, [xmlcon], [psa]):

sbe.loop_edit(data, [xmlcon], [psa]):

sbe.sea_plot(data, [xmlcon], [psa]):

sbe.section(data, [xmlcon], [psa]):

sbe.wild_edit(data, [xmlcon], [psa]):
```

### Example usage

Example with default defined config file locations:

```python
from seabirdSBE import SBE
import os

# Create instance of SBE functions with config files
cwd = os.path.dirname(__file__)
sbe = SBE(
    bin='c:\Program Files (x86)\Sea-Bird\SBEDataProcessing-Win32', #default
    temp_path=os.getenv('TEMP'), #default
    xmlcon=os.join(cwd, 'xmlcon', '19-7467.xmlcon'),
    psa_align_ctd=os.join(cwd, 'psa', 'AlignCTD.psa'),
    psa_bin_avg=os.join(cwd, 'psa', 'BinAvg.psa'),
    psa_cell_thermal_mass=os.join(cwd, 'psa', 'CellTM.psa'),
    psa_dat_cnv=os.join(cwd, 'psa', 'DatCnv.psa'),
    psa_derive=os.join(cwd, 'psa', 'Derive.psa'),
    psa_derive_teos10=os.join(cwd, 'psa', 'DeriveTEOS_10.psa'),
    psa_filter=os.join(cwd, 'psa', 'Filter.psa'),
    psa_loop_edit=os.join(cwd, 'psa', 'LoopEdit.psa'),
    psa_sea_plot=os.join(cwd, 'psa', 'SeaPlot.psa'),
    psa_section=os.join(cwd, 'psa', 'Section.psa'),
    psa_wild_edit=os.join(cwd, 'psa', 'WildEdit.psa')
)

# Execute a SBE method on some file data
with open('./seabird_data_file.hex', 'r') as hexfile:
  cnvfile = sbe.dat_cnv(hexfile)

  print(cnvfile)

  # * Sea-Bird SBE19plus  Data File:
  # * FileName = C:\Users\Jimbo\Desktop\seabird_data_file.hex
  # * Software version 2.4.1
  # ...
```

Example with on-the-fly defined config file locations:

```python
from seabirdSBE import SBE
import os

# Create instance of SBE functions with config files
cwd = os.path.dirname(__file__)
sbe = SBE()  # Using default bin and temp locations here

# Execute a SBE method on some file data
with open('./seabird_data_file.hex', 'r') as hexfile:
  xmlcon = os.join(cwd, 'xmlcon', '19-7467.xmlcon')
  psa_dat_cnv=os.join(cwd, 'psa', 'DatCnv.psa')

  cnvfile = sbe.dat_cnv(hexfile, xmlcon, psa_dat_cnv)

  print(cnvfile)

  # * Sea-Bird SBE19plus  Data File:
  # * FileName = C:\Users\Jimbo\Desktop\seabird_data_file.hex
  # * Software version 2.4.1
  # ...
```

### Installation / Requirements

An installation of the [Seabird Processing Suite](http://www.seabird.com/software/software) is required to run these modules since they simply provide a convenient abstraction of the command line options built into the software. The Seabird software itself requires an installation of Windows 7+.

To install this tool in your current python environment do `pip install -i https://testpypi.python.org/pypi seabirdSBE`

### Copyright and Licensing Information

_Read LICENSE_

### Authors

Taylor Denouden at the Hakai Institute

### Bugs / Feature requests

Please file bug reports and feature requests on Github. Pull Requests to add functionality or fix bugs are also more than welcome.
