from ..api import Request, Response
import httpx
from typing import override
from urllib.parse import urljoin
from pydantic import Field


class JobCreateResponse(Response):
    code: int
    status: str
    job_id: str = Field(alias="id")

    @override
    def from_response(response: httpx.Response):
        return JobCreateResponse(**response.json())


class JobCreateRequest(Request):
    lambda_id: str = Field(serialization_alias="lambda")
    data_id: str = Field(serialization_alias="input")
    tags: list[str]

    @override
    def endpoint(self):
        return "job"

    @override
    async def send(self, client: httpx.AsyncClient, host: str) -> JobCreateResponse:
        url = urljoin(host, self.endpoint())
        response = await client.post(url, json=self.model_dump())

        return JobCreateResponse.from_response(response)
