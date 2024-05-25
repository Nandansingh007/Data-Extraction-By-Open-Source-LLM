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

    #prompt="List all the content",  
    prompt="List me all the products with their Name, price, Number of Ratings, Product Description, Rating out of 5 if available",\
    
    # Source URL or HTML content to scrape
    source = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Product List</title>
                    <style>
                        .product-list {
                            display: flex;
                            flex-wrap: wrap;
                            gap: 16px;
                            justify-content: center;
                        }
                        .product {
                            border: 1px solid #ccc;
                            padding: 16px;
                            max-width: 300px;
                            margin: 16px;
                            text-align: center;
                        }
                        .product img {
                            max-width: 100%;
                            height: auto;
                        }
                        .product h2 {
                            font-size: 1.5em;
                            margin: 0.5em 0;
                        }
                        .product p {
                            margin: 0.5em 0;
                        }
                        .product .price {
                            color: green;
                            font-size: 1.2em;
                            font-weight: bold;
                        }
                        .product .availability {
                            color: red;
                        }
                        .product button {
                            background-color: #28a745;
                            color: white;
                            border: none;
                            padding: 10px 20px;
                            cursor: pointer;
                            font-size: 1em;
                        }
                        .product button:hover {
                            background-color: #218838;
                        }
                    </style>
                </head>
                <body>

                <div class="product-list">
                    <div class="product">
                        <img src="path/to/product1-image.jpg" alt="Product 1">
                        <h2>Product 1</h2>
                        <p class="description">This is a brief description of product 1.</p>
                        <p class="price">$99.99</p>
                        <p class="availability">In Stock</p>
                        <button>Add to Cart</button>
                    </div>
                    
                    <div class="product">
                        <img src="path/to/product2-image.jpg" alt="Product 2">
                        <h2>Product 2</h2>
                        <p class="description">This is a brief description of product 2.</p>
                        <p class="price">$89.99</p>
                        <p class="availability">Out of Stock</p>
                        <button disabled>Out of Stock</button>
                    </div>
                    
                    <div class="product">
                        <img src="path/to/product3-image.jpg" alt="Product 3">
                        <h2>Product 3</h2>
                        <p class="description">This is a brief description of product 3.</p>
                        <p class="price">$79.99</p>
                        <p class="availability">In Stock</p>
                        <button>Add to Cart</button>
                    </div>

                    <!-- Add more products as needed -->
                </div>

                </body>
                </html>
                ''',


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