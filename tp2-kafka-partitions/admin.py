from kafka import KafkaAdminClient
from kafka.admin import NewPartitions

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")
topic_partitions = {}
topic = "weng"
partitions = NewPartitions(total_count=2)
topic_partitions[topic] = partitions
admin_client.create_partitions(topic_partitions)
