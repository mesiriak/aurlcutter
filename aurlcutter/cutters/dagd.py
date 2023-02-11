from .._base import BaseCutter
from .._validators import validate_url
from .._links import DAGD
from .._exceptions import CuttingErrorException

import logging

logger = logging.getLogger(__name__)


class Cutter(BaseCutter):
    """
    Tinyurl shortener implementation

    """

    api_url = DAGD
    
    async def cut(self, url: str) -> str:
        """
        Dd.gd cut method implementation
        
        Args:
            url (str): URL u want to cut

        Raises:
            CuttingErrorException: If API response was incorrect

        Returns:
            str: Short url if everything is ok
        """
        
        url = await validate_url(url)
        response = await self._get(self.api_url + "shorten", params={"url": url})

        if response.status_code == 200:
            return response.text.strip()
        
        raise CuttingErrorException(response.content)