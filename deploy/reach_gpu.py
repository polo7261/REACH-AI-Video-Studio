"""Cross-process GPU card lock shared by the image and video servers.

Both services load models on demand onto one physical card. The flock makes
"image reloads because the UI polled" and "video loads for a job" mutually
exclusive at load time, so the two lazy loaders can no longer race.
"""
import fcntl
import os
from contextlib import contextmanager

_LOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gpu.lock")
_fh = None


@contextmanager
def card(timeout_s: int = 3600):
    """Exclusive cross-process lock; waits up to timeout_s for the card."""
    global _fh
    if _fh is None:
        _fh = open(_LOCK_PATH, "w")
    deadline = __import__("time").time() + timeout_s
    while True:
        try:
            fcntl.flock(_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except OSError:
            if __import__("time").time() >= deadline:
                raise TimeoutError("GPU card lock busy >%ds" % timeout_s)
            __import__("time").sleep(5)
    try:
        yield
    finally:
        fcntl.flock(_fh, fcntl.LOCK_UN)
