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

from seabird_processing.configs import (
    AlignCTDConfig,
    BinAvgConfig,
    CellTMConfig,
    DatCnvConfig,
    DeriveConfig,
    DeriveTEOS10Config,
    FilterConfig,
    LoopEditConfig,
    SeaPlotConfig,
    SectionConfig,
    WildEditConfig,
)


def align_ctd(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Align CTD module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = AlignCTDConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def bin_avg(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Bin Average.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = BinAvgConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def cell_thermal_mass(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Cell Thermal Mass.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = CellTMConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def dat_cnv(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Data Conversion.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = DatCnvConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def derive(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Derive.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = DeriveConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def derive_teos10(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Derive TEOS-10.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = DeriveTEOS10Config(output_dir=output_dir, xmlcon=xmlcon, psa=psa)
    return config.run(input_file)


def filter_(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Filter.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = FilterConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def loop_edit(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Loop Edit.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = LoopEditConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def sea_plot(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Sea Plot.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = SeaPlotConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def section(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Section.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = SectionConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)


def wild_edit(
    input_file: Union[Path, str],
    output_dir: Union[Path, str],
    xmlcon: Union[Path, str] = None,
    psa: Union[Path, str] = None,
    **kwargs,
):
    """Process data through the SBE Wild Edit.exe module.

    Args:
        input_file: The path to the input file to run the command on
        output_dir: The directory to store the output file in
        xmlcon (str | Path): The xmlcon file to use. Overrides any default
        psa (str | Path): The psa file to use. Overrides any default psa
    Returns:
        str: The processed data
    """
    config = WildEditConfig(output_dir=output_dir, xmlcon=xmlcon, psa=psa, **kwargs)
    return config.run(input_file)
