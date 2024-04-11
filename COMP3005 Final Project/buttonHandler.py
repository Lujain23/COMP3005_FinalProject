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

def printMyPayments(email):
    con = function.connectToDatabase()
    return function.printMemberPayments(con,email)

def changePaymentStatus(paymentID,new_status):
    con = function.connectToDatabase()
    return function.changePaymentStatus(con,paymentID,new_status)

'''TRAINER'''
def getMember(firstName):
    con = function.connectToDatabase()
    values = function.getMember(con,firstName)
    return values

def setAvailability(email,start_time,end_time):
    con = function.connectToDatabase()
    return function.setAvailability(con, email, start_time, end_time)

def trainerClasses(email):
    con = function.connectToDatabase()
    return function.trainerViewClasses(con, email)

def getNotifications(email):
    con = function.connectToDatabase()
    return function.getNotifications(con,email)

def deleteNotifications(email):
    con = function.connectToDatabase()
    return function.viewNotifications(con,email)    

'''STAFF'''
def printAllClasses():
    con = function.connectToDatabase()
    return function.printAllClasses(con)

#classes
def staffAddClass(room_used, trainer_email, day,start_time, end_time, type_session, class_type):
    con = function.connectToDatabase()
    return function.classScheduling(con, room_used, trainer_email,day, start_time, end_time, type_session, class_type)
def staffRemoveClass(scheduleID):
    con = function.connectToDatabase()
    function.staffCancelClass(con,scheduleID)
    return True
def staffModifyClass(schedule_id,start_time,end_time):
    con = function.connectToDatabase()
    return function.rescheduleClass(con,schedule_id,start_time,end_time)

#room booking
def printAllRoomBooking():
    con = function.connectToDatabase()
    return function.printAllRoomBooking(con)

def addRoomBooking(room_id, attendees, day,start_time, end_time):
    con = function.connectToDatabase()
    return function.roomBooking(con,room_id, attendees, day,start_time, end_time)

def removeRoomBooking(eventID):
    con = function.connectToDatabase()
    return function.staffCancelRoomBooking(con,eventID)

def modifyRoomBooking(eventID,startTime,endTime):
    con = function.connectToDatabase()
    return function.modifyRoomBooking(con,eventID,startTime,endTime)    

#equipment stuff
def addEquipment(equipmentName,insideRoom):
    con = function.connectToDatabase()
    function.addEquipment(con,equipmentName,insideRoom)
    return True
def updateEquipment(equipmentName):
    con = function.connectToDatabase()
    return function.equipmentMaintenenceMonitoring(con,equipmentName)

def printAllMaintenance():
    con =function.connectToDatabase()
    return function.printMaintenence(con)

#payment styff
def printAllPayments():
    con = function.connectToDatabase()
    return function.printAllPayments(con)
#changing payment status is like the member one

def addPayment(amount, member_email, transaction_date, stat, descript):
    con = function.connectToDatabase()
    return function.createPayment(con, amount, member_email, transaction_date, stat, descript)

def filterPayment(memberEmail):
    con = function.connectToDatabase()
    return function.viewMemberPayments(con,memberEmail)
