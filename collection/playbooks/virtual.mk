# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: provision-virtual-overview
provision-virtual-overview: \
	.check-stage .check-limit
	@## Information about the role operations
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-overview<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-overview,\
				proxmox-overview" \
			enasisnetwork.provision.virtual; \
		deactivate)



.PHONY: provision-virtual-create
provision-virtual-create: \
	.check-stage .check-limit
	@## Create the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-create<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-create,\
				proxmox-create" \
			enasisnetwork.provision.virtual; \
		deactivate)



.PHONY: provision-virtual-update
provision-virtual-update: \
	.check-stage .check-limit
	@## Update the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-update<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		orche_ensured="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-update,\
				proxmox-update" \
			enasisnetwork.provision.virtual; \
		deactivate)



.PHONY: provision-virtual-install-upload
provision-virtual-install-upload: \
	.check-stage .check-limit
	@## Upload the installation to hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-install-upload<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-install-upload,\
				proxmox-install-upload" \
			enasisnetwork.provision.virtual; \
		deactivate)



.PHONY: provision-virtual-install-delete
provision-virtual-install-delete: \
	.check-stage .check-limit
	@## Delete the installation on hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-install-delete<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-install-delete,\
				proxmox-install-delete" \
			enasisnetwork.provision.virtual; \
		deactivate)



.PHONY: provision-virtual-state-poweron
provision-virtual-state-poweron: \
	.check-stage .check-limit
	@## Update status for guest in hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-state-poweron<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-state-poweron,\
				proxmox-state-poweron" \
			enasisnetwork.provision.virtual; \
		deactivate)



.PHONY: provision-virtual-state-nopower
provision-virtual-state-nopower: \
	.check-stage .check-limit
	@## Update status for guest in hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-state-nopower<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-state-nopower,\
				proxmox-state-nopower" \
			enasisnetwork.provision.virtual; \
		deactivate)



.PHONY: provision-virtual-delete
provision-virtual-delete: \
	.check-stage .check-limit
	@## Delete the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-virtual-delete<c0>)
	@#
	@( \
		set -e; \
		[ -f ./orchestro.env ] \
			&& set -a \
			&& . ./orchestro.env \
			&& set +a || true; \
		. $(VENVP)/bin/activate; \
		PYTHONPATH=. \
		ansible_serial="yes" \
		orche_ensured="yes" \
		orche_confirm="yes" \
		ansible-playbook \
			$(ansible_args) \
			--limit="$(limit)" \
			--tags="\
				libvirt-delete,\
				proxmox-delete" \
			enasisnetwork.provision.virtual; \
		deactivate)
