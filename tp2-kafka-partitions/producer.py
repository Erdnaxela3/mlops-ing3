from kafka import KafkaProducer

topic = "weng"
server_ip = "localhost:9092"
producer = KafkaProducer(
    bootstrap_servers=server_ip,
)

producer.send(topic, value=b"coucou alexandre")
producer.flush()
