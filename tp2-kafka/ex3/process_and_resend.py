from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np

topic = "WENG"
server_ip = '51.38.185.58:9092'
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=server_ip
)

producer = KafkaProducer(
    bootstrap_servers=server_ip,
    value_serializer=lambda x: x.to_bytes(4, byteorder='big'),
)

for msg in consumer:
    data = json.loads(msg.value)
    arr = np.array(data['data'])
    arr_sum = int(np.sum(arr))

    producer.send(
        topic="processed",
        value=arr_sum,
    )
    producer.flush()