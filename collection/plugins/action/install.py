"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget roles/params.yml
# NOTE Remember to update README file



from pathlib import Path
from re import match as re_match
from typing import Annotated
from typing import Any
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field
from pydantic import field_validator
from pydantic import model_validator



class InstallWindowsCertificateParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    certificate: Annotated[
        Optional[str],
        Field(None,
              description='Path to the P12 certificate file',
              min_length=1)]

    thumbprint: Annotated[
        Optional[str],
        Field(None,
              description='Path to the certificate thumbprint',
              min_length=1)]


    @field_validator(
        'certificate',
        'thumbprint',
        mode='after')
    @classmethod
    def parse_paths(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Optional[str]:
        """
        Perform advanced validation on the parameters provided.
        """

        if value is None:
            return None

        exists = (
            Path(value)
            .exists())

        if exists is True:
            return str(value)

        raise ValueError(
            'path does not exist'
            ' on the filesystem')



class InstallCertificateParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    windows: Annotated[
        Optional[InstallWindowsCertificateParams],
        Field(None,
              description='Paths to various certificate files')]



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

    certificate: Annotated[
        Optional[InstallCertificateParams],
        Field(None,
              description='Optional certificate for install')]


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
