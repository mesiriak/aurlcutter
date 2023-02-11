from .._base import BaseCutter
from .._validators import validate_url
from .._links import ISGD
from .._exceptions import CuttingErrorException

import logging

logger = logging.getLogger(__name__)


class Cutter(BaseCutter):
    """
    Is.gd shortener implementation   
    """
    
    api_url = ISGD
    
    async def cut(self, url: str) -> str:
        """
        Is.gd cut method implementation
        
        Args:
            url (str): url to be shorted

        Raises:
            CuttingErrorException: If API response come with error

        Returns:
            str: Short url if everything is ok
        """
        url = await validate_url(url)
        response = await self._get(self.api_url, params={"format": "simple", "url": url})

        if response.status_code == 200:
            return response.text.strip()

        raise CuttingErrorException(response.content)
