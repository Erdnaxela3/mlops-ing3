from kafka import KafkaConsumer
import json
import numpy as np

topic = "WENG"
server_ip = '51.38.185.58:9092'
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=server_ip,
)


for msg in consumer:
    data = json.loads(msg.value)
    arr = np.array(data['data'])
    print(np.sum(arr))