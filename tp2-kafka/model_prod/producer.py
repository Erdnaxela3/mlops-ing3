from kafka import KafkaProducer
import json

topic = "WENG"
server_ip = '51.38.185.58:9092'
producer = KafkaProducer(
    bootstrap_servers=server_ip,
)

data = {
    "size": 200.42,
    "nb_rooms": 4,
    "garden": 1,
}

json_string = json.dumps(
    data,
).encode('utf8')

for _ in range(5):
    producer.send(
        topic,
        value=json_string
    )

producer.flush()