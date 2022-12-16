# Kafka-Streaming-Pipeline
Optimizing Bank Marketing Model through building an event streaming pipeline that communicates with a Machine learning model microservice to display the likelihood and status of Bank Customers in real time.

# Proposed Architecture
![](https://github.com/judeleonard/Kafka-Streaming-Pipeline/blob/main/assests/architecture.jpeg)

# Project Description
For this project I chose to go with a Microservice architecture instead of a Monolithic one since Microservices can communicate assynchronously and are independent of one of another, which makes them even more fault tolerant, fast and easily maintainable.


The project comprises of two separate microservices that communicates with each other other i.e __The Data Polling Microservices__ wrapped around Kafka and then the __Machine Learning Model Microservice__ deployed as RESTAPI via docker registry on __Heroku__. [See this repository for model deployment reference](https://github.com/judeleonard/Machine-learning-model-microservice). Unfortunately, this deployment is no longer valid as Heroku does no longer support free hosting services however, I had to utilize the local version of this API which still works nonetheless. 

# About the Dataset
The data for this experiment is downloaded from [Kaggle](https://www.kaggle.com/). The dataset is trained on about 45000 rows of data(downloaded from UCI repository) while the test data for this experiment is over 4000 rows that are streamed to and fro Kafka.

# Kafka Producer sending data to kafka topic
The kafka producer reads each record from the test data and sends it to a kafka topic

![](https://github.com/judeleonard/Kafka-Streaming-Pipeline/blob/main/assests/kafka-producer.gif)


# Kafka Consumer consuming, processing and running model inference for every data send to kafka topic

The kafka consumer on receiving this data via the kafka topic and processes it since the method support assynchronous process, then outputs both the input data and predicted result. Prediction result contains the likelihood of a Bank customer opening a term deposit with the bank, which is a boolean and the probability for that prediction.

![](https://github.com/judeleonard/Kafka-Streaming-Pipeline/blob/main/assests/kafka-consumer.gif)


# Challenges

My major challenge was consuming and manipulating the data after it has been sent to Kafka. After observing the data was not coming in the right format it was sent. It was rather coming in as a tuple object instead of a dict. This made it very difficult to serialize for the model inference. I had to build my own custom json encoder before I could serialize it and parse it as json for model inferencing.
