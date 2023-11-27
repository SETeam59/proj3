from subprocess import Popen, PIPE


def gits_tag_func(args):
	"""
	Function to tag a commit which is used to capture a point in history 
	that is used for a marked version release
	"""

	print('Welcome to gits tag')
	try:
		subprocess_command = list()
		subprocess_command.append("git")
		subprocess_command.append("tag")

		command_num = int(input('''
		Enter the command number that you want to execute:
		1. gits tag (List all tags)
		2. gits tag <tag_name> (Add a new tag)
		3. gits checkout <tag_name> (Checkout to a particular tag)	
		'''))
		
		# print(command_num)
		if command_num == 1:
			process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
			stdout, stderr = process.communicate()
			stdout = stdout.decode("ascii")
			final = stdout.split("\n")
			final = list(filter(None, final)) 
			for f in final:
				print(f)
			print("gits tag executed successfully")
				
		elif command_num == 2:
			tag_name = input("Enter the tag name:")
			subprocess_command.append(tag_name)
			process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
			stdout, stderr = process.communicate()
			print("gits tag ", tag_name, " executed successfully")
			
		elif command_num == 3:
			subprocess_command.remove("tag")
			subprocess_command.append("checkout")
			tag_name = input("Enter the tag name:")
			subprocess_command.append(tag_name)
			process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
			stdout, stderr = process.communicate()
			stdout = stdout.decode("ascii")
			final = stdout.split("\n")
			final = list(filter(None, final)) 
			for f in final:
				print(f)
			
			if stderr:
				stderr = stderr.decode("ascii")
				final1 = stderr.split("\n")
				final1 = list(filter(None, final1))
				for f in final1:
					print(f)

			print("gits checkout ", tag_name, " executed successfully")
			
		else:
			print("Invalid command")
				
	except Exception as e:
		print("ERROR: gits tag command caught an exception")
		print("ERROR: {}".format(str(e)))

