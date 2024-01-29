# Import necessary libraries and modules
from kafka import KafkaProducer
from time import sleep
import json

# Set the Kafka topic
topic = 'test'

# Initialize Kafka producer with bootstrap servers and a JSON value serializer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Produce 11 messages to the Kafka topic with a 'number' field in the message data
for i in range(11):
    data = {'number': i} 
    producer.send(topic, value=data)
    print("producer")
    sleep(1)  # Introduce a 1-second delay between messages
