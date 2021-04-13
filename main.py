import sys
import file_mng
import command as cmnd
import os

mng = file_mng.Manager ("Firebase.Auth.dll")

command = cmnd.Interpreter ()
command.addCommand ("add", mng.add)
command.addCommand ("get", mng.get)
command.addCommand ("reset", mng.reset)

if __name__ == "__main__":
	args = sys.argv
	if len (args) == 1:
		while True:
			command.call (input ("--- "))
	else:
		string = ""
		for i in args [1:]:
			string += f'"{i}"'
		command.call (string)