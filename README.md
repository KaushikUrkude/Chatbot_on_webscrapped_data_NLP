Chatbot on Web-Scraped Data
Overview
This project demonstrates a sophisticated chatbot built on web-scraped data. The chatbot leverages advanced web crawling, data chunking, and vector database techniques to answer user queries accurately. It utilizes a hybrid retrieval approach combining BM25 and BERT-based methods for effective data retrieval and re-ranking, enhancing the overall user experience.

Features
1_web_crawler
Description: Contains the code for scraping data from websites and their sub-links up to 5 levels deep.

2_data_processing
Description: Includes scripts for cleaning, processing, and preparing the scraped data for further analysis.

3_Create_embedding
Description: Scripts for generating embeddings from the processed data.

4_Chunking_cosine_similarity
Description: Implements data chunking based on cosine similarity between sentences or topics.

5_uploading_Embeddings_MILVUS
Description: Code for uploading the generated embeddings into the MILVUS vector database.

6_qna-model
Description: Contains the implementation of the question-answering model that uses the embeddings to answer user queries.
Docker_and_Milvus_Config

Description: Configuration files and scripts for setting up Docker containers and configuring MILVUS.
Key Files: Dockerfile, docker-compose.yml, milvus_config.yml
