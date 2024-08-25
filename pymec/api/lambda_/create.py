from ..api_types import Request, Response
import httpx
from urllib.parse import urljoin
from pydantic import Field


class LambdaCreateResponse(Response):
    code: int
    status: str
    lambda_id: str = Field(alias="id")

    def from_response(response: httpx.Response):
        return LambdaCreateResponse(**response.json())


class LambdaCreateRequest(Request[LambdaCreateResponse]):
    data_id: str = Field(serialization_alias="codex")
    runtime: str

    def endpoint(self):
        return "lambda"

    async def send(self, client: httpx.AsyncClient, host: str) -> LambdaCreateResponse:
        url = urljoin(host, self.endpoint())
        response = await client.post(url, json=self.model_dump(by_alias=True))

        return LambdaCreateResponse.from_response(response)
