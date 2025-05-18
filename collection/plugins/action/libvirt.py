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



class LibvirtParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    host: Annotated[
        Optional[str],
        Field(None,
              description='Inventory host where Libvirt runs',
              min_length=1)]

    prefix: Annotated[
        str,
        Field('qemu://',
              description='Prefix when interacting with API',
              min_length=5)]

    vcpus: Annotated[
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

    osid: Annotated[
        Optional[str],
        Field(None,
              description='Identifier for operating system',
              min_length=5)]

    isos: Annotated[
        Optional[str],
        Field(None,
              description='Indicate where to upload the ISO',
              min_length=1)]

    install: Annotated[
        Optional[str],
        Field(None,
              description='Optional path to installation ISO',
              min_length=1)]

    autostart: Annotated[
        bool,
        Field(False,
              description='Automatic startup with hypervisor')]
