from ._types import *
from ._validators import *

import httpx


class BaseCutter:
    """
    Base class with methods for every Cutter implementation
    """

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

        # self.proxies = getattr(self, "proxies", {}) Should be implemented

        self.timeout = getattr(self, "timeout", 2)
        self.follow_redirects = getattr(self, "follow_redirects", True)
        self.cert = getattr(self, "cert", None)

        self._async_client = httpx.AsyncClient()

    async def _get(
        self, url: str, params: ParamsType = None, headers: HeadersType = None
    ) -> ResponseType:
        url = await validate_url(url=url)

        response = await self._async_client.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
            follow_redirects=self.follow_redirects,
        )

        return response

    async def _post(
        self,
        url: str,
        data: DataType = None,
        json: JsonType = None,
        params: ParamsType = None,
        headers: HeadersType = None,
        cookies: CookiesType = None,
    ) -> ResponseType:
        url = await validate_url(url=url)

        response = await self._async_client.post(
            url,
            params=params,
            headers=headers,
            json=json,
            data=data,
            cookies=cookies,
            timeout=self.timeout,
            follow_redirects=self.follow_redirects,
        )

        return response

    async def cut(self, url: str) -> str:
        """
        Cutting URL using shortening service API

        Args:
            url (str): URL to shorten.

        Raises:
            NotImplementedError: Children should override this
        """

        raise NotImplementedError
