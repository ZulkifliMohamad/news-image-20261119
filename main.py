#!/usr/bin/env python3
"""news-image-20261119 entrypoint.

Copies the pre-rendered infographic ``entry.png`` (which sits next to
this file) into the output directory make.fun expects. Python 3.13,
standard library only, no network access. The output is byte-identical
to the source image, so repeated runs always produce the same file.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE_IMAGE = os.path.join(HERE, "entry.png")


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SOURCE_IMAGE):
        print(f"error: source image not found: {SOURCE_IMAGE}", file=sys.stderr)
        return 1
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(SOURCE_IMAGE, destination)
    # The entry must be byte-identical to the source: verify the copy
    # by size and by content before reporting success.
    if os.path.getsize(destination) != os.path.getsize(SOURCE_IMAGE):
        print("error: copied file size does not match the source image",
              file=sys.stderr)
        return 1
    with open(SOURCE_IMAGE, "rb") as src, open(destination, "rb") as dst:
        if src.read() != dst.read():
            print("error: copied file bytes do not match the source image",
                  file=sys.stderr)
            return 1
    print(f"wrote {destination} ({os.path.getsize(destination)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
