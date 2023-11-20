import json
import subprocess
from typing import List

import click

DOCKER_IMAGE_NAME = "biggates/esp-idf-devcontainer"


def _get_all_tags() -> List[str]:
    with open("idf_versions.json", "r") as fp:
        return json.load(fp)


def _get_qemu_info() -> List[dict]:
    with open("qemu_versions.json", "r") as fp:
        return json.load(fp)


def _get_qemu_versions() -> List[str]:
    all_qemu_info = _get_qemu_info()

    return [item.get("version") for item in all_qemu_info]


def _check_qemu_version(version: str) -> str:
    all_versions = _get_qemu_versions()
    return version if version in all_versions else all_versions[0]


def _get_qemu_item(version: str) -> dict:
    all_qemu_info = _get_qemu_info()
    for v in all_qemu_info:
        if v.get("version") == version:
            return v
    return None


def _build(tag: str, qemu_version: str, verbose: bool = False):
    click.echo(
        f"building tag={click.style(tag, fg='green')}, qemu={click.style(qemu_version, fg='green')}"
    )

    qemu_item = _get_qemu_item(qemu_version)
    qemu_rel = qemu_item.get("rel")
    qemu_sha256 = qemu_item.get("sha256")
    qemu_dist = qemu_item.get("dist")
    qemu_url = qemu_item.get("url")
    full_tag_name = f"{DOCKER_IMAGE_NAME}:idf_{tag}_qemu_{qemu_version}"

    args = [
        "docker",
        "build",
        "--file",
        "Dockerfile",
        "--build-arg",
        f"IDF_VERSION={tag}",
        "--build-arg",
        f"QEMU_REL={qemu_rel}",
        "--build-arg",
        f"QEMU_SHA256={qemu_sha256}",
        "--build-arg",
        f"QEMU_DIST={qemu_dist}",
        "--build-arg",
        f"QEMU_URL={qemu_url}",
        "--tag",
        full_tag_name,
        ".",
    ]

    if verbose:
        args.append("--progress=plain")
        click.echo(f"will run: {click.style(' '.join(args), fg='yellow')}")

    completed_process = subprocess.run(args)

    if completed_process.returncode == 0:
        click.echo(f"Successfully built tag {click.style(full_tag_name, fg='green')}")
    else:
        click.echo(
            f"docker returned {click.style(completed_process.returncode, fg='red')} when building tag {click.style(full_tag_name, fg='red')}"
        )


def _push(tag: str, qemu_version: str, verbose: bool = False):
    click.echo(
        f"building tag={click.style(tag, fg='green')}, qemu={click.style(qemu_version, fg='green')}"
    )

    _get_qemu_item(qemu_version)
    full_tag_name = f"{DOCKER_IMAGE_NAME}:idf_{tag}_qemu_{qemu_version}"

    args = ["docker", "push", full_tag_name]

    if verbose:
        args.append("--progress=plain")
        click.echo(f"will run: {click.style(' '.join(args), fg='yellow')}")

    completed_process = subprocess.run(args)

    if completed_process.returncode == 0:
        click.echo(f"Successfully pushed tag {click.style(full_tag_name, fg='green')}")
    else:
        click.echo(
            f"docker returned {click.style(completed_process.returncode, fg='red')} when pushing tag {click.style(full_tag_name, fg='red')}"
        )


@click.group
def main():
    pass


@main.command
@click.option("--all", type=bool, required=False, default=False, is_flag=True)
@click.option(
    "--qemu-version",
    "--qemu",
    type=click.Choice(_get_qemu_versions()),
    required=False,
)
@click.argument("tags", type=click.Choice(_get_all_tags()), nargs=-1, required=False)
@click.option("--verbose", type=bool, required=False, default=False, is_flag=True)
def build(tags: List[str], all: bool, qemu_version: str, verbose: bool = False):
    """Build docker image(s)

    Args:
        tags (List[str]): build specified (multiple) tag(s)
        all (bool): build all tags specified by idf_versions.json
        qemu_version (str): specify QEMU version
        verbose (bool, optional): output more details. Defaults to False.
    """
    _all_tags = _get_all_tags()
    if all:
        tags = _all_tags
    else:
        ignored_tags = set(tags).difference(_all_tags)
        tags = set(tags).intersection(_all_tags)
        if len(ignored_tags) > 0:
            for ignored_tag in ignored_tags:
                click.echo(
                    f"will ignore tag {click.style(ignored_tag, fg='yellow')}, which is not in whitelist"
                )

    if len(tags) == 0:
        click.secho("No tag(s) specified", fg="red")

    qemu_version = _check_qemu_version(qemu_version)

    for tag in tags:
        _build(tag, qemu_version, verbose=verbose)


@main.command
@click.option("--all", type=bool, required=False, default=False, is_flag=True)
@click.option(
    "--qemu-version",
    "--qemu",
    type=click.Choice(_get_qemu_versions()),
    required=False,
)
@click.argument("tags", type=click.Choice(_get_all_tags()), nargs=-1, required=False)
@click.option("--verbose", type=bool, required=False, default=False, is_flag=True)
def push(tags: List[str], all: bool, qemu_version: str, verbose: bool = False):
    """Push specified docker image(s) by tag

    Args:
        tags (List[str]): specified idf version(s)
        all (bool): push all tags defined in idf_versions.json
        qemu_version (str): specify QEMU version
        verbose (bool, optional): output more details. Defaults to False.
    """
    _all_tags = _get_all_tags()
    if all:
        tags = _all_tags
    else:
        ignored_tags = set(tags).difference(_all_tags)
        tags = set(tags).intersection(_all_tags)
        if len(ignored_tags) > 0:
            for ignored_tag in ignored_tags:
                click.echo(
                    f"will ignore tag {click.style(ignored_tag, fg='yellow')}, which is not in whitelist"
                )

    if len(tags) == 0:
        click.secho("No tag(s) specified", fg="red")

    qemu_version = _check_qemu_version(qemu_version)

    for tag in tags:
        _push(tag, qemu_version, verbose=verbose)


if __name__ == "__main__":
    main()
