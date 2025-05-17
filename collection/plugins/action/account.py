"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml



from typing import Annotated
from typing import Any
from typing import Literal
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field
from pydantic import field_validator



class AccountPasshashParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    linux: Annotated[
        Optional[str],
        Field(None,
              description='Password hash value for account',
              min_length=1)]

    openbsd: Annotated[
        Optional[str],
        Field(None,
              description='Password hash value for account',
              min_length=1)]



class AccountParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Name for the account on system',
              min_length=1)]

    uid: Annotated[
        Optional[str],
        Field(None,
              description='Unique identifier for the account',
              min_length=1)]

    gid: Annotated[
        Optional[str],
        Field(None,
              description='Primary group for the account',
              min_length=1)]

    password: Annotated[
        Optional[str],
        Field(None,
              description='Password when creating account',
              min_length=1)]

    passhash: Annotated[
        Optional[AccountPasshashParams],
        Field(None,
              description='Password hash value for account')]

    display: Annotated[
        Optional[str],
        Field(None,
              description='Friendly display name for account',
              min_length=1)]

    groups: Annotated[
        Optional[list[str]],
        Field(None,
              description='Additional groups for the account',
              min_length=1)]

    home: Annotated[
        Optional[str],
        Field(None,
              description='Optional path of the home directory',
              min_length=5)]

    shell: Annotated[
        Optional[str],
        Field(None,
              description='Optional path of shell executable',
              min_length=5)]

    system: Annotated[
        bool,
        Field(False,
              description='Determine if is a system account')]

    state: Annotated[
        Literal['present', 'absent'],
        Field('present',
              description='Determine whether account present')]

    initial: Annotated[
        bool,
        Field(False,
              description='Define the account in unattended')]


    @field_validator(
        'groups',
        mode='before')
    @classmethod
    def parse_groups(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if isinstance(value, str):
            return [value]

        return value
