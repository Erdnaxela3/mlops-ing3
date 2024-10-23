from kafka import KafkaProducer

topic = 'exo1'
server_ip = '51.38.185.58:9092'
producer = KafkaProducer(
    bootstrap_servers=server_ip,
)

for _ in range(10):
    producer.send(
        topic,
        value=b'coucou alexandre'
    )

producer.flush()