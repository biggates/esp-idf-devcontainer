# esp-idf-devcontainer

[![](https://img.shields.io/docker/image-size/biggates/esp-idf-devcontainer/idf_v5.2.2_qemu_20240122?label=biggates%2Fidf_v5.2.2_qemu_20240122&logo=docker) ![](https://img.shields.io/docker/image-size/biggates/esp-idf-devcontainer/idf_v5.1.4_qemu_20240122?label=biggates%2Fidf_v5.1.4_qemu_20240122&logo=docker) ![](https://img.shields.io/docker/image-size/biggates/esp-idf-devcontainer/idf_v5.0.6_qemu_20240122?label=biggates%2Fidf_v5.0.6_qemu_20240122&logo=docker) ![](https://img.shields.io/docker/image-size/biggates/esp-idf-devcontainer/idf_v4.4.7_qemu_20240122?label=biggates%2Fidf_v4.4.7_qemu_20240122&logo=docker) ![](https://img.shields.io/docker/image-size/biggates/esp-idf-devcontainer/idf_v4.3.7_qemu_20240122?label=biggates%2Fidf_v4.3.7_qemu_20240122&logo=docker)](https://hub.docker.com/r/biggates/esp-idf-devcontainer/tags) [![Docker Publish](https://github.com/biggates/esp-idf-devcontainer/actions/workflows/docker_publish.yml/badge.svg)](https://github.com/biggates/esp-idf-devcontainer/actions/workflows/docker_publish.yml)

docker image for developing espressif idf in VS Code devcontainer

## How to use

1. "Add Docker container configuration" in ESP-IDF VS Code Extension, as in [Tutorial: Using Docker Container](https://github.com/espressif/vscode-esp-idf-extension/blob/master/docs/tutorial/using-docker-container.md)
2. Replace `.devcontainer/Dockerfile` with:

  ```dockerfile
  FROM biggates/esp-idf-devcontainer:(TAG)
  ```

## Available tags

* `biggates/esp-idf-devcontainer:idf_v5.2.2_qemu_20240122`
* `biggates/esp-idf-devcontainer:idf_v5.1.4_qemu_20240122`
* `biggates/esp-idf-devcontainer:idf_v5.0.6_qemu_20240122`
* `biggates/esp-idf-devcontainer:idf_v4.4.7_qemu_20240122`
* `biggates/esp-idf-devcontainer:idf_v4.3.7_qemu_20240122`
* `biggates/esp-idf-devcontainer:idf_v4.2.5_qemu_20240122`
* `biggates/esp-idf-devcontainer:idf_v4.1.4_qemu_20230223`
* `biggates/esp-idf-devcontainer:idf_v4.0.4_qemu_20230223`

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
