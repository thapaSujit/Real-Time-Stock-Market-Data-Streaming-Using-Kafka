# Import necessary libraries and modules
from kafka import KafkaConsumer
import json

# Set the Kafka topic
topic = 'test'

# Initialize Kafka consumer with bootstrap servers, auto offset reset to 'earliest', and a JSON value deserializer
consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Consume messages from the Kafka topic
for message in consumer:
    print("consumer")
    message = message.value
    print('Message :{}'.format(message))
