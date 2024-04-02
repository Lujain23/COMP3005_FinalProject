import functions as function


'''MEMBER'''
def addMember(email,password,firstName,age,gender,height,weight,target,exceriseRoutine):
    con = function.connectToDatabase()
    function.addMember(con,email,password,firstName,age,gender,height,weight,target,exceriseRoutine)
    function.disconnectDatabase(con)
    return True

def validateUser(email,password,userType):
    con = function.connectToDatabase()
    return function.validateUser(con,email,password,userType)

#would return a LIST of everything
def selectMember(email):
    con = function.connectToDatabase()
    values = function.selectMember(con,email)
    return values

def updateMember(email,password,firstName,age,gender,height,weight,target,exceriseRoutine):
    con = function.connectToDatabase()
    function.updateMemberInformation(con,email,password,firstName,age,gender,height,weight,target,exceriseRoutine)
    return True

def printDashboard(email):
    con = function.connectToDatabase()
    return function.printDashboard(con,email)

def printAvailableClasses():
    con = function.connectToDatabase()
    return function.printAvailableClasses(con)

def joinClass(scheduleID,email):
    con = function.connectToDatabase()
    function.joinClass(con, scheduleID, email)
    return True

'''TRAINER'''
def getMember(firstName):
    con = function.connectToDatabase()
    values = function.getMember(con,firstName)
    return values
