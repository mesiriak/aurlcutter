from .._base import BaseCutter
from .._validators import validate_url
from .._links import OSDB
from .._exceptions import CuttingErrorException

import logging
import re

logger = logging.getLogger(__name__)


class Cutter(BaseCutter):
    """
    Osdb shortener implementation   
    """
    
    api_url = OSDB
    
    response_re = re.compile(r"http:\/\/osdb\.link\/.*<", re.IGNORECASE)
    
    async def cut(self, url: str) -> str:
        """
        OSDB cutter method

        Args:
            url (str): Url u wanna to cut

        Raises:
            CuttingErrorException: If the API returns an error as response

        Returns:
            str: Shorted url
        """
        
        url = await validate_url(url)
        response = await self._post(self.api_url, data={"url": url})

        if response.status_code == 200:
            return self.response_re.findall(response.text)[0].strip("<")

        raise CuttingErrorException(response.content)