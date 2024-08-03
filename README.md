Chatbot on Web-Scraped Data
Overview
This project features an advanced chatbot designed to provide accurate answers based on web-scraped data. The chatbot integrates sophisticated web crawling, data chunking, and vector database techniques. It employs a hybrid retrieval approach, combining BM25 and BERT-based methods for efficient data retrieval and re-ranking, thereby enhancing the user experience.

Features
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
