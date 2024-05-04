from attrs import define, field
from enum import Enum, auto
import httpx
import logging
import io

import error


###############################################################


class ContentType(Enum):
    JSON = auto()
    BLOB = auto()


def get_data(server_url, data_id: str) -> tuple[ContentType, bytes | error.RespError]:
    endpoint = f"{server_url}/data/{data_id}/blob"
    headers = {"Accept": "application/octet-stream"}

    with httpx.Client() as client:
        response = client.get(
            endpoint,
            headers=headers,
        )

    # If the response is JSON, return the JSON object
    # `response.headers` returns a `CaseInsensitiveDict`
    if response.headers.get("content-type") == "application/json":
        response_json: dict[str, str] = response.json()
        logging.debug(response_json)

        return (ContentType.JSON, error.RespError(**response_json))

    logging.debug("content-type: application/octet-stream")

    return (ContentType.BLOB, response.content)


async def get_data_async(
    server_url, data_id: str
) -> tuple[ContentType, bytes | error.RespError]:
    endpoint = f"{server_url}/data/{data_id}/blob"
    headers = {"Accept": "application/octet-stream"}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            endpoint,
            headers=headers,
        )

    # If the response is JSON, return the JSON object
    # `response.headers` returns a `CaseInsensitiveDict`
    if response.headers.get("content-type") == "application/json":
        response_json: dict[str, str] = response.json()
        logging.debug(response_json)

        return (ContentType.JSON, error.RespError(**response_json))

    logging.debug("content-type: application/octet-stream")

    return (ContentType.BLOB, response.content)


###############################################################


@define(slots=True, frozen=True)
class RespDataCreate:
    """Create a BLOB
    method: `POST`
    endpoint: `/data`

    type respMessageDataCreate struct {
        Code    int    `json:"code"`
        Status  string `json:"status"`
        Message string `json:"message,omitempty"`

        DataID   int64  `json:"id,string"`
        DataHash string `json:"checksum"`
    }
    """

    code: int
    status: str
    message: str
    data_id: str = field(alias="id")
    checksum: str


def post_data(
    server_url,
    data_bytes: bytes,
    file_name: str = "input",
) -> RespDataCreate:
    endpoint = f"{server_url}/data"
    headers = {"Accept": "application/json"}

    file = {"file": (file_name, io.BytesIO(data_bytes))}

    with httpx.Client() as client:
        response = client.post(
            endpoint,
            headers=headers,
            files=file,
        )

    response_json: dict[str, str] = response.json()
    logging.debug(response_json)

    return RespDataCreate(**response_json)


async def post_data_async(
    server_url,
    data_bytes: bytes,
    file_name: str = "input",
) -> RespDataCreate:
    endpoint = f"{server_url}/data"
    headers = {"Accept": "application/json"}

    file = {"file": (file_name, io.BytesIO(data_bytes))}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            endpoint,
            headers=headers,
            files=file,
        )

    response_json: dict[str, str] = response.json()
    logging.debug(response_json)

    return RespDataCreate(**response_json)


###############################################################


@define(slots=True, frozen=True)
class RespDataInfo:
    """Get BLOB metadata
    method: `GET`
    endpoint: `/data/{data_id}`

    type respMsgDataRead struct {
        Code    int    `json:"code"`
        Status  string `json:"status"`
        Message string `json:"message,omitempty"`

        DataID   int64  `json:"id,string,omitempty"`
        DataHash string `json:"checksum,omitempty"`
    }
    """

    code: int
    status: str
    message: str
    data_id: str = field(alias="id")
    checksum: str


def get_data_info(server_url, data_id: str) -> RespDataInfo:
    endpoint = f"{server_url}/data/{data_id}"
    headers = {"Accept": "application/json"}

    with httpx.Client() as client:
        response = client.get(
            endpoint,
            headers=headers,
        )

    response_json = response.json()
    logging.debug(response_json)

    return RespDataInfo(**response_json)


async def get_data_info_async(server_url, data_id: str) -> RespDataInfo:
    endpoint = f"{server_url}/data/{data_id}"
    headers = {"Accept": "application/json"}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            endpoint,
            headers=headers,
        )

    response_json = response.json()
    logging.debug(response_json)

    return RespDataInfo(**response_json)
