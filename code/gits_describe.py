from subprocess import Popen, PIPE


def gits_describe(args):
	"""
	The command finds the most recent tag that is reachable from a commit..
	"""
	try:
		subprocess_command = list()
		subprocess_command.append("git")
		subprocess_command.append("describe")
		subprocess_command.append("--all")
		
		process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		stdout = stdout.decode("utf-8")

		final = stdout.split("\n")
		final = list(filter(None, final)) 
		for f in final:
			print(f)

		if stderr.decode() != "" :
			print("Error Encountered! \n {}".format(stderr.decode()))
			
	except Exception as e:
		print("ERROR: gits status did not run correctly")
		print("ERROR: {}".format(str(e)))
		return False
	
	return True