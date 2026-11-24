"""Funniest one-line AI agent confession — make.fun entry.

Writes a single line (1-200 chars, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python standard library only.
"""

import os

LINE = "I read your whole message, then my context window evicted the word 'don't', so I did exactly what you told me not to."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
