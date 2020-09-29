import subprocess
from threading import Timer

def catMessages(timeoutSec, broker, topic):
	proc = subprocess.Popen(["kafkacat", "-b", broker, "-t", topic], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	timer = Timer(timeoutSec, proc.kill)
	try:
		timer.start()
		stdout, stderr = proc.communicate()
	finally:
		timer.cancel()
	return stdout

def main():
	out = catMessages(5, "localhost:9092", "topic-1")
	print(out)

if __name__ == "__main__":
	main()
