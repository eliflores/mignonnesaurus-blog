import os

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

_FIREFOX_BINARY_CANDIDATES = [
    "/snap/firefox/current/usr/lib/firefox/firefox",
    "/usr/lib/firefox/firefox",
]


def create_firefox_webdriver(headless=True):
    options = Options()
    if headless:
        options.add_argument("-headless")
    options.binary_location = get_firefox_binary_or_raise()
    return WebDriver(options=options)


def get_firefox_binary_or_raise():
    candidates = [os.getenv("FIREFOX_BINARY")] + _FIREFOX_BINARY_CANDIDATES
    for path in candidates:
        if path and os.path.isfile(path) and os.access(path, os.X_OK) and not _is_shell_script(path):
            return path
    raise RuntimeError(
        "Could not find an executable Firefox binary. "
        "Set FIREFOX_BINARY to a valid executable path, or install Firefox in one of: "
        + ", ".join(_FIREFOX_BINARY_CANDIDATES)
    )


def _is_shell_script(path):
    try:
        with open(path, "rb") as f:
            return f.read(2) == b"#!"
    except OSError:
        return False

