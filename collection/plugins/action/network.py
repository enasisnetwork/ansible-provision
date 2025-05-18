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



class NetworkHostParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    bridge: Annotated[
        str,
        Field(...,
              description='Attach to bridge on the host',
              min_length=1)]



class NetworkParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Device name in operating system',
              min_length=1)]

    type: Annotated[
        Literal['ethernet'],
        Field('ethernet',
              description='Type of the device to provision',
              min_length=1)]

    virtual: Annotated[
        NetworkHostParams,
        Field(...,
              description='Define additional host settings')]

    state: Annotated[
        Literal['present', 'absent'],
        Field('present',
              description='Determine whether device present')]

    ipaddr: Annotated[
        Optional[str],
        Field(None,
              description='Address of the network interface',
              min_length=5)]

    hwaddr: Annotated[
        Optional[str],
        Field(None,
              description='Address of the network interface',
              min_length=1)]

    resolve: Annotated[
        Optional[list[str]],
        Field(None,
              description='Servers for recursive DNS queries',
              min_length=1)]

    gateway: Annotated[
        Optional[str],
        Field(None,
              description='Default gateway for the interface',
              min_length=5)]


    @field_validator(
        'hwaddr',
        mode='before')
    @classmethod
    def parse_hwaddr(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if isinstance(value, str):
            return value.replace('-', ':')

        return value


    @field_validator(
        'resolve',
        mode='before')
    @classmethod
    def parse_resolve(
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
