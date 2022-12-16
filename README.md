# Kafka-Streaming-Pipeline
Optimizing Bank Marketing Model through building an event streaming pipeline that communicates with a Machine learning model microservice to display the likelihood and status of Bank Customers in real time.

# Proposed Architecture
![](https://github.com/judeleonard/Kafka-Streaming-Pipeline/blob/main/assests/architecture.jpeg)

# Project Description
For this project I chose to go with a Microservice architecture instead of a Monolithic one since Microservices can communicate assynchronously and are independent of one of another, which makes them even more fault tolerant, fast and easily maintainable.


The project comprises of two separate microservices that communicates with each other other i.e __The Data Polling Microservices__ wrapped around Kafka and then the __Machine Learning Model Microservice__ deployed as RESTAPI via docker registry on __Heroku__. [See this repository for model deployment reference](https://github.com/judeleonard/Machine-learning-model-microservice). Unfortunately, this deployment is no longer valid as Heroku does no longer support free hosting services however, I had to utilize the local version of this API which still works nonetheless. 
