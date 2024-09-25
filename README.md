

# TechCrunch News Summarizer

## Overview

This project is a news summarizer app that scrapes articles from TechCrunch and provides users with concise, AI-enhanced summaries of the latest articles. The user can ask questions about recent events, and the app will search through the scraped data and provide summaries of relevant articles. It is built with Python and integrates FAISS for efficient search and OpenAI's GPT model for generating human-like summaries.

## Features

- **Web Scraping**: Data is scraped from TechCrunch using the `scraper.py` script, storing key information like article titles, authors, URLs, and content in a CSV file.
- **Efficient Search**: FAISS is used to index and search through the article content based on user queries.
- **AI Summarization**: GPT-4 is used to summarize the search results, presenting only the most relevant points in a conversational tone to the user.
- **Interactive CLI**: Users can interact with the app by asking questions, and the app will retrieve and enhance relevant articles.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables by creating a `.env` file:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the Scraper**: First, use `scraper.py` to scrape TechCrunch articles and store them in a CSV file.
   ```bash
   python scraper.py
   ```

2. **Run the Main Application**: After scraping, you can launch the interactive summarizer with the `main.py` file.
   ```bash
   python main.py
   ```

3. **Interact with the App**: When prompted, type your query, such as:
   - "Who raised funding in tech lately?"
   - "What's new in the world of AI?"

   The app will search for relevant articles and provide AI-generated summaries.

## Example Queries
- Who raised funding in tech lately?
- What’s new in the world of AI?

## Dependencies

The required dependencies are listed in the `requirements.txt` file, including:

- `requests`
- `beautifulsoup4`
- `python-dotenv`
- `faiss-cpu`
- `langchain`
- `transformers`
- `pandas`
- `numpy`
- `sentence-transformers`
- `openai`
- `pinecone`

Install these dependencies with:
```bash
pip install -r requirements.txt
```

## Files

- **scraper.py**: Script for scraping TechCrunch articles.
- **techcrunch.csv**: Contains scraped article data.
- **main.py**: Main application script for the interactive summarizer.
- **requirements.txt**: List of required dependencies.

## License

This project is for educational purposes.

---

Let me know if you need any more adjustments!
