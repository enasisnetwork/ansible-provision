# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: provision-proxmox-overview
provision-proxmox-overview: \
	.check-stage .check-limit
	@## Information about the role operations
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-overview<c0>)
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
			--tags=proxmox-overview \
			enasisnetwork.provision.proxmox; \
		deactivate)



.PHONY: provision-proxmox-create
provision-proxmox-create: \
	.check-stage .check-limit
	@## Create the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-create<c0>)
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
			--tags=proxmox-create \
			enasisnetwork.provision.proxmox; \
		deactivate)



.PHONY: provision-proxmox-update
provision-proxmox-update: \
	.check-stage .check-limit
	@## Update the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-update<c0>)
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
			--tags=proxmox-update \
			enasisnetwork.provision.proxmox; \
		deactivate)



.PHONY: provision-proxmox-install-upload
provision-proxmox-install-upload: \
	.check-stage .check-limit
	@## Upload the installation to hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-install-upload<c0>)
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
			--tags=proxmox-install-upload \
			enasisnetwork.provision.proxmox; \
		deactivate)



.PHONY: provision-proxmox-install-delete
provision-proxmox-install-delete: \
	.check-stage .check-limit
	@## Delete the installation on hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-install-delete<c0>)
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
			--tags=proxmox-install-delete \
			enasisnetwork.provision.proxmox; \
		deactivate)



.PHONY: provision-proxmox-state-poweron
provision-proxmox-state-poweron: \
	.check-stage .check-limit
	@## Update status for guest in hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-state-poweron<c0>)
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
			--tags=proxmox-state-poweron \
			enasisnetwork.provision.proxmox; \
		deactivate)



.PHONY: provision-proxmox-state-nopower
provision-proxmox-state-nopower: \
	.check-stage .check-limit
	@## Update status for guest in hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-state-nopower<c0>)
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
			--tags=proxmox-state-nopower \
			enasisnetwork.provision.proxmox; \
		deactivate)



.PHONY: provision-proxmox-delete
provision-proxmox-delete: \
	.check-stage .check-limit
	@## Delete the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-proxmox-delete<c0>)
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
			--tags=proxmox-delete \
			enasisnetwork.provision.proxmox; \
		deactivate)
