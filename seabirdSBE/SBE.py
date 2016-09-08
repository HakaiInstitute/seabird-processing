"""This module provides an abstraction of Seabird SBE software exection.

Each command allows passing a text blob, and the module will handle storing a
temporary file before spawning a sub process to process the file. This is an
improvement over the regular command line arguments of SBE because it allows
for the separation of file I/O and data processing, which is important when
files are not stored on the local file system.

Written by: Taylor Denouden
Last updated: September 2016

Copyright (c) 2016 Hakai Institute and Contributors All Rights Reserved.
"""

from __future__ import print_function
from hashlib import sha1
import os
import subprocess


class SBE(object):
    """SBE processing class.

    Allows for the defining of global variables at instantiation so that
    environment defaults may be used across different machine installations.
    """
    def __init__(self, *args, **kwargs):
        """constructor kwargs available:
            bin: The bin directory containing all SBE functions
            temp_path: Temp directory
            xmlcon
            psa_align_ctd, psa_bin_avg, psa_cell_thermal_mass
            psa_dat_cnv, psa_derive, psa_derive_teos10
            psa_filter, psa_loop_edit, psa_sea_plot, psa_section
            psa_wild_edit
        """
        super(SBE, self).__init__()
        # Path to SBE installation
        dflt_bin = 'c:\Program Files (x86)\Sea-Bird\SBEDataProcessing-Win32'
        self._sbe_path = kwargs.get('bin', dflt_bin)

        # Temporary directory to store generated files
        self._temp_dir = kwargs.get('temp_path', os.getenv('TEMP'))

        # Default config files
        self._xmlcon = kwargs.get('xmlcon')
        self._psa_align_ctd = kwargs.get('psa_align_ctd')
        self._psa_bin_avg = kwargs.get('psa_bin_avg')
        self._psa_cell_thermal_mass = kwargs.get('psa_cell_thermal_mass')
        self._psa_dat_cnv = kwargs.get('psa_dat_cnv')
        self._psa_derive = kwargs.get('psa_derive')
        self._psa_derive_teos10 = kwargs.get('psa_derive_teos10')
        self._psa_filter = kwargs.get('psa_filter')
        self._psa_loop_edit = kwargs.get('psa_loop_edit')
        self._psa_sea_plot = kwargs.get('psa_sea_plot')
        self._psa_section = kwargs.get('psa_section')
        self._psa_wild_edit = kwargs.get('psa_wild_edit')

    def _write_temp_file(self, content, ext='.txt'):
        """Save in memory file content to temp dir and return path."""
        # Create temp file path use hash of file content
        path = os.path.join(self._temp_dir, sha1(content).hexdigest() + ext)

        # Create the temp file
        with open(path, 'w') as f:
            f.write(content)

        # Return path name of temp file
        return path

    def _sbe_cmd(self, cmd, in_file, out_dir, xmlcon, psa):
        """Execute an SBE module via comand args."""
        # Check that cmd is valid
        if not os.path.exists(cmd):
            raise RuntimeError('Executable {} not found'.format(cmd))

        # see pp 136
        # seabird.com/sites/default/files/documents/SBEDataProcessing_7.26.0.pdf
        exec_str = '"{cmd}" /c"{c}" /i"{i}" /o"{o}" /p"{p}" /s'.format(
            cmd=cmd,
            c=xmlcon,
            i=in_file,
            o=out_dir,
            p=psa
        )

        # Run command, throw error if failure occurs
        subprocess.check_call(exec_str)

    def align_ctd(self, data, xmlcon=None, psa=None):
        """Execute the SBE Align CTD module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_align_ctd

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\AlignCTDW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def bin_avg(self, data, xmlcon=None, psa=None):
        """Execute the SBE Bin Average module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_bin_avg

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\BinAvgW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def cell_thermal_mass(self, data, xmlcon=None, psa=None):
        """Execute the SBE Cell Thermal Mass module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_cell_thermal_mass

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\CellTMW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def dat_cnv(self, data, xmlcon=None, psa=None):
        """Execute the SBE Data Conversion module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_dat_cnv

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.hex')

        # Execute the seabird command
        cmd = '{}\DatCnvW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = os.path.splitext(in_file)[0] + '.cnv'
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(in_file)
        os.remove(out_file)

        # Return content
        return result

    def derive(self, data, xmlcon=None, psa=None):
        """Execute the SBE Derive module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_derive

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\DeriveW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def derive_teos10(self, data, xmlcon=None, psa=None):
        """Execute the SBE Derive TEOS-10 module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_derive_teos10

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\DeriveTEOS_10W.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def filter(self, data, xmlcon=None, psa=None):
        """Execute the SBE Filter module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_filter

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\FilterW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def loop_edit(self, data, xmlcon=None, psa=None):
        """Execute the SBE Loop Edit module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_loop_edit

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\LoopEditW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def sea_plot(self, data, xmlcon=None, psa=None):
        """Execute the SBE Sea Plot module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_sea_plot

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\SeaPlotW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def section(self, data, xmlcon=None, psa=None):
        """Execute the SBE Section module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_section

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\SectionW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result

    def wild_edit(self, data, xmlcon=None, psa=None):
        """Execute the SBE Wild Edit module."""
        # Set to xmlcon and psa paths to instance default if not defined as arg
        xmlcon = xmlcon or self._xmlcon
        psa = psa or self._psa_wild_edit

        # Create temporary files and paths from data
        in_file = self._write_temp_file(data, '.cnv')

        # Execute the seabird command
        cmd = '{}\WildEditW.exe'.format(self._sbe_path)
        self._sbe_cmd(cmd, in_file, os.path.dirname(in_file), xmlcon, psa)

        # Return file content
        out_file = in_file
        f = open(out_file, 'r')
        result = f.read()
        f.close()

        # Cleanup
        os.remove(out_file)

        # Return content
        return result
