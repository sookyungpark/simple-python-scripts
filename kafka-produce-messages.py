from kafka import KafkaProducer

def produceMessages(broker, topic, messages):
	producer = KafkaProducer(bootstrap_servers = broker)
	for msg in messages:
		producer.send(topic, msg.encode("utf-8"))

def main():
	produceMessages("localhost:9092", "topic-1", ["foo", "bar"])

if __name__ == "__main__":
	main()
