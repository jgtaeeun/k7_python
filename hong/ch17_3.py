#stauts_code 가  200임을 확인하는 방법 1>requests를 통한 status_code가 200인지 확인
#headers = {"Accept": "application/vnd.github.v3+json"}
#r = requests.get(url, headers=headers)
#print(f"Status code: {r.status_code}")


#stauts_code 가  200임을 확인하는 방법 2>pytest를 사용해서 status_code가 200인지 확인
#터미널에서 설치(python -m pip install pytest)(python -m pip install pytest-asyncio)( python -m  pip install httpx)
#( python -m pip install fastapi)

import json
import pytest
from httpx import AsyncClient

async def test_root():
    async with AsyncClient(base_url="https://api.github.com/search/repositories") as ac:
        response = await ac.get("?")
        assert response.status_code == 200
        assert response.json() == {"msg": "successful for api"}

url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
