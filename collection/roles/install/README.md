# Description
Provides tasks for building installations from normalized parameters.

# Using this role with tags
- `install-overview` Information about the role operations
- `install-download` Download the ISO from configured source
- `install-prepare` Construct prepare from the distribute
- `install-unattend` Template the unattend installation file
- `install-build` Create new ISO from prepare directory
- `install-delete` Delete files and folders from operation
- `install-clean` Delete files and folders from operation

# Example with role and tags
```yaml
- hosts: ...
  tasks:

    - name: Information about the role operations
      import_role:
        name: enasisnetwork.provision.install
      tags: install-overview
```

# Example from command line
*Information about the role operations*
```
ansible-playbook \
  ...
  --tags "install-overview" \
  enasisnetwork.provision.install
```

## Variables for Ansible inventory
- `provision_install` Parameters for the install ISO
    - You may specify values here, or in explicit below.
    - `source` Where source install is located
    - `checksum` Expected hash value of the ISO
    - `cached` File name when downloading file
- `provision_install_source` Where source install is located
- `provision_install_checksum` Expected hash value of the ISO
- `provision_install_cached` File name when downloading file

Check out the parameter model on
[GitHub](https://github.com/enasisnetwork/ansible-provision/blob/main/collection/plugins/action/install.py)
for more information.

## OpenBSD unattended installation
It's not currently straight forward to inject the `auto_install.conf` into
the `bsd.rd`, which would require an OpenBSD machine as the controller.

```
(I)nstall, (U)pgrade, (A)utoinstall or (S)hell? s

# mount /dev/cd0a /mnt
# cp /mnt/auto_install.conf .
# umount /mnt
# exit

(I)nstall, (U)pgrade, (A)utoinstall or (S)hell? a
```
