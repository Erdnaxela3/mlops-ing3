from kafka import KafkaConsumer, TopicPartition

topic = "weng"
server_ip = "localhost:9092"


consumer = KafkaConsumer(
    bootstrap_servers=server_ip,
    group_id="grp1",
)

topic_partition = TopicPartition(topic, 1)
consumer.assign([topic_partition])

for msg in consumer:
    print(msg.value, "received from partition", msg.partition)
