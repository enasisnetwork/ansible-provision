"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml



from typing import Annotated
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field



class ProxmoxParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    enable: Annotated[
        bool,
        Field(False,
              description='Whether or provision the guest')]

    host: Annotated[
        Optional[str],
        Field(None,
              description='Inventory host where Proxmox runs',
              min_length=1)]

    endpoint: Annotated[
        Optional[str],
        Field(None,
              description='API endpoint for the operations',
              min_length=1)]

    port: Annotated[
        int,
        Field(8006,
              description='Port number to the API service',
              ge=1, le=65535)]

    username: Annotated[
        Optional[str],
        Field(None,
              description='Username for API authentication',
              min_length=1)]

    password: Annotated[
        Optional[str],
        Field(None,
              description='Password for API authentication',
              min_length=1)]

    token: Annotated[
        Optional[str],
        Field(None,
              description='Credential for API authentication',
              min_length=1)]

    secret: Annotated[
        Optional[str],
        Field(None,
              description='Credential for API authentication',
              min_length=1)]

    cores: Annotated[
        int,
        Field(1,
              description='Amount of virtual CPUs allocated',
              ge=1)]

    memory: Annotated[
        int,
        Field(1,
              description='Amount of memory allocated in GB',
              ge=1)]

    uefi: Annotated[
        bool,
        Field(True,
              description='Enable UEFI firmware for the OS')]

    ostype: Annotated[
        Optional[str],
        Field(None,
              description='Identifier for operating system',
              min_length=3)]

    install: Annotated[
        Optional[str],
        Field(None,
              description='Optional path to installation ISO',
              min_length=1)]

    autostart: Annotated[
        bool,
        Field(False,
              description='Automatic startup with hypervisor')]
