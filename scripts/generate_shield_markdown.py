#!/usr/bin/env python3

# This scripts generates shields.io markdown text, which is used in README.md

import json

REPO = "esp-idf-devcontainer"


def _tag_to_markdown(tag):
    return f"![{tag} badge](https://img.shields.io/docker/v/biggates/{REPO}/{tag}?label=biggates%2Fesp-idf-devcontainer%2F{tag}&logo=docker)"


if __name__ == "__main__":
    with open("idf_versions.json", "r") as f:
        idf_versions = json.load(f)

        latest_idf_version = idf_versions[0]

    with open("qemu_versions.json", "r") as f:
        qemu_versions = json.load(f)
        latest_qemu_version_item = qemu_versions[0]

    all_tags = []
    for idf_version in idf_versions:
        all_tags.append(f"{idf_version}_qemu_{latest_qemu_version_item.get('version')}")

    all_images = " ".join([_tag_to_markdown(tag) for tag in all_tags])

    all_markdown = (
        "["
        + all_images
        + f"](https://hub.docker.com/r/biggates/{REPO})"
        + f" [![Docker Publish Badge](https://github.com/biggates/{REPO}/actions/workflows/docker-publish.yml/badge.svg?branch=master)](https://github.com/biggates/{REPO}/actions/workflows/docker-publish.yml)"
    )

    all_supported_tags = "\n".join([f"- `biggates/{REPO}:{tag}`" for tag in all_tags])

    print("")
    print("## Tags")
    print(all_markdown)

    print("")
    print("## Supported tags")
    print("")
    print(all_supported_tags)
