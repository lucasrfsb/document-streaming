# document-streaming
Repository for the Document streaming capstone projects

# How it works
Dockerized Document Streaming ETL, with FastAPI to ingest the data from customer.Kafka streaming to buffer the requests. Spark to process the data, and integrate with MongoDB for document storage. Ending with UI customer's search with Streamlit.

# How to run
1- Install WSL if you're in a Windows machine  
2- deploy the api-ingestion on docker on the 'API-Ingest' folder and name the image as 'api-ingestion'  
3- Create 'mytesttopic' and 'spark-output' topics on Kafka  
4- Run the docker-compose 'docker-compose-kafka-spark-mongodb.yml'  
5- Create a db named 'docstreaming' and a collection named 'invoices' in MongoDB  
6- Run the Spark streaming processing and producing to the 'spark-output' topic  
7- To automatize a testing client inputs, go to the client's folder and run the 'api-client.py'  
8- Make your customer's search in the Streamlit UI. 

# Next steps
- Deploy the streamlit app as docker (build and add in dockerfile)
- Deploy the whole platform with all containers on a cloud platform of your choice
- Add an API between Streamlit and MongoDB so that Streamlit doesnt have to be directly connected with MongoDB (User& Password)
- Run this project on Cloud
- What if the data was stored in a relational model?

# Links to deploy the streamlit app as docker container
https://maelfabien.github.io/project/Streamlit/#the-application  
https://towardsdatascience.com/how-to-deploy-a-semantic-search-engine-with-streamlit-and-docker-on-aws-elastic-beanstalk-42ddce0422f3

# Credits
Special thanks to the idealist of the project, Andreas Kretz. Meet his projects at https://github.com/team-data-science/ and his Data Engineering learning course at https://learndataengineering.com/
