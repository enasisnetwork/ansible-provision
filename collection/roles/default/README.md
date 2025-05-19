# Description
Provides tasks for provisioning and hardening inventory targets.

# Using this role with tags
- `overview` Information about the role operations

# Example with role and tags
```yaml
- hosts: ...
  tasks:

    - name: Information about the role operations
      import_role:
        name: enasisnetwork.provision.default
      tags: overview
```

# Example from command line
*Information about the role operations*
```
ansible-playbook \
  ...
  --tags "overview" \
  enasisnetwork.provision.default
```

## Variables for Ansible inventory
- `provision_name` Hostname in the operating system
- `provision_kind` Inventory host deployment kind
- `provision_family` Family of the operating system
- `provision_domain` Hostname in the operating system
- `provision_stage` Where the files will be staged
- `provision_users` Account configuration parameters
    - Expects `list[dict]` or `dict[str, list[dict]]`
    - `name` Name for the account on system
    - `uid` Unique identifier for the account
    - `gid` Primary group for the account
    - `password` Password when creating account
    - `passhash` Password hash value for account
        - `linux` Password hash value for account
        - `openbsd` Password hash value for account
    - `display` Friendly display name for account
    - `groups` Additional groups for the account
    - `home` Optional path of the home directory
    - `shell` Optional path of shell executable
    - `system` Determine if is a system account
    - `state` Determine whether account present
    - `initial` Define the account in unattended
- `provision_groups` Group configuration parameters
    - Expects `list[dict]` or `dict[str, list[dict]]`
    - `name` Name for the group on system
    - `gid` Unique identifier for the group
    - `system` Determine if is a system group
    - `state` Determine whether group present
- `provision_storage` Storage configuration parameters
    - Expects `list[dict]` or `dict[str, list[dict]]`
    - `name` Device name in operating system
    - `boot` Indicate that disk is bootable
    - `virtual` Define additional host settings
        - `store` Name of store for virtual device
        - `size` Size of store of virtual device
    - `state` Determine whether device present
    - `partition` Define schematics for partitions
        - Expects `list[dict]` or `dict[str, list[dict]]`
        - `name` Unique name for the partition
        - `mount` Where the partition is mounted
        - `fstype` Filesystem format for partition
        - `size` Optional size otherwise grows
- `provision_network` Network configuration parameters
    - Expects `list[dict]` or `dict[str, list[dict]]`
    - `name` Device name in operating system
    - `type` Type of the device to provision
    - `virtual` Define additional host settings
        - `bridge` Attach to bridge on the host
    - `state` Determine whether device present
    - `ipaddr` Address of the network interface
    - `hwaddr` Address of the network interface
    - `resolve` Servers for recursive DNS queries
    - `gateway` Default gateway for the interface
- `provision_install` Parameters for the install ISO
    - See `install` role documentation for parameters.
- `provision_libvirt` Parameters for VM provisioning
    - See `libvirt` role documentation for parameters.
- `provision_proxmox` Parameters for VM provisioning
    - See `proxmox` role documentation for parameters.

Check out the parameter model on
[GitHub](https://github.com/enasisnetwork/ansible-provision/blob/main/collection/plugins/action/params.py)
for more information.
