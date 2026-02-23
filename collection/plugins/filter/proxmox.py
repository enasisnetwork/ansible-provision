"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from encommon.parse.jinja2 import FILTERS



class FilterModule:
    """
    Define filter functions available with Ansible routines.
    """


    def filters(
        # NOCVR
        self,
    ) -> 'FILTERS':
        """
        Return the filter functions for use in Ansible routines.

        :returns: Filter functions for use in Ansible routines.
        """

        return {
            'proxmox_facts_virtio': proxmox_facts_virtio,
            'proxmox_facts_net': proxmox_facts_net}



def proxmox_facts_virtio(
    storage: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Construct the information for use within the downstream.

    .. note::
       Born out of changes to Ansible and their templating.

    :param storage: Values that will be prepared for tasks.
    :returns: Constructed information for use in downstream.
    """

    from encommon.types import getate

    output: dict[str, Any] = {}
    index = 0

    for item in storage:

        state = item['state']

        if state != 'present':
            continue

        store = getate(
            item, 'virtual/store')

        size = getate(
            item, 'virtual/size')

        assert store and size

        output[f'virtio{index}'] = (
            f'{store}:{size}')

        index += 1

    return output



def proxmox_facts_net(
    network: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Construct the information for use within the downstream.

    .. note::
       Born out of changes to Ansible and their templating.

    :param network: Values that will be prepared for tasks.
    :returns: Constructed information for use in downstream.
    """

    from encommon.types import getate

    output: dict[str, Any] = {}
    index = 0

    for item in network:

        state = item['state']
        type = item['type']

        if (state != 'present'
                or type != 'ethernet'):
            continue

        hwaddr = item['hwaddr']

        bridge = getate(
            item, 'virtual/bridge')

        assert bridge is not None

        output[f'net{index}'] = (
            f'virtio={hwaddr},'
            f'bridge={bridge}')

        index += 1

    return output
