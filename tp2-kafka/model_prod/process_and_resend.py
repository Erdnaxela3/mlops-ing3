from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np
import joblib

model_path = 'regression.joblib'
model = joblib.load(model_path)

topic = "WENG"
output_topic = f"prediction_{topic}"
server_ip = '51.38.185.58:9092'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=server_ip,
    group_id=f'{topic}_consumer_group'
)

producer = KafkaProducer(
    bootstrap_servers=server_ip,
)

for msg in consumer:
    try:
        data = json.loads(msg.value)
        size = data['size']
        nb_rooms = data['nb_rooms']
        garden = data['garden']

        prediction = float(model.predict([[size, nb_rooms, garden]])[0])
    except:
        prediciton = -1

        data = {
            "prediction": prediction,
        }
        json_string = json.dumps(
            data,
        ).encode('utf8')

        producer.send(
            topic=output_topic,
            value=json_string,
        )
        producer.flush()