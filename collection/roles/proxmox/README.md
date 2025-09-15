# Description
Provides tasks for provisioning guests from normalized parameters.

# Using this role with tags
- `proxmox-overview` Information about the role operations
- `proxmox-create` Create the guest within the hypervisor
- `proxmox-update` Update the guest within the hypervisor
- `proxmox-install-upload` Upload the installation to hypervisor
- `proxmox-install-delete` Delete the installation on hypervisor
- `proxmox-state-poweron` Update status for guest in hypervisor
- `proxmox-state-nopower` Update status for guest in hypervisor
- `proxmox-delete` Delete the guest within the hypervisor

# Example with role and tags
```yaml
- hosts: ...
  tasks:

    - name: Information about the role operations
      import_role:
        name: enasisnetwork.provision.proxmox
      tags: proxmox-overview

    - name: Create the guest within the hypervisor
      import_role:
        name: enasisnetwork.provision.proxmox
      tags: proxmox-create

    - name: Upload the installation to hypervisor
      import_role:
        name: enasisnetwork.provision.proxmox
      tags: proxmox-install-upload

    - name: Update the guest within the hypervisor
      import_role:
        name: enasisnetwork.provision.proxmox
      tags: proxmox-update
```

# Example from command line
*Information about the role operations*
```
ansible-playbook \
  ...
  --tags "proxmox-overview" \
  enasisnetwork.provision.proxmox
```

## Variables for Ansible inventory
- `provision_proxmox` Parameters for VM provisioning
    - You may specify values here, or in explicit below.
    - `enable` Whether or provision the guest
    - `autostart` Automatic startup with hypervisor
    - `host` Inventory host where Proxmox runs
    - `endpoint` API endpoint for the operations
    - `port` Port number to the API service
    - `username` Username for API authentication
    - `password` Password for API authentication
    - `token` Credential for API authentication
    - `secret` Credential for API authentication
    - `cpu` What type of CPU emulation is used
    - `cores` Amount of virtual CPUs allocated
    - `memory` Amount of memory allocated in GB
    - `uefi` Enable UEFI firmware for the OS
    - `ostype` Identifier for operating system
    - `install` Optional path to installation ISO
- `provision_proxmox_enable` Whether or provision the guest
- `provision_proxmox_autostart` Automatic startup with hypervisor
- `provision_proxmox_host` Inventory host where Proxmox runs
- `provision_proxmox_endpoint` API endpoint for the operations
- `provision_proxmox_port` Port number to the API service
- `provision_proxmox_username` Username for API authentication
- `provision_proxmox_password` Password for API authentication
- `provision_proxmox_token` Credential for API authentication
- `provision_proxmox_secret` Credential for API authentication
- `provision_proxmox_cpu` What type of CPU emulation is used
- `provision_proxmox_cores` Amount of virtual CPUs allocated
- `provision_proxmox_memory` Amount of memory allocated in GB
- `provision_proxmox_uefi` Enable UEFI firmware for the OS
- `provision_proxmox_ostype` Identifier for operating system
- `provision_proxmox_install` Optional path to installation ISO

Check out the parameter model on
[GitHub](https://github.com/enasisnetwork/ansible-provision/blob/main/collection/plugins/action/proxmox.py)
for more information.
