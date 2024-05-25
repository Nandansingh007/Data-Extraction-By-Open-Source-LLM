# Import SmartScraperGraph from scrapegraphai.graphs module
from scrapegraphai.graphs import SmartScraperGraph

import nest_asyncio  # Import nest_asyncio module for asynchronous operations
nest_asyncio.apply()  # Apply nest_asyncio to resolve any issues with asyncio event loop

# Configuration dictionary for the graph
graph_config = {
    "llm": {
        "model": "ollama/llama3",  # Specify the model for the llm
        "temperature": 0,  # Set temperature parameter for llm
        "format": "json",  # Specify the output format as JSON for Ollama
        "base_url": "http://localhost:11434",  # Set the base URL for Ollama
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specify the model for embeddings
        "base_url": "http://localhost:11434",  # Set the base URL for Ollama
    },
    "verbose": True,  # Enable verbose mode for debugging purposes
}

# Initialize SmartScraperGraph with prompt, source, and configuration

smart_scraper_graph = SmartScraperGraph(
    #prompt="List all the content",  # Set prompt for scraping
    prompt="List me all the products with their price, Number of Ratings, Product Description, Rating out of 5 if available",

    # Source URL or HTML content to scrape
    source="https://www.daraz.com.np/products/round-neck-soft-feel-cotton-t-shirt-for-men-i128115405-s1035186708.html?spm=a2a0e.11779170.just4u.1.1fdd2d2borwbIU&scm=1007.28811.376629.0&pvid=b6926f13-cee7-4409-ab3f-e2f90beac310&clickTrackInfo=pvid%3Ab6926f13-cee7-4409-ab3f-e2f90beac310%3Bchannel_id%3A0000%3Bmt%3Ahot%3Bitem_id%3A128115405%3B",

    config=graph_config  # Pass the graph configuration
)

# Run the SmartScraperGraph and store the result
result = smart_scraper_graph.run()

# Print the result
print(result)

# Prettify the result and display the JSON
import json

output = json.dumps(result, indent=2)  # Convert result to JSON format with indentation

line_list = output.split("\n")  # Split the JSON string into lines

# Print each line of the JSON separately
for line in line_list:
    print(line) 

