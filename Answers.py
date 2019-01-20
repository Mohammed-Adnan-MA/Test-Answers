#1: Module:

#Reading data function
def readingData(name, age, length):
	name= raw_input("Enter a name to check: ")
	age= raw_input("Enter the age you want to check: ")
	length= raw_input("Enter a name to calculate its length: ")
	return name, age, length

#A
def checkFirstAndLastLetters(name):
	if name[0].lower()==name[-1].lower():
		return True
	else:
		return False
			

#print checkFirstAndLastLetters("")

#B
def checkAge(age):
	if age>="20" and age<="30":
		return "Young"
	elif age>"30":
		return  "Old"

#print checkAge()

#C
def checkTheLengthOfTheName(length):
	return len(length)

#print checkTheLengthOfTheName("")

####################################

#Application: A & B & C:
class Details():
	def __init__(self, name, age, title):
		self.name, self.age, self.title= readingData(name, age, length)



 
	
class One(Details):
	def __init__(self, name, age, title):
		Details.__init__(self, name, age, title)
		print checkFirstAndLastLetters(self.name)
		print checkAge(self.age)
		print checkTheLengthOfTheName(self.title)


name=""
age=0
length=""
One(name, age, length)
################################################

#2
while True:
	name_input= raw_input("Enter a name: ")
	for i in range(len(name_input)):
		if name_input[i].lower()=="t":
			break
	if name_input[i].lower()=="t":		
		break

################################################

#3
#A
txt=['a','b','d','a','l','r','a','h','m','a','n']
good= "".join(txt)
print good

#B
counter=0
for i in range(len(good)):
	if good[i].lower()=="a":
		counter+=1
print counter

#C
replace= good.replace("d","c")
good= replace
replace= good.replace("h","k")
good= replace
print good

#D
n= good[:good.find("l")] + good[good.find("l")+1:]
print n

