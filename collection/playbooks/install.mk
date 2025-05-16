# Functions and routines associated with Enasis Network Orchestrations.

# This file is part of Enasis Network software eco-system. Distribution
# is permitted, for more information consult the project license file.



.PHONY: provision-install-download
provision-install-download: \
	.check-stage .check-limit
	@## Download the ISO from defined source
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-install-download<c0>)
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
			--tags=install-download \
			enasisnetwork.provision.install; \
		deactivate)



.PHONY: provision-install-prepare
provision-install-prepare: \
	.check-stage .check-limit
	@## Prepare for bootable installation image
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-install-prepare<c0>)
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
			--tags=install-prepare \
			enasisnetwork.provision.install; \
		deactivate)



.PHONY: provision-install-unattend
provision-install-unattend: \
	.check-stage .check-limit
	@## Template the kickstart related files
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-install-unattend<c0>)
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
			--tags=install-unattend \
			enasisnetwork.provision.install; \
		deactivate)



.PHONY: provision-install-build
provision-install-build: \
	.check-stage .check-limit
	@## Build the bootable installation image
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-install-build<c0>)
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
			--tags=install-build \
			enasisnetwork.provision.install; \
		deactivate)



.PHONY: provision-install-delete
provision-install-delete: \
	.check-stage .check-limit
	@## Delete files related to inventory hosts
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-install-delete<c0>)
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
			--tags=install-delete \
			enasisnetwork.provision.install; \
		deactivate)



.PHONY: provision-install-clean
provision-install-clean: \
	.check-stage .check-limit
	@## Delete files related to image building
	@#
	$(call MAKE_PR2NT,\
		<cD>make <cL>provision-install-clean<c0>)
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
			--tags=install-clean \
			enasisnetwork.provision.install; \
		deactivate)
