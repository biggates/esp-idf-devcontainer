# esp-idf-devcontainer

[![v5.3.2_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v5.3.2_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv5.3.2_qemu_20240606&logo=docker) ![v5.3.1_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v5.3.1_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv5.3.1_qemu_20240606&logo=docker) ![v5.2.3_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v5.2.3_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv5.2.3_qemu_20240606&logo=docker) ![v5.2.2_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v5.2.2_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv5.2.2_qemu_20240606&logo=docker) ![v5.1.5_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v5.1.5_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv5.1.5_qemu_20240606&logo=docker) ![v5.1.4_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v5.1.4_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv5.1.4_qemu_20240606&logo=docker) ![v5.0.7_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v5.0.7_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv5.0.7_qemu_20240606&logo=docker) ![v4.4.8_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v4.4.8_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv4.4.8_qemu_20240606&logo=docker) ![v4.3.7_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v4.3.7_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv4.3.7_qemu_20240606&logo=docker) ![v4.2.5_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v4.2.5_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv4.2.5_qemu_20240606&logo=docker) ![v4.1.4_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v4.1.4_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv4.1.4_qemu_20240606&logo=docker) ![v4.0.4_qemu_20240606 badge](https://img.shields.io/docker/v/biggates/esp-idf-devcontainer/v4.0.4_qemu_20240606?label=biggates%2Fesp-idf-devcontainer%2Fv4.0.4_qemu_20240606&logo=docker)](https://hub.docker.com/r/biggates/esp-idf-devcontainer) [![Docker Publish Badge](https://github.com/biggates/esp-idf-devcontainer/actions/workflows/docker-publish.yml/badge.svg?branch=master)](https://github.com/biggates/esp-idf-devcontainer/actions/workflows/docker-publish.yml)

docker image for developing espressif idf in VS Code devcontainer

## How to use

1. "Add Docker container configuration" in ESP-IDF VS Code Extension, as in [Tutorial: Using Docker Container](https://github.com/espressif/vscode-esp-idf-extension/blob/master/docs/tutorial/using-docker-container.md)
2. Replace `.devcontainer/Dockerfile` with:

  ```dockerfile
  FROM biggates/esp-idf-devcontainer:(TAG)
  ```

## Available tags

- `biggates/esp-idf-devcontainer:v5.3.2_qemu_20240606`
- `biggates/esp-idf-devcontainer:v5.3.1_qemu_20240606`
- `biggates/esp-idf-devcontainer:v5.2.3_qemu_20240606`
- `biggates/esp-idf-devcontainer:v5.2.2_qemu_20240606`
- `biggates/esp-idf-devcontainer:v5.1.5_qemu_20240606`
- `biggates/esp-idf-devcontainer:v5.1.4_qemu_20240606`
- `biggates/esp-idf-devcontainer:v5.0.7_qemu_20240606`

## Solved Problem

Currently, the dev container provided by ESP-IDF VS Code Extension is a [Dockerfile](https://github.com/espressif/vscode-esp-idf-extension/blob/master/templates/.devcontainer/Dockerfile), which has to be re-built every time when switching between idf versions.

This project provides a pre-built image so you can skip this build process.

## Base Container

* https://github.com/espressif/vscode-esp-idf-extension/blob/master/templates/.devcontainer/Dockerfile

## Additional packages

* instead of using `linux-tools-5.4.0-77-generic`, use `linux-tools-virtual` instead. via [dorssel/usbipd-win](https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools)
* a more recently version of [espressif/qemu](https://github.com/espressif/qemu/)
* [pre-commit](https://pre-commit.com/)

## Developing

### Environment

* python
* install python requirements by `python -m pip install -r requirements.txt`

### Add more idf versions

Supported idf versions (tags) are stored in [idf_versions.json](./idf_versions.json) as a whitelist.

### Add more qemu versions

Known espressif/qemu info are stored in [qemu_versions.json](./qemu_versions.json) as a list.

The tricky part is that you have to specify sha256 of the asset.



### How to build an image manually

build all tags:

```bash
$ python scripts/main.py build --all
```

build specific one or more tags:

```bash
$ python scripts/main.py build v4.3.4
```

### How to push an image

```bash
$ python scripts/main.py push v5.0.1
```
