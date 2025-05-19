# Description
Provides tasks for provisioning guests from normalized parameters.

# Using this role with tags
- `libvirt-overview` Information about the role operations
- `libvirt-create` Create the guest within the hypervisor
- `libvirt-update` Update the guest within the hypervisor
- `libvirt-install-upload` Upload the installation to hypervisor
- `libvirt-install-delete` Delete the installation on hypervisor
- `libvirt-state-poweron` Update status for guest in hypervisor
- `libvirt-state-nopower` Update status for guest in hypervisor
- `libvirt-delete` Delete the guest within the hypervisor

# Example with role and tags
```yaml
- hosts: ...
  tasks:

    - name: Information about the role operations
      import_role:
        name: enasisnetwork.provision.libvirt
      tags: libvirt-overview

    - name: Create the guest within the hypervisor
      import_role:
        name: enasisnetwork.provision.proxmox
      tags: libvirt-create

    - name: Upload the installation to hypervisor
      import_role:
        name: enasisnetwork.provision.proxmox
      tags: libvirt-install-upload

    - name: Update the guest within the hypervisor
      import_role:
        name: enasisnetwork.provision.proxmox
      tags: libvirt-update
```

# Example from command line
*Information about the role operations*
```
ansible-playbook \
  ...
  --tags "libvirt-overview" \
  enasisnetwork.provision.libvirt
```

## Variables for Ansible inventory
- `provision_libvirt` Parameters for VM provisioning
    - You may specify values here, or in explicit below.
    - `enable` Whether or provision the guest
    - `autostart` Automatic startup with hypervisor
    - `host` Inventory host where Libvirt runs
    - `prefix` Prefix when interacting with API
    - `vcpus` Amount of virtual CPUs allocated
    - `memory` Amount of memory allocated in GB
    - `uefi` Enable UEFI firmware for the OS
    - `osid` Identifier for operating system
    - `isos` Indicate where to upload the ISO
    - `install` Optional path to installation ISO
- `provision_libvirt_enable` Whether or provision the guest
- `provision_libvirt_autostart` Automatic startup with hypervisor
- `provision_libvirt_host` Inventory host where Libvirt runs
- `provision_libvirt_prefix` Prefix when interacting with API
- `provision_libvirt_vcpus` Amount of virtual CPUs allocated
- `provision_libvirt_memory` Amount of memory allocated in GB
- `provision_libvirt_uefi` Enable UEFI firmware for the OS
- `provision_libvirt_osid` Identifier for operating system
- `provision_libvirt_isos` Indicate where to upload the ISO
- `provision_libvirt_install` Optional path to installation ISO

Check out the parameter model on
[GitHub](https://github.com/enasisnetwork/ansible-provision/blob/main/collection/plugins/action/libvirt.py)
for more information.
