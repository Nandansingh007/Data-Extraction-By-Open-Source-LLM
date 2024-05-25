# Importing Necessary Library
from flask import Flask, request, jsonify, render_template
import nest_asyncio
from scrapegraphai.graphs import SmartScraperGraph
import json

# Apply nest_asyncio to resolve any issues with asyncio event loop
nest_asyncio.apply()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "Welcome to the Smart Scraper API. Use the /scrape/ endpoint to scrape e-commerce data."})

@app.route('/scrape/', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        url = request.json.get('url')
    else:
        url = request.args.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    graph_config = {
        "llm": {
            "model": "ollama/llama3",
            "temperature": 0,
            "format": "json",
            "base_url": "http://localhost:11434",
        },
        "embeddings": {
            "model": "ollama/nomic-embed-text",
            "base_url": "http://localhost:11434",
        },
        "verbose": True,
    }

    scraper_graph = SmartScraperGraph(
        prompt="List me all the products with their Name, price, Number of Ratings, Product Description, Rating out of 5 if available",
        source=url,
        config=graph_config
    )

    result = scraper_graph.run()

    # Convert result to JSON format with indentation
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
