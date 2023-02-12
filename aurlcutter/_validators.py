from ._exceptions import *

import re


URL_RE = re.compile(
    r"^https?://"
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"
    r"localhost|"
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    r"(?::\d+)?"
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


async def validate_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"

    if not URL_RE.match(url):
        raise IncorrectURLException(f"{url} is not a valid URL")

    return url
