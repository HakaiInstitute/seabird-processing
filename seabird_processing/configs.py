"""
This module contains the configuration for the seabird commands.

Each command allows passing a text blob, and the module will handle storing a
temporary file before spawning a sub process to process the file. This is an
improvement over the regular command line arguments of SBE because it allows
for the separation of file I/O and data processing, which is important when
files are not stored on the local file system.
"""
import subprocess
from pathlib import Path
from typing import Union

from pydantic import BaseModel, FilePath, DirectoryPath

from seabird_processing.logger import logger
from seabird_processing.settings import load_settings


class _SBEConfig(BaseModel):
    exe_name: str
    batch_name: str
    output_dir: DirectoryPath
    xmlcon: FilePath
    psa: FilePath
    output_file_suffix: str = ""
    input_file_ext: str = ".cnv"
    output_file_ext: str = ".cnv"

    @property
    def _exe_path(self) -> str:
        settings = load_settings()
        return f"{settings.seabird_sbe_path}/{self.exe_name}"

    def output_file_path(self, input_file: Union[Path, str]) -> str:
        """Get the path to the output file.

        Args:
            input_file: The path to the input file
        Returns:
            str: The path to the output file
        """
        input_file_path = Path(input_file)
        output_file_path = (
            Path(self.output_dir)
            / f"{input_file_path.stem}{self.output_file_suffix}{self.output_file_ext}"
        )

        return str(output_file_path)

    def get_exec_str(
        self,
        input_file: Union[Path, str],
        batch_mode: bool = False,
    ) -> str:
        """Get the command to as a string.

        Args:
            input_file: The path to the input file
            batch_mode: Flag to generate the command for a batch config file
        Returns:k
            str: The command to execute
        """
        cmd_path = self._exe_path if not batch_mode else self.batch_name

        exec_str = [
            cmd_path,
            f"/c{self.xmlcon}",
            f"/i{input_file}",
            f"/o{self.output_dir}\\",
            f"/p{self.psa}",
            f"/a{self.output_file_suffix}",
            "/s",
        ]
        return " ".join(exec_str)

    def run(self, input_file: Union[Path, str]) -> str:
        """Run the command on the data.

        Args:
            input_file: The path to the file to run the command on
        Returns:
            str: The path to the output file
        """
        if not Path(self._exe_path).is_file():
            raise RuntimeError(f"Executable {self._exe_path} not found")

        # Execute the seabird command
        try:
            exec_str = self.get_exec_str(input_file).split()
            ps = subprocess.run(
                exec_str,
                timeout=50,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if ps.stdout:
                logger.debug(ps.stdout)
        except Exception as e:
            # TODO: Fix this to be more specific
            if e.stderr:
                logger.error(e.stderr)
            raise e

        return self.output_file_path(input_file)


class AlignCTDConfig(_SBEConfig):
    exe_name: str = "AlignCTDW.exe"
    batch_name: str = "alignctd"


class BinAvgConfig(_SBEConfig):
    exe_name: str = "BinAvgW.exe"
    batch_name: str = "binavg"


class CellTMConfig(_SBEConfig):
    exe_name: str = "CellTMW.exe"
    batch_name: str = "celltm"


class DatCnvConfig(_SBEConfig):
    exe_name: str = "DatCnvW.exe"
    batch_name: str = "datcnv"
    input_file_ext: str = ".hex"


class DeriveConfig(_SBEConfig):
    exe_name: str = "DeriveW.exe"
    batch_name: str = "derive"


class DeriveTEOS10Config(_SBEConfig):
    exe_name: str = "DeriveTEOS_10W.exe"
    batch_name: str = "deriveteos10"


class FilterConfig(_SBEConfig):
    exe_name: str = "FilterW.exe"
    batch_name: str = "filter"


class LoopEditConfig(_SBEConfig):
    exe_name: str = "LoopEditW.exe"
    batch_name: str = "loopedit"


class SeaPlotConfig(_SBEConfig):
    exe_name: str = "SeaPlotW.exe"
    batch_name: str = "seaplot"


class SectionConfig(_SBEConfig):
    exe_name: str = "SectionW.exe"
    batch_name: str = "section"


class WildEditConfig(_SBEConfig):
    exe_name: str = "WildEditW.exe"
    batch_name: str = "wildedit"
