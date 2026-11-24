"""One-Liner Marathon entry: write a single one-line joke to entry.txt.

Deterministic: the same bytes on every run, no randomness, no timestamps,
no network, no reads outside this file. The output directory comes from
MAKEFUN_OUTPUT_DIR (default '/output'); only a file inside it is written,
never the directory itself. The write is atomic (temp file in the same
directory + os.replace) so a crash can never leave a partial entry behind.
"""

import os
import stat
import tempfile

JOKE = "I told the hotel minibar I was just looking. It charged me $14 for eye contact."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def resolve_output_dir(raw: str) -> str:
    """Return the absolute output directory, failing closed on bad input."""
    if not raw or not raw.strip():
        raise SystemExit("MAKEFUN_OUTPUT_DIR is empty")
    path = os.path.abspath(raw)
    if os.path.exists(path) and not os.path.isdir(path):
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not a directory: %s" % path)
    return path


def main() -> None:
    out_dir = resolve_output_dir(OUTPUT_DIR)
    os.makedirs(out_dir, mode=0o755, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(prefix=".entry-", dir=out_dir)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    # Self-check: what landed on disk must be the intended joke, byte for byte.
    with open(path, "rb") as fh:
        if fh.read() != data:
            raise SystemExit("entry.txt does not match the intended joke")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise SystemExit("entry.txt permissions are not 0644")


if __name__ == "__main__":
    main()
