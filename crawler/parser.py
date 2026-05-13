from bs4 import BeautifulSoup
from urllib.parse import urljoin


def parse(html: str, base_url: str):
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup(["script", "style"]):
        tag.decompose()
    text = soup.get_text(separator=" ", strip=True)
    links = [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True)]
    return text, links