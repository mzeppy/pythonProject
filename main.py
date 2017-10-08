
name = input("Enter your name: ")
print("Hello " + name + "! My name is Howard. I am a robot that can help you. Type help for a list ot commands.")

command = ""

def ex():
	print("Quitting...")


def help():
	print("I am able to interpret the following commands:")
	print("help : displays this help menu")
	print("ex : quits the application")
	print("+ : add two numbers (IE: 2+3)")
	print("- : subtract two numbers (IE: 2-3)")
	print("* : multiply two numbers (IE: 2*3)")
	print("/ : divide two numbers (IE: 2*/3)")

options = {
	'ex': ex, 
	'help': help,
	}

		
def executeCommand(command):
	try:
		options.get(command)()
	except:
		print ("Enter a correct command.")
		
help()

while command!="ex":
	
	#command entered by user
	command = input()
	
	#define calculator operators to split string if an operator is found
	operators = ['+', '-', '*', '/']
	operatorFound = False
	
	if operatorFound!=True:
		
		for i in range(0, len(operators)):
			nums = command.split(str(operators[i]))
		
			if(len(nums)!=1):
				print(str(nums[0]) + " " + operators[i] + " " + str(nums[1]) + " = " + str(eval(command)))
				operatorFound = True
	
	if operatorFound==False: #execute command if no arthmetic operator found
		executeCommand(command)
