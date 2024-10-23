from kafka import KafkaConsumer

topic = 'processed'
server_ip = '51.38.185.58:9092'
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=server_ip,
)

for msg in consumer:
    print (msg)