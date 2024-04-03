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

def cancelClass(scheduleID,email):
    con = function.connectToDatabase()
    function.cancelClass(con,scheduleID,email)
    return True

def printMembersClass(email):
    con = function.connectToDatabase()
    return function.printMembersClasses(con,email)
    
def rescheduleClass(schedule_id,start_time,end_time):
    con = function.connectToDatabase()
    return function.rescheduleClass(con,schedule_id,start_time,end_time)

def printSoloClass(email):
    con = function.connectToDatabase()
    return function.printSoloMemberClasses(con,email)


'''TRAINER'''
def getMember(firstName):
    con = function.connectToDatabase()
    values = function.getMember(con,firstName)
    return values

def setAvailability(email,start_time,end_time):
    con = function.connectToDatabase()
    return function.setAvailability(con, email, start_time, end_time)


'''STAFF'''
def printAllClasses():
    con = function.connectToDatabase()
    return function.printAllClasses(con)

def staffAddClass(room_used, trainer_email, start_time, end_time, type_session, class_type):
    con = function.connectToDatabase()
    return function.classScheduling(con, room_used, trainer_email, start_time, end_time, type_session, class_type)