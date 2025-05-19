#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from os import getuid
from pathlib import Path

from ansible.module_utils.basic import AnsibleModule  # type: ignore

from encommon.types import DictStrAny
from encommon.types import LDictStrAny
from encommon.types import sort_dict



_STATES = ['absent', 'present']

_PARAMETERS: DictStrAny = {
    'dest': {
        'type': 'str',
        'required': True},
    'src': {
        'type': 'str',
        'required': False},
    'state': {
        'type': 'str',
        'required': True,
        'choices': _STATES}}



def parameters(
    # NOCVR
    module: AnsibleModule,
) -> DictStrAny:
    """
    Construct parameters which are associated with the file.

    :param module: Relevant class object for Ansible module.
    :returns: Arguments which are associated with the file.
    """

    params = module.params
    check = module.check_mode

    dest = params['dest']
    state = params['state']
    src = params.get('src')


    def _exists(
        path: str,
    ) -> bool:

        return (
            Path(path)
            .exists())


    if (src is not None
            and not _exists(src)):

        module.fail_json(
            changed=False,
            msg='src not exists')

    if (not _exists(dest)
            and state == 'present'
            and check is False):

        module.fail_json(
            changed=False,
            msg='dest not exists')

    if (state == 'present'
            and src is None):

        module.fail_json(
            changed=False,
            msg='src is required')


    return sort_dict({
        'dest': dest,
        'src': src,
        'state': state})



def _mounted(
    # NOCVR
    module: AnsibleModule,
) -> bool:
    """
    Return the boolean indicating if path is a mount point.

    :param module: Relevant class object for Ansible module.
    :returns: Boolean indicating if path is a mount point.
    """

    params = parameters(module)

    path = params['dest']

    returned = (
        module.run_command(
            ['mountpoint',
             '-q', path],
            check_rc=False))

    assert isinstance(
        returned[0], int)

    return returned[0] == 0



def _domount(
    # NOCVR
    module: AnsibleModule,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param module: Relevant class object for Ansible module.
    """

    if _mounted(module):
        module.exit_json(
            changed=False)

    output: LDictStrAny = []

    if module.check_mode:
        module.exit_json(
            changed=True,
            output=output)


    params = parameters(module)


    options = (
        'loop,ro,uid='
        f'{getuid()}')

    command = [
        'sudo', 'mount',
        '-t', 'udf,iso9660',
        '-o', options,
        params['src'],
        params['dest']]


    rcode, stdout, stderr = (
        module.run_command(
            command,
            check_rc=False))

    stdout = stdout.strip()
    stderr = stderr.strip()

    output.append({
        'cmd': command,
        'rc': rcode,
        'stdout': stdout,
        'stderr': stderr})


    if rcode != 0:
        module.fail_json(
            changed=False,
            msg=output)

    module.exit_json(
        changed=True,
        output=output)



def _unmount(
    # NOCVR
    module: AnsibleModule,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param module: Relevant class object for Ansible module.
    """

    if not _mounted(module):
        module.exit_json(
            changed=False)

    output: LDictStrAny = []

    if module.check_mode:
        module.exit_json(
            changed=True,
            output=output)


    params = parameters(module)


    command = [
        'sudo', 'umount',
        params['dest']]


    rcode, stdout, stderr = (
        module.run_command(
            command,
            check_rc=False))

    stdout = stdout.strip()
    stderr = stderr.strip()

    output.append({
        'cmd': command,
        'rc': rcode,
        'stdout': stdout,
        'stderr': stderr})


    if rcode != 0:
        module.fail_json(
            changed=False,
            msg=output)

    module.exit_json(
        changed=True,
        output=output)



def execution() -> None:  # NOCVR
    """
    Perform whatever operation is associated with the file.
    """

    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=_PARAMETERS)


    params = parameters(module)

    state = params['state']


    if state == 'present':
        _domount(module)


    if state == 'absent':
        _unmount(module)


    raise ValueError('state')



if __name__ == '__main__':
    execution()  # NOCVR
