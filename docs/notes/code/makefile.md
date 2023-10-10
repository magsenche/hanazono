# Makfile

```
.SILENT:

default: help;

help: ## Display commands help
    @grep -E '^[a-zA-Z][a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

setup: ## Nothing for now
.PHONY: setup

check_format: ## Nothing for now
.PHONY: check_format

check_linting: ## Nothing for now
.PHONY: check_linting

unit_test: ## Nothing for now
.PHONY: unit_test

integ_test: ## Nothing for now
.PHONY: integ_test

nightly_test: ## Nothing for now
.PHONY: nightly_test

post_test: ## Nothing for now
.PHONY: post_test

post_master: ## Do stuff after master build
.PHONY: post_master
```