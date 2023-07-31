"""This module provides an abstraction of Seabird SBE software execution.

Each command allows passing a text blob, and the module will handle storing a
temporary file before spawning a sub process to process the file. This is an
improvement over the regular command line arguments of SBE because it allows
for the separation of file I/O and data processing, which is important when
files are not stored on the local file system.

Written by: Taylor Denouden
Last updated: September 2016

Copyright (c) 2016 Hakai Institute and Contributors All Rights Reserved.
"""

from seabird_sbe import configs
from seabird_sbe.commands import (
    sbe_align_ctd,
    sbe_bin_avg,
    sbe_cell_thermal_mass,
    sbe_dat_cnv,
    sbe_derive,
    sbe_derive_teos10,
    sbe_filter,
    sbe_loop_edit,
    sbe_sea_plot,
    sbe_section,
    sbe_wild_edit,
)
from seabird_sbe.pipeline import Pipeline

__all__ = [
    "configs",
    "sbe_align_ctd",
    "sbe_bin_avg",
    "sbe_cell_thermal_mass",
    "sbe_dat_cnv",
    "sbe_derive",
    "sbe_derive_teos10",
    "sbe_filter",
    "sbe_loop_edit",
    "sbe_sea_plot",
    "sbe_section",
    "sbe_wild_edit",
    "Pipeline",
]
