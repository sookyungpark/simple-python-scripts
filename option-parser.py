from optparse import OptionParser

def getOptionParser():
	parser = OptionParser()
	parser.add_option("-s", "--seconds", dest="seconds",
		              help="seconds", default=5)
	parser.add_option("-n", "--name", dest="name",
		              help="name", default="skpark")
	return parser

def main():
	(options, args) = getOptionParser().parse_args()
	print(options.seconds)
	print(options.name)

if __name__ == "__main__":
	main()
	