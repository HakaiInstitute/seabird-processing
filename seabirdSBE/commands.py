"""
This module contains the commands that can be executed on data.

Each command allows passing a text blob, and the module will handle storing a
temporary file before spawning a sub process to process the file. This is an
improvement over the regular command line arguments of SBE because it allows
for the separation of file I/O and data processing, which is important when
files are not stored on the local file system.
"""

from pathlib import Path
from typing import Union

from seabirdSBE.configs import AlignCTDConfig, BinAvgConfig, CellTMConfig, \
    DatCnvConfig, DeriveConfig, DeriveTEOS10Config, FilterConfig, LoopEditConfig, \
    SeaPlotConfig, SectionConfig, WildEditConfig


def sbe_align_ctd(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Align CTD module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return AlignCTDConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_bin_avg(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Bin Average.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return BinAvgConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_cell_thermal_mass(data: str, xmlcon: Union[Path, str] = None,
                          psa: Union[Path, str] = None):
    """Process data through the SBE Cell Thermal Mass.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return CellTMConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_dat_cnv(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Data Conversion.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return DatCnvConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_derive(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Derive.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return DeriveConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_derive_teos10(data: str, xmlcon: Union[Path, str] = None,
                      psa: Union[Path, str] = None):
    """Process data through the SBE Derive TEOS-10.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return DeriveTEOS10Config(xmlcon=xmlcon, psa=psa).run(data)


def sbe_filter(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Filter.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return FilterConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_loop_edit(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Loop Edit.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return LoopEditConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_sea_plot(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Sea Plot.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return SeaPlotConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_section(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Section.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return SectionConfig(xmlcon=xmlcon, psa=psa).run(data)


def sbe_wild_edit(data: str, xmlcon: Union[Path, str] = None, psa: Union[Path, str] = None):
    """Process data through the SBE Wild Edit.exe module.

    Args:
        data (str): The data to execute this module on
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    return WildEditConfig(xmlcon=xmlcon, psa=psa).run(data)
