# HTMLDATA to JSON Conversion Using Large Language Models (LLMs)

## Table of Contents

1. [Possible Solutions](#possible-solutions)
2. [Technology Used](#technology-used)
    - [ScrapeGraph-ai](#scrapegraph-ai)
    - [Ollama](#ollama)
    - [Llama3](#llama3)
    - [Flask](#flask)
3. [Setup](#setup)
    - [Clone the Repository](#clone-the-repository)
    - [Download Ollama](#download-ollama)
    - [Create and Activate a Virtual Environment](#create-and-activate-a-virtual-environment)
    - [Install Requirements](#install-requirements)
    - [Install Playwright](#install-playwright)
    - [Pull Llama3 and Embedding Models](#pull-llama3-and-embedding-models)
4. [Testing](#testing)
    - [app.py](#apppy)
    - [main.py](#mainpy)
5. [Testing of Result and Output](#result-and-output)
6. [Result and Conclusion](#result-and-conclusion)
4. [Further Enhancements](#further-enhancements)

## Possible Solutions

1. **Fine-tuning**: Train a Large Language Model (LLM) on a diverse dataset to accurately convert HTML data into valid JSON.
2. **Context-aware Prompting**: Create prompts that provide the model with context about the dataset to generate JSON output.
3. **Retrieval-Augmented Generation (RAG)**: Break the dataset into blocks and retrieve relevant parts using prompting to facilitate conversion.

## Technology Used

### 1. ScrapeGraph-ai
ScrapeGraphAI is a Python library for web scraping that leverages LLMs and direct graph logic to create scraping pipelines for websites and local documents (XML, HTML, JSON, etc.).

- **URL of Reference**: [ScrapeGraph-ai GitHub Repository](https://github.com/VinciGit00/Scrapegraph-ai)

### 2. Ollama
Ollama is a versatile platform for running LLMs locally on your device. It supports models such as Llama 3, Mistral, Gemma, and Phi 3, among others, facilitating easy deployment and customization.

- **URL**: [Ollama](https://ollama.com/)

### 3. Llama3
Llama 3 is the latest version of Meta's large language model, designed to enhance applications with advanced natural language processing capabilities. It ranges from 8 billion to 70 billion parameters.

### 4. Flask
Flask is a lightweight web framework for Python that simplifies the creation of web applications.

## Setup

### 1. Clone the Repository

  - command: git clone https://github.com/Nandansingh007/Data-Extraction-By-Open-Source-LLM.git

### 2. Download Ollama
  - **URL** : https://ollama.com/download
  - Install the file and make sure it is running
  - Make sure it is running by command: ollama serve

### 3. Create virtual environment and Activate it 
- command: python -m venv .venv
- command: .venv\scripts\activate

### 4. Install requirement file
  - command:	pip install -r requirements.txt


### 5. Install playwright with command 
  - command: playwright install

### 6. Pull Llama3 and embedding:
- command: ollama pull llama3 
- command: ollam pull nomic-embed-text

## Testing

### 1. Use app.py code
- This code is for testing purpose only.
- change the variable (source = URL or HTML block ). Works both for URL or HTML block
- Run this by using command: python app.py

### 2. Use main.py code
- This is Flask API implementation of the code
- Run the code by command: python main.py
- Home page: http://127.0.0.1:8000/
- Testing With URL: http://127.0.0.1:8000/scrape/?url=input_the_url

## Testing of Result and Output

- Dataset : testhtmlblockdata.txt (This is the test result form app.py with dataset in source variable)
<img width="536" alt="image" src="https://github.com/Nandansingh007/Data-Extraction-By-Open-Source-LLM/assets/65103905/ff523db8-e79f-4061-83ac-590c372099d1">


(This below test result output is from api i.e. main.py using 'http://127.0.0.1:8000/scrape/?url=input_the_url' where input_the_url is the url below  )
- URL : https://www.daraz.com.np/products/white-doro-dot-polo-t-shirts-for-men-multisize-fashion-t-shirts-for-men-mens-wear-polo-t-shirts-i127412221-s1034525814.html?spm=a2a0e.searchlistcategory.sku.1.cbe91194tjQZtt&search=1
<img width="940" alt="image" src="https://github.com/Nandansingh007/Data-Extraction-By-Open-Source-LLM/assets/65103905/ef99b363-e41e-439a-a81c-fc0b896b755b">

## Result and Conclusion
- The running of the procedure is slow since it takes pc specification which is much low than required specification to run LLMs
- The testing could take 10-15 mins depending on PC specification

## Further Enhancements
- This use single page scrapper for URL using SmartScraperGraph. So, SeachGraph which is multipage scrapper could be used during fully functional project
- For Prompting using LlaMa3, ollama is used for simple solution in local pc. So for production we can used most powerful LlaMa3 with 70b parameters and write custom prompt for further enhancement
- This is simple API design using Flask. So, it can be enhanced using FastAPI and other API enhancement Techniques
