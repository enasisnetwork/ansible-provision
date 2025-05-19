"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget roles/params.yml
# NOTE Remember to update README file



from typing import Annotated
from typing import Literal
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field



class GroupParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Name for the group on system',
              min_length=1)]

    gid: Annotated[
        Optional[str],
        Field(None,
              description='Unique identifier for the group',
              min_length=1)]

    system: Annotated[
        bool,
        Field(False,
              description='Determine if is a system group')]

    state: Annotated[
        Literal['present', 'absent'],
        Field('present',
              description='Determine whether group present')]
