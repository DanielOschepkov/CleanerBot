#cleanerBot

print("Enter file directory:\n")
dir = input()
try:
	f = open(dir, 'w')
	f.write("")
	f.close()
except NameError:
	f.close()
	print("No such file or directory")