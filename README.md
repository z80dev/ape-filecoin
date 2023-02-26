# Quick Start

Ape plugin for [Filecoin EVM](https://docs.filecoin.io/developers/smart-contracts/concepts/filecoin-evm/)

## Dependencies

- [python3](https://www.python.org/downloads) version 3.8 or greater, python3-dev

## Installation

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-filecoin
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/z80dev/ape-filecoin.git
cd ape-filecoin
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Filecoin EVM ecosystem

In your `ape-config.yaml`:


``` yaml
geth:
  filecoin:
    hyperspace-testnet:
      uri: https://filecoin-hyperspace.chainstacklabs.com/rpc/v1 # rpc endpoint from chainlist.org
```

Then, in your terminal:

```bash
ape console --network filecoin:hyperspace-testnet
```

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.
