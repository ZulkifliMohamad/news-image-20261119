#!/usr/bin/env python3
"""Copy the bundled news image to the harness output directory.

The entry is a program that writes one image summing up the world news
of Thursday 19 November 2026. The image itself ships in this
repository as entry.png; this program's only job is to place an exact
copy of it where the harness expects the result.

It uses nothing but the Python standard library, reads no network,
and writes nothing except the single output file. The copy is checked
afterwards: the output must be byte-identical to the bundled image,
or the program fails instead of handing in a broken file.
"""

import hashlib
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def bundled_image():
    """Path of the image shipped beside this program."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def output_image():
    """Where the harness wants the result.

    The harness sets MAKEFUN_OUTPUT_DIR for local runs; the sealed
    run writes to /output.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    source = bundled_image()
    if not os.path.isfile(source):
        print(f"bundled image not found: {source}", file=sys.stderr)
        return 1
    with open(source, "rb") as handle:
        header = handle.read(33)
    if header[: len(PNG_MAGIC)] != PNG_MAGIC:
        print("bundled image is not a PNG file", file=sys.stderr)
        return 1
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if (width, height) != (1024, 1024):
        print(f"bundled image is {width}x{height}, need 1024x1024",
              file=sys.stderr)
        return 1
    target = output_image()
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(source, target)
    if sha256_of(source) != sha256_of(target):
        print("copy mismatch: output differs from entry.png",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
