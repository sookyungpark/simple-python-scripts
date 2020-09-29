import sys
import platform
import subprocess

def checkRequiredTools(requiredTools):
	cmd = "where" if platform.system() == "Windows" else "which"
	if subprocess.call([cmd] + requiredTools) != 0:
		print("Tools are not installed. Please install " + ",".join(requiredTools))
		sys.exit()

def main():
	checkRequiredTools(["foo"])

if __name__ == "__main__":
	main()
	