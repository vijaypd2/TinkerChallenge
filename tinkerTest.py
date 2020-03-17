class Student:
    'common base class for all registered learners and mentors'
    stack = []
    timeAvail = 0

    def __init__(self,name):
        self.name = name
        print(self.name)

    def addStacks(self,interest):

        Student.stack.append(interest)
        for x in Student.stack:
            print(x)

    def setMentorOrLearner(self,cho):
        if cho == 0:
            self.role = 0   # value 0 for Mentor
        if cho == 1:
            self.role = 1   # value 1 for Student
        print(self.role)
    def setAvailableTime(self,time):
        Student.timeAvail = time

    def getMentor(self,expertiseNeed,intStack,time):
        for x in intStack:
            if x == expertiseNeed:
                if time != 0:
                    print("This can be mentor")
                else:
                    print("No time")
            else:
                print("No mentor for this interest")

    
def runCode():
    rname=input("Enter your name: ")
    stud = Student(rname)

    a=input("0.Mentor\n1.Student\n:")
    stud.setMentorOrLearner(int(a))
    x=0
    while x == 0:
        skill = input("Enter your Interest or Expertise: ")
        stud.addStacks(skill)
        x = int(input("\n1.Exit\n0.Continue:"))
   
    mainStack = []
    mainStack.append(stud)
    for x in mainStack:
        print(x.name)

    if stud.role == 1:
        for x in mainStack:
            stud.getMentor(stud.stack[0],x.stack,x.timeAvail)


runCode()   





