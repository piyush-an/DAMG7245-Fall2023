---
draft: false 
date: 2023-10-31
authors:
  - piyush
categories:
  - LLM
---

# Pathway's LLM (Large Language Model) App

This is referred from https://github.com/pathwaycom/llm-app

## Reproducibility

The codebase underwent a few updates:

- Integration of Streamlit within a container.
- Utilization of Docker Compose to initiate both containers.
- Inclusion of a sample .env file.

These changes have been implemented and are available at [piyush-an/llm-app](https://github.com/piyush-an/llm-app)


## Sample Query

1. How to use LLMs in Pathway?
```bash
$ curl --data '{"user": "user", "query": "How to use LLMs in Pathway?"}' http://localhost:8080/
"LLMs (Louvain Local Modularity) can be used in Pathway by following these steps:\n\n1. Import the necessary modules:\n   ```python\n   from pathway.stdlib.graphs.louvain_communities import LLM\n   ```\n\n2. Create an instance of the LLM"
```

2. How to connect to Kafka in Pathway?
```bash
$ curl --data '{"user": "user", "query": "How to connect to Kafka in Pathway?"}' http://localhost:8080/
"To connect to Kafka in Pathway, you can use the `pathway.io.kafka` package. This package provides the necessary connectors for reading and writing data from and to Kafka streams."
```

## Observation

1. The knowledge base is structured data stored in the form of a dictionary in the folder location `examples/data/pathway-docs`.
2. The app does not use a vector database and offers real-time retrieval of data from the knowledge base.
3. The knowledge base can be updated in real time to add more files.
4. Users have the option to utilize the Hugging Face model in place of OpenAI.
5. Other available options for the knowledge base include PDF, HTML, DOCX, PPTX stored locally or on S3, and a SQL database.

