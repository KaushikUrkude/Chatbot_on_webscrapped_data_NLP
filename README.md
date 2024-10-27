
# Chatbot on Web-Scraped Data

This project features an advanced chatbot designed to provide accurate answers based on web-scraped data. The chatbot integrates sophisticated web crawling, data chunking, and vector database techniques. It employs a hybrid retrieval approach, combining BM25 and BERT-based methods for efficient data retrieval and re-ranking, thereby enhancing the user experience.




## Features

1. web_crawler
Description: Contains code for scraping data from websites and their sub-links up to 5 levels deep.

2. data_processing
Description: Includes scripts for cleaning, processing, and preparing the scraped data for further analysis.

3. create_embedding
Description: Scripts for generating embeddings from the processed data.

4. chunking_cosine_similarity
Description: Implements data chunking based on cosine similarity between sentences or topics.

5. uploading_embeddings_milvus
Description: Code for uploading the generated embeddings into the MILVUS vector database.

6. qna_model
Description: Contains the implementation of the question-answering model that uses the embeddings to respond to user queries.

7. docker_and_milvus_config
Description: Configuration files and scripts for setting up Docker containers and configuring MILVUS.
Key Files: Dockerfile, docker-compose.yml, milvus_config.yml


## Getting Started

To run this project

```bash
  git clone https://github.com/KaushikUrkude/Chatbot_on_webscrapped_data_NLP.git
cd NLP-Basics
```

Install dependencies:

1.Use pip to install any necessary libraries (such as nltk, sklearn, or gensim), as listed in each notebook.

Open VsCode:<br/>
2.Start Vscode and run each file sequentially as in reposotory.

Setup Docker:<br/>
**Prerequisites:**
1.Install Docker: Make sure Docker is installed on your machine. 
You can download and install Docker from the official Docker website.

1.Install Docker Compose: Docker Compose is included with Docker Desktop 
for Windows and macOS. For Linux, you might need to install it separately. 
Check the official installation guide for details.

**Steps**
1.Navigate to the Project Directory:<br/>
 Open your terminal and navigate to the directory containing your docker-compose.yml 
 file using the cd command.
 For example: cd /path/to/your/project

2.Run 'docker-compose up': <br>
In the terminal, run the following command:
```bash
  docker-compose up
```
  This command will start all the services defined in your docker-compose.yml file.
