"""
Settings for the seabird-sbe package.

This module contains the settings for the seabird-sbe package. These settings
are loaded from the .env file in the root of the package. The settings are
loaded using the pydantic_settings package, which allows for the settings to
be validated and loaded as an object.
"""

from functools import lru_cache

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="sbe_"
    )

    bin_dir: DirectoryPath = r"C:\Program Files (x86)\Sea-Bird\SBEDataProcessing-Win32"
    command_timeout: int = 60 * 2  # 2 minutes


@lru_cache()
def load_settings() -> _Settings:
    """Load settings from .env file or env variables and return them as an object."""
    return _Settings()
