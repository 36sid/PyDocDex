import httpx
import logging

logger = logging.getLogger(__name__)

def fetch(url: str) -> str | None:
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        return response.text
    except (httpx.RequestError, httpx.HTTPStatusError) as exc:
        logger.error(f"An error occurred while fetching {url}: {exc}")
        return None