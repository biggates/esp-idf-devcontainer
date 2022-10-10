# esp-idf-devcontainer
docker image for developing espressif idf in VS Code devcontainer

## How to use

1. "Add Docker container configuration" in ESP-IDF VS Code Extension, as in [Tutorial: Using Docker Container](https://github.com/espressif/vscode-esp-idf-extension/blob/master/docs/tutorial/using-docker-container.md)
2. Replace `.devcontainer/Dockerfile` with:

  ```dockerfile
  FROM biggates/esp-idf-devcontainer
  ```

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

### How to build

build all tags:

```bash
$ python scripts/main.py build --all
```

build specific tag:

```bash
$ python scripts/main.py build v4.3.4
```
