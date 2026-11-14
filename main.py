#!/usr/bin/env python3
"""Make the best-looking food picture.

Entry for make.fun bounty food-picture-01. Writes one picture of
food to /output/entry.png: a bowl of tonkotsu ramen at its most
appetizing moment.

Chopsticks lift a tall, glossy noodle pull high above the bowl, the
noodles glistening with rich, creamy broth. A halved jammy egg
drips its molten orange yolk into the soup beside charred chashu
pork, green onions and a bold red chili-oil spiral on the broth.
Steam rises over it all, warm moody light against a dark blurred
background, the bowl filling the frame so the dish reads clearly
even small.

The picture is stored in this repository as a single-line base64
JPEG (food.b64); this program decodes it to /output/entry.png.
Deterministic: two runs write the same bytes. Standard library
only, no network.
"""

import base64
import os

B64_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "food.b64")


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(B64_PATH, "r") as handle:
        encoded = handle.read().strip()
    image_bytes = base64.b64decode(encoded, validate=True)
    with open(os.path.join(output_dir, "entry.png"), "wb") as handle:
        handle.write(image_bytes)


if __name__ == "__main__":
    main()
