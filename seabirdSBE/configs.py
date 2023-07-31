"""
This module contains the configuration for the seabird commands.

Each command allows passing a text blob, and the module will handle storing a
temporary file before spawning a sub process to process the file. This is an
improvement over the regular command line arguments of SBE because it allows
for the separation of file I/O and data processing, which is important when
files are not stored on the local file system.
"""

import tempfile
from pathlib import Path
from typing import Union

from pydantic import BaseModel, FilePath, DirectoryPath

from seabirdSBE.sbe_exec import _sbe_exec
from seabirdSBE.settings import load_settings


class _SBEConfig(BaseModel):
    exe_name: str
    xmlcon: FilePath
    psa: FilePath
    input_file_suffix: str = ".cnv"
    output_file_suffix: str = ".cnv"

    @property
    def _exe_path(self) -> str:
        settings = load_settings()
        return f"{settings.seabird_sbe_path}/{self.exe_name}"

    def run(self, in_path: Union[Path, str]) -> str:
        """Run the command on the data.

        Args:
            in_path: The path to the file to run the command on
        Returns:
            str: The processed data
        """
        # Create temporary files and paths from data
        with tempfile.TemporaryDirectory() as out_dir:
            out_path = Path(out_dir) / Path(in_path).stem
            out_path = out_path.with_suffix(self.output_file_suffix)

            # Execute the seabird command
            _sbe_exec(self._exe_path, in_path, out_dir, self.xmlcon, self.psa)

            # Read the result
            with open(out_path, "r") as out_file:
                result = out_file.read()

            # Return content
        return result


class _FuncConfig(_SBEConfig):
    def __init__(self,
                 xmlcon: FilePath,
                 psa: FilePath,
                 output_dir: DirectoryPath,
                 **kwargs
        ):
        super().__init__(xmlcon=xmlcon, psa=psa, **kwargs)


class AlignCTDConfig(_FuncConfig):
    exe_name: str = "AlignCTDW.exe"


class BinAvgConfig(_FuncConfig):
    exe_name: str = "BinAvgW.exe"


class CellTMConfig(_FuncConfig):
    exe_name: str = "CellTMW.exe"


class DatCnvConfig(_FuncConfig):
    exe_name: str = "DatCnvW.exe"
    input_file_suffix = ".hex"


class DeriveConfig(_FuncConfig):
    exe_name: str = "DeriveW.exe"


class DeriveTEOS10Config(_FuncConfig):
    exe_name: str = "DeriveTEOS_10W.exe"


class FilterConfig(_FuncConfig):
    exe_name: str = "FilterW.exe"


class LoopEditConfig(_FuncConfig):
    exe_name: str = "LoopEditW.exe"


class SeaPlotConfig(_FuncConfig):
    exe_name: str = "SeaPlotW.exe"


class SectionConfig(_FuncConfig):
    exe_name: str = "SectionW.exe"


class WildEditConfig(_FuncConfig):
    exe_name: str = "WildEditW.exe"
