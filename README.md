# Real-Time Stock Market Data Streaming Using Kafka

This repository demonstrates a simple implementation of real-time stock market data streaming using Apache Kafka. The project includes a Kafka producer (`producer.py` and `producer.ipynb`) to simulate stock data generation and a Kafka consumer (`consumer.py` and `consumer.ipynb`) to receive and process the streaming data.

## Files

1. **producer.py**
   - Python script showcasing how the Kafka producer works.
   - Sends random data to a Kafka topic named 'test'.
   - Uses the `kafka` library and a JSON value serializer.

2. **consumer.py**
   - Python script illustrating how the Kafka consumer operates.
   - Consumes messages from the 'test' Kafka topic.
   - Utilizes the `kafka` library, JSON value deserializer, and subscribes to the topic.

3. **docker-compose.yaml**
   - Docker Compose configuration file for setting up Kafka and Zookeeper services.
   - Uses ConfluentInc Docker images for Kafka and Zookeeper.

4. **producer.ipynb**
   - Jupyter Notebook version of the Kafka producer.
   - Simulates real-time stock market data streaming.
   - Reads processed stock market data from a CSV file and continuously produces data to the 'stock-data' Kafka topic.

5. **consumer.ipynb**
   - Jupyter Notebook version of the Kafka consumer.
   - Consumes and prints messages from the 'stock-data' Kafka topic.

## Setup

1. Make sure you have Docker and Docker Compose installed.
2. Install the necessary Python libraries using the following command:
   ```bash
   pip install pandas kafka
   ```
3. Run `docker-compose up -d` to start the Kafka and Zookeeper services.
4. Execute the `producer.py` or `producer.ipynb` script to start the data simulation.
5. Run the `consumer.py` or `consumer.ipynb` script to consume and process the streaming data.

## Some Additional Commands for Debugging/Using CLI

### Get into Kafka Bash
```bash
    $ docker-compose exec -it kafka bash
```

### Create a topic with name test
```bash    
    docker-compose exec kafka kafka-console-producer.sh --topic test --broker-list kafka:9092
```
### List Topics
```bash    
    $ docker-compos exec kafka-topics --list --bootstrap-server kafka:9092
```
### Produce Some Message
```bash    
    docker-compose exec kafka kafka-console-producer.sh --topic test --broker-list kafka:9092
```
### Consume Some Message
```bash    
    $ docker-compose exec kafka kafka-console-consumer.sh --topic test --from-beginning --bootstrap-server kafka:9092
```
### Stop Containers
```bash
    $ docker-compose down
```


