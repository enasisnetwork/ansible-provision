# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: provision-libvirt-overview
provision-libvirt-overview: \
	.check-stage .check-limit
	@## Information about the role operations
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-overview<c0>)
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
			--tags=libvirt-overview \
			enasisnetwork.provision.libvirt; \
		deactivate)



.PHONY: provision-libvirt-create
provision-libvirt-create: \
	.check-stage .check-limit
	@## Create the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-create<c0>)
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
			--tags=libvirt-create \
			enasisnetwork.provision.libvirt; \
		deactivate)



.PHONY: provision-libvirt-update
provision-libvirt-update: \
	.check-stage .check-limit
	@## Update the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-update<c0>)
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
			--tags=libvirt-update \
			enasisnetwork.provision.libvirt; \
		deactivate)



.PHONY: provision-libvirt-install-upload
provision-libvirt-install-upload: \
	.check-stage .check-limit
	@## Upload the installation to hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-install-upload<c0>)
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
			--tags=libvirt-install-upload \
			enasisnetwork.provision.libvirt; \
		deactivate)



.PHONY: provision-libvirt-install-delete
provision-libvirt-install-delete: \
	.check-stage .check-limit
	@## Delete the installation on hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-install-delete<c0>)
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
			--tags=libvirt-install-delete \
			enasisnetwork.provision.libvirt; \
		deactivate)



.PHONY: provision-libvirt-state-poweron
provision-libvirt-state-poweron: \
	.check-stage .check-limit
	@## Update status for guest in hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-state-poweron<c0>)
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
			--tags=libvirt-state-poweron \
			enasisnetwork.provision.libvirt; \
		deactivate)



.PHONY: provision-libvirt-state-nopower
provision-libvirt-state-nopower: \
	.check-stage .check-limit
	@## Update status for guest in hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-state-nopower<c0>)
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
			--tags=libvirt-state-nopower \
			enasisnetwork.provision.libvirt; \
		deactivate)



.PHONY: provision-libvirt-delete
provision-libvirt-delete: \
	.check-stage .check-limit
	@## Delete the guest within the hypervisor
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-libvirt-delete<c0>)
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
			--tags=libvirt-delete \
			enasisnetwork.provision.libvirt; \
		deactivate)
