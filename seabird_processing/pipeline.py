"""
This module contains the Pipeline class.

The Pipeline class allows for the chaining of SBE commands to run on data. This
is useful for running multiple commands on the same data without having to
write the data to disk between each command.
"""
from typing import Iterable

from seabird_processing.configs import _SBEConfig


class Pipeline(object):
    """A pipeline of SBE commands to run on data.

    This class allows for the chaining of SBE commands to run on data. This is
    useful for running multiple commands on the same data without having to
    write the data to disk between each command.
    """

    def __init__(self, stages: Iterable[_SBEConfig]):
        """
        Args:
            stages: (Iterable[_SBECommand]) The stages to run on the data
        Returns:
            Pipeline: The pipeline object
        """
        super().__init__()
        self.stages = stages

    def __call__(self, data: str):
        """Run the pipeline on the data.

        Args:
            data (str): The data to run the pipeline on
        Returns:
            str: The processed data
        """
        for config in self.stages:
            data = config.run(data)
        return data
