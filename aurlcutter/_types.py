from typing import Iterator, AsyncIterator, Sequence, Any, Mapping
from httpx import Cookies, Response


SimpleTypes = str | bytes
BaseTypes = str | int | float | bool | None

DataType = dict[str, BaseTypes] | SimpleTypes | Iterator[bytes] | AsyncIterator[bytes]

HeadersType = dict[SimpleTypes, SimpleTypes] | Sequence[tuple[SimpleTypes, SimpleTypes]]

JsonType = dict[str, Any] | Any

ParamsType = (
    Mapping[str, BaseTypes | Sequence[BaseTypes]] | list[tuple[str, BaseTypes]] | str
)

CookiesType = dict[str, Any] | Cookies

ResponseType = Response
