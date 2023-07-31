"""
Module for executing SBE modules via command line.

This module contains the _sbe_exec function, which is used to execute SBE
modules via command line. This function is used by the commands module to
execute SBE modules on data.
"""
import subprocess
from pathlib import Path

from seabirdSBE.logger import logger


def _sbe_exec(
    exe_path: str,
    in_file: str,
    out_dir: str,
    xmlcon: str,
    psa: str,
):
    """Execute an SBE module via command args.

    Try to process the file through a SBE module. Timeout after 50s to
    prevent hangs on files where errors are thrown in the SBE gui.

    Args:
        exe_path: (str | Path) The full path to the SBE.exe to execute
        in_file: (str | Path) The path to the file to execute the module on
        out_dir: (str | Path) The path to the directory to save the output file
        xmlcon: (str | Path) The path to the xmlcon file to use
        psa: (str | Path) The path to the psa file to use
    """
    # Check that cmd is valid
    if not Path(exe_path).is_file():
        raise RuntimeError(f"Executable {exe_path} not found")

    # see pp 136
    # seabird.com/sites/default/files/documents/SBEDataProcessing_7.26.0.pdf
    exec_str = [
        exe_path,
        f"/c{xmlcon}",
        f"/i{in_file}",
        f"/o{out_dir}\\",
        f"/p{psa}",
        "/s",
    ]
    logger.debug(" ".join(exec_str))

    try:
        # Run command, throw error if failure occurs
        ps = subprocess.run(
            exec_str, timeout=50, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if ps.stdout:
            logger.debug(ps.stdout)
    except Exception as e:
        if e.stderr:
            logger.error(e.stderr)
        raise e
