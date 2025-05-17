"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml



from pathlib import Path
from re import match as re_match
from typing import Annotated
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field
from pydantic import model_validator



class InstallParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    source: Annotated[
        str,
        Field(...,
              description='Where source install is located',
              min_length=1)]

    checksum: Annotated[
        Optional[str],
        Field(None,
              description='Expected hash value of the ISO',
              min_length=1)]

    cached: Annotated[
        Optional[str],
        Field(None,
              description='File name when downloading file',
              min_length=1)]


    @model_validator(mode='after')
    def check_cached(
        # NOCVR
        self,
    ) -> 'InstallParams':
        """
        Perform advanced validation on the parameters provided.
        """

        source = self.source
        cached = self.cached

        download = re_match(
            'https?:', source)

        if download is None:

            exists = (
                Path(source)
                .exists())

            if exists is True:
                return self

            raise ValueError(
                'source path does not '
                'exist on filesystem')

        if cached is not None:
            return self

        raise ValueError(
            'cached is required '
            'when source is URL')
