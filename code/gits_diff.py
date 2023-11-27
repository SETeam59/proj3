from subprocess import Popen, PIPE


def gits_diff(args):
	"""
	Function to analyze the current state of a Git repo. It shows difference commits, branches, files and more. 
	Performs operation as similar to git diff command
	"""
	print("Welcome to git diff")
	try:
		subprocess_command = list()
		subprocess_command.append("git")
		subprocess_command.append("diff")
		process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		stdout = stdout.decode("utf-8")
		print(stdout)
		
	except Exception as e:
		print("ERROR: gits diff did not run correctly")
		print("ERROR: {}".format(str(e)))

		return False

	return True