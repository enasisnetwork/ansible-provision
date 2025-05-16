"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget about params.yml



from pathlib import Path
from re import match as re_match
from typing import Annotated
from typing import Any
from typing import Literal
from typing import Optional

from ansible.plugins.action import ActionBase  # type: ignore

from encommon.types import BaseModel
from encommon.types import DictStrAny
from encommon.types import sort_dict

from pydantic import Field
from pydantic import field_validator
from pydantic import model_validator



class InstallParams(BaseModel, extra='ignore'):
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



class AccountPasshashParams(BaseModel, extra='ignore'):
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



class AccountParams(BaseModel, extra='ignore'):
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



class GroupParams(BaseModel, extra='ignore'):
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



class StorageHostParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    store: Annotated[
        str,
        Field(...,
              description='Name of store for virtual device',
              min_length=1)]

    size: Annotated[
        int,
        Field(...,
              description='Size of store of virtual device',
              ge=1)]



class StoragePartParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Unique name for the partition',
              min_length=1)]

    mount: Annotated[
        str,
        Field(...,
              description='Where the partition is mounted',
              min_length=1)]

    fstype: Annotated[
        str,
        Field(...,
              description='Filesystem format for partition',
              min_length=3)]

    size: Annotated[
        Optional[int],
        Field(None,
              description='Optional size otherwise grows',
              ge=1)]



class StorageParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Device name in operating system',
              min_length=1)]

    boot: Annotated[
        bool,
        Field(False,
              description='Indicate that disk is bootable')]

    virtual: Annotated[
        StorageHostParams,
        Field(...,
              description='Define additional host settings')]

    state: Annotated[
        Literal['present', 'absent'],
        Field('present',
              description='Determine whether device present')]

    partition: Annotated[
        Optional[list[StoragePartParams]],
        Field(None,
              description='Define schematics for partitions')]


    @field_validator(
        'partition',
        mode='before')
    @classmethod
    def parse_partition(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if (isinstance(value, list)
                or value is None):
            return value

        model = StoragePartParams

        returned: list[StoragePartParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned



class NetworkHostParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    bridge: Annotated[
        str,
        Field(...,
              description='Attach to bridge on the host',
              min_length=1)]



class NetworkParams(BaseModel, extra='ignore'):
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



class LibvirtParams(BaseModel, extra='ignore'):
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
        str,
        Field(...,
              description='Identifier for operating system',
              min_length=5)]

    isos: Annotated[
        Optional[str],
        Field(None,
              description='Indicate where to upload the ISO',
              min_length=1)]



class ProxmoxParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

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
        str,
        Field(...,
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
        str,
        Field(...,
              description='Identifier for operating system',
              min_length=3)]



class RoleParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    name: Annotated[
        str,
        Field(...,
              description='Hostname in the operating system',
              min_length=1)]

    kind: Annotated[
        Literal['physical', 'virtual'],
        Field(...,
              description='Inventory host deployment kind')]

    family: Annotated[
        Literal[
            'almalinux',
            'fedora',
            'openbsd',
            'windows',
            'proxmox'],
        Field(...,
              description='Family of the operating system')]

    domain: Annotated[
        str,
        Field('invalid',
              description='Hostname in the operating system',
              min_length=1)]

    staging: Annotated[
        str,
        Field(...,
              description='Where the files will be staged',
              min_length=5)]

    install: Annotated[
        Optional[InstallParams],
        Field(None,
              description='Parameters for the install ISO')]

    users: Annotated[
        Optional[list[AccountParams]],
        Field(None,
              description='Account configuration parameters')]

    groups: Annotated[
        Optional[list[GroupParams]],
        Field(None,
              description='Group configuration parameters')]

    storage: Annotated[
        Optional[list[StorageParams]],
        Field(None,
              description='Storage configuration parameters')]

    network: Annotated[
        Optional[list[NetworkParams]],
        Field(None,
              description='Network configuration parameters')]

    libvirt: Annotated[
        Optional[LibvirtParams],
        Field(None,
              description='Parameters for VM provisioning')]

    proxmox: Annotated[
        Optional[ProxmoxParams],
        Field(None,
              description='Parameters for VM provisioning')]


    @field_validator(
        'users',
        mode='before')
    @classmethod
    def parse_users(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if (isinstance(value, list)
                or value is None):
            return value

        model = AccountParams

        returned: list[AccountParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned


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

        if (isinstance(value, list)
                or value is None):
            return value

        model = GroupParams

        returned: list[GroupParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned


    @field_validator(
        'storage',
        mode='before')
    @classmethod
    def parse_storage(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if (isinstance(value, list)
                or value is None):
            return value

        model = StorageParams

        returned: list[StorageParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned


    @field_validator(
        'network',
        mode='before')
    @classmethod
    def parse_network(
        # NOCVR
        cls,
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        """
        Perform advanced validation on the parameters provided.
        """

        if (isinstance(value, list)
                or value is None):
            return value

        model = NetworkParams

        returned: list[NetworkParams] = []


        assert isinstance(value, dict)

        items = value.items()

        for key, value in items:

            value = dict(value)
            name = value.get('name')

            if name is None:
                value['name'] = key

            item = model(**value)

            returned.append(item)


        return returned



class ActionModule(ActionBase):  # type: ignore
    """
    Perform whatever operation is associated with the file.
    """


    def run(
        # NOCVR
        self,
        tmp: Optional[str] = None,
        task_vars: Optional[DictStrAny] = None,
    ) -> DictStrAny:
        """
        Perform whatever operation is associated with the file.

        :param tmp: Placeholder for since deprecated parameter.
        :param task_vars: Variables associated around this task.
        :returns: Dictionary of results for the module process.
        """

        result: DictStrAny = {
            'params': None,
            'changed': False}

        source = self._task.args


        try:

            params = (
                RoleParams(**source)
                .endumped)

            result['params'] = (
                sort_dict(params))


        except Exception as reason:
            result |= {
                'failed': True,
                'exception': reason}


        return sort_dict(result)
