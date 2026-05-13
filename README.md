# PyDocDex

A search engine that crawls Python documentation and lets you query it locally.
Built from scratch as a learning project — crawler, inverted index, BM25 ranking, and a simple web UI.

## Features

- Async web crawler with politeness rules (robots.txt, rate limiting)
- Inverted index with BM25 scoring
- Snippet extraction with matched term highlighting
- Simple search UI built with Flask      

## Setup
```
git clone https://github.com/36sid/PyDocDex.git
cd PyDocDex
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

# Run the crawler and indexer
python main.py

# Start the search UI
```
python app.py
```

Then open http://localhost:5000 in your browser.

## Configuration

Copy .env.example to .env and edit:

SEED_URL=https://docs.python.org/3/

CRAWL_DEPTH=2

DB_PATH=search.db


## Tech stack

- httpx — async HTTP
- BeautifulSoup4 + lxml — HTML parsing
- nltk — tokenization and stemming
- SQLite — storage
- Flask — search UI

## Status

Work in progress. Building phase by phase.
