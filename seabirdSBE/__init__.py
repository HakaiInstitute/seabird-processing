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

from SBE import SBE

__all__ = ["SBE"]
