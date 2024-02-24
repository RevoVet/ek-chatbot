from httpx import AsyncClient
import pytest
from main import app

@pytest.mark.asyncio
async def test_read_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() is not None  # Further checks can be added
