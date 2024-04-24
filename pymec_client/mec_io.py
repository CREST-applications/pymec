from enum import Enum, auto
import requests
import logging

from .mec_api import MECAPI, MECContentType


class MECIOException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class MECResStatus(Enum):
    OK = auto()
    FAILED = auto()


class MECIO(object):
    def __init__(self, server_url: str):
        self._server_url = server_url
        self._api = MECAPI(server_url)

    def get_data(self, data_id: str) -> str:
        # endpoint = f"{self._server_url}/data/{data_id}/blob"
        # headers = {"Accept": "application/json"}

        # response = requests.get(
        #     endpoint,
        #     headers=headers,
        # )

        # logging.debug("Data fetched.")

        # # blob が json の場合は成功したのか判定できない
        # # header から判定する？
        # return response.text

        (content_type, data) = self._api.get_data(data_id)

        if content_type == MECContentType.JSON:
            logging.error(data)
            raise MECIOException("Failed to fetch data.")
        
        logging.info("Data fetched.")
        
        return data

    def post_data(self, data: str, filename: str = "input") -> str:
        # endpoint = f"{self._server_url}/data"
        # headers = {"Accept": "application/json"}

        # file = {"file": (filename, data)}

        # response = requests.post(
        #     endpoint,
        #     headers=headers,
        #     files=file,
        # )

        # response_json: dict[str, str] = response.json()

        # if response_json.get("status") != "ok":
        #     logging.error(response_json)
        #     raise MECIOException("Failed to upload data.")

        # logging.debug("Data uploaded.")

        # return response_json["id"]

        response_json = self._api.post_data(data, filename)

        if response_json.get("status") != "ok":
            logging.error(response_json)
            raise MECIOException("Failed to upload data.")
        
        logging.info("Data uploaded.")

        return response_json["id"]
