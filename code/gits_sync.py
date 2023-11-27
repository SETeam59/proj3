import gits_logging
import subprocess
from subprocess import Popen, PIPE

def get_trunk_branch(args):
	"""
	Function to return the trunk branch.
	"""
	try:
		subprocess_command = list()
		subprocess_command.append("git")
		subprocess_command.append("branch")
		subprocess_command.append("-r")
		process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		stdout = stdout.decode("utf-8")
		branches = list(filter(None, stdout.split("\n")))
		trunk=branches[0].split("/")[1]
		return trunk

	except Exception as e:
		print("ERROR: gits branch command caught an exception")
		print("ERROR: {}".format(str(e)))

def get_cur_branch(args):
	"""
	Function to get the current branch
	"""
	try:
		subprocess_git_branch=list()
		subprocess_git_branch.append("git")
		subprocess_git_branch.append("branch")
		process1=Popen(subprocess_git_branch, stdout=PIPE, stderr=PIPE)
		stdout1,stderr1=process1.communicate()
		branch=stdout1.decode("utf-8").split("\n")
		
		for b in branch:
			if "*" in b:
				return b.replace("*","").strip()

	except Exception as e:
		print("ERROR: gits branch command caught an exception")
		print("ERROR: {}".format(str(e)))
        	
def gits_sync(args):
	"""
	Function to sync local master with remote master and rebases the current branch with remote branch branch.
    Used when we want to go back to its stable state. Function is similar to git sync
	"""
	print("Starting to sync...")
	try:

		untracked_stuff = list()
		untracked_stuff.append("git")
		untracked_stuff.append("--porcelain")
		untracked_stuff.append("status")

		process = subprocess.Popen(untracked_stuff,stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		if stdout != b'':
			print("Note: Please commit uncommitted changes")
			exit()

		source=get_trunk_branch(args)
		current=get_cur_branch(args)



		print("Switching to master/main branch")
		checkout_source = list()
		checkout_source.append("git")
		checkout_source.append("checkout")
		checkout_source.append(source)
		process1 = subprocess.Popen(checkout_source, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process1.communicate()
		print(stdout.decode('utf-8'))

		print("Pulling changes from upstream master/main...")
		pull_main = list()
		pull_main.append("git")
		pull_main.append("pull")
		process2 = subprocess.Popen(pull_main, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process2.communicate()
		print(stdout.decode('utf-8'))

		print("Switching to current branch..")
		checkout_current = list()
		checkout_current.append("git")
		checkout_current.append("checkout")
		checkout_current.append(current)
		process3 = subprocess.Popen(checkout_current, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process3.communicate()
		print(stdout.decode('utf-8'))

		print("Rebasing current branch onto the updated source branch..")
		rebase = list()
		rebase.append("git")
		rebase.append("rebase")
		rebase.append(source)
		process4 = subprocess.Popen(rebase, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process4.communicate()
		print(stdout.decode('utf-8'))

	except Exception as e:
		print("ERROR: gits sync command caught an exception")
		print("ERROR: {}".format(str(e)))
		return False
	return True



