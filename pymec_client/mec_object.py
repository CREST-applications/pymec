from typing import Optional, Any
from typing_extensions import Self
import logging


class MECObject(object):
    __slots__ = ["_server_url", "_id", "_logger"]

    def __init__(
        self,
        server_url: str,
        id: Optional[str] = None,
        logger: Optional[logging.Logger] = None,
    ):
        self._server_url = server_url
        self._id = id
        self._logger: logging.Logger = logger or logging.getLogger(__name__)

    @property
    def id(self) -> str:
        if self._id is None:
            raise ValueError("id is not set")
        return self._id

    def remote_info(self) -> Any:
        raise NotImplementedError()

    async def remote_info_async(self) -> Any:
        raise NotImplementedError()
    
    def has_remote(self) -> bool:
        return self._id is not None
