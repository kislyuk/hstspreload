SHELL=/bin/bash -eo pipefail
TSS_URL=https://chromium.googlesource.com/chromium/src/+/master/net/http/transport_security_state_static.json

wheel: lint constants clean
	./setup.py bdist_wheel

constants: pyhttpsec/hsts_preload_domains.json.gz

pyhttpsec/hsts_preload_domains.json.gz:
	curl "$(TSS_URL)?format=TEXT" | base64 --decode | scripts/gen_tss | gzip > $@

test_deps:
	pip install coverage flake8

lint: test_deps
	./setup.py flake8

test: test_deps lint
	coverage run setup.py test

init_docs:
	cd docs; sphinx-quickstart

docs:
	$(MAKE) -C docs html

install: clean
	python ./setup.py bdist_wheel
	pip install --upgrade dist/*.whl

clean:
	-rm -rf build dist
	-rm -rf *.egg-info

.PHONY: wheel lint test test_deps docs install clean

include common.mk
