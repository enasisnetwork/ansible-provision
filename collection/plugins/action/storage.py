"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



# NOTE Do not forget roles/params.yml
# NOTE Remember to update README file



from typing import Annotated
from typing import Any
from typing import Literal
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field
from pydantic import field_validator



class StorageHostParams(BaseModel, extra='forbid'):
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



class StoragePartParams(BaseModel, extra='forbid'):
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



class StorageParams(BaseModel, extra='forbid'):
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
