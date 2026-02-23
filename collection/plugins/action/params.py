"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget roles/params.yml
# NOTE Remember to update README file



from pathlib import Path
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

from .account import AccountParams
from .group import GroupParams
from .install import InstallParams
from .libvirt import LibvirtParams
from .network import NetworkParams
from .proxmox import ProxmoxParams
from .storage import StorageParams



class RoleParams(BaseModel, extra='forbid'):
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
        Field(...,
              description='Hostname in the operating system',
              min_length=1)]

    stage: Annotated[
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

    drivers: Annotated[
        Optional[str],
        Field(None,
              description='Additional drivers to include',
              min_length=1)]

    libvirt: Annotated[
        Optional[LibvirtParams],
        Field(None,
              description='Parameters for VM provisioning')]

    proxmox: Annotated[
        Optional[ProxmoxParams],
        Field(None,
              description='Parameters for VM provisioning')]


    def __init__(
        # NOCVR
        self,
        /,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """


        fields = (
            'install',
            'libvirt',
            'proxmox')

        for key in list(data):

            if '_' not in key:
                continue

            base, name = (
                key.split('_', 1))

            if base not in fields:
                continue

            if base not in data:
                data[base] = {}

            _data = data[base]
            value = data[key]

            _data[name] = value

            del data[key]


        super().__init__(**data)


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


    @field_validator(
        'drivers',
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

        args = self._task.args

        assert task_vars is not None

        prefix = args['prefix']
        source = task_vars


        source = {
            k[len(prefix):]: v
            for k, v in source.items()
            if k.startswith(prefix)
            and v not in [None, '']}


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
