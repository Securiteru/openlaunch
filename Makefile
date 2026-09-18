PY ?= python3

.PHONY: playbooks serve check help

help:
	@echo "make playbooks  - generate stubs for platforms missing one"
	@echo "make serve      - serve the tracker at http://localhost:8420"
	@echo "make check      - validate platforms.csv + tracker/data.json"

playbooks:
	$(PY) platforms/build.py

serve:
	cd tracker && $(PY) -m http.server 8420

check:
	$(PY) platforms/build.py --check
