# Kafka-Streaming-Pipeline
Optimizing Bank Marketing Model through building an event streaming pipeline that communicates with a Machine learning model microservice to display the likelihood and status of Bank Customers in real time.

# Proposed Architecture
![](https://github.com/judeleonard/Kafka-Streaming-Pipeline/blob/main/assests/kafka-architecture.jpeg)

# Project Description
For this project I chose to go with a Microservice architecture instead of a Monolithic one since Microservices can communicate asynchronously and are independent of one of another, which makes them even more fault tolerant, fast and easily maintainable.


The project comprises of two separate microservices that communicates with each other other i.e __The Data Polling Microservices__ wrapped around Kafka and then the __Machine Learning Model Microservice__ deployed as RESTAPI via docker registry on __Heroku__. [See this repository for model deployment reference](https://github.com/judeleonard/Machine-learning-model-microservice). Unfortunately, this deployment is no longer valid as Heroku does no longer support free hosting services however, I had to utilize the local version of this API which still works nonetheless. 

# About the Dataset
The data for this experiment is downloaded from [Kaggle](https://www.kaggle.com/). The dataset is trained on about 45000 rows of data(downloaded from UCI repository) while the test data for this experiment is over 4000 rows that are streamed to and fro Kafka.

# Kafka Producer sending data to kafka topic
The kafka producer reads each record from the test data and sends it to a kafka topic

![](https://github.com/judeleonard/Kafka-Streaming-Pipeline/blob/main/assests/kafka-producer.gif)


# Kafka Consumer consuming, processing and running model inference for every data send to kafka topic

The kafka consumer on receiving this data via the kafka topic, processes it since the method support asynchronous process. It then outputs both the input data and predicted result. Prediction result contains the likelihood of a Bank customer opening a term deposit with the bank, which is a boolean and the probability for that prediction.

![](https://github.com/judeleonard/Kafka-Streaming-Pipeline/blob/main/assests/kafka-consumer.gif)


# Challenges

My major challenge was consuming and manipulating the data after it has been sent to Kafka. After observing the data was not coming in the right format it was sent. It was rather coming in as a tuple object instead of a dict. This made it very difficult to serialize for the model inference. I had to build my own custom json encoder before I could serialize it and parse it as json for model inferencing.


# How to run the Project
    
   - To start installation of services and set up, run the below command:
   
   
              docker-compose up

      __Note__: running the docker command automatically creates a topic which is a bash command which I have included in the docker config file. Incase       you wish to Manually create your own topic without having them created automatically prior to running the compose command. After cloning this repo       edit the docker file by removing the kafka-create topic service as shown below;
      
                  kafka-create-topics:
                  image: confluentinc/cp-kafka:5.2.0
                  depends_on:
                    - broker
                  hostname: kafka-create-topics
                  command: "bash -c 'echo Waiting for Kafka to be ready... && \
                                     cub kafka-ready -b kafka:9092 1 20 && \
                                     kafka-topics --create --topic customer_pred --if-not-exists --zookeeper zookeeper:2181 --partitions 2 --replication-factor 1 && \
                                     sleep infinity'"
                                     
                                     
                                     
       Once removed you can Manually create as many topic as you want from your terminal after the `docker compose command` is done installing and        setting up as shown below:
                   
                   docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --topic <your topic name> --create
                   
                   
  - Create a virtual env and run:
              
                pip install -r requirements.txt
                
  - To start the producer run:
                 
                 python3 simulation.py
                 
   __Note__: Before running the consumer to start consuming data sent to our destination kafka topic. Make sure the model micro service API is running in the background also since we are utilizing the local version of the API.
   
   - To consume data and run model inferencing on every data sent. Run the below command:
                 
                 faust -A customer_prediction worker -l info
                 
      If we need more workers to load and process the data we can also start an additional worker.
      
      
      
 # Other things we can try

We can also stream our data to focus on a particular business metric. Let's assume a situation whereby the bank wish to run this model real time prediction only on customers between a certain age limit. We can simply leverage this asynchronous process
to capture the age field, parse in our condition and forward all incoming data to that event. In this case, a new Kafka topic to capture only this business metric. 
      
__Feel free to reach out incase anything here doesn't work as expected__.
                 
     
