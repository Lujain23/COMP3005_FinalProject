import psycopg2


#returns the cursor to execute
def connectToDatabase():
    try:
        #would change depending on the user
        password = "admin" #trista
        password = "comp3005" #lujain
        database = "GymManagementSystem"
        #database = "COMP3005FinalProject"

        connection = psycopg2.connect( database = database,
                                    host = "localhost",
                                    password = password,
                                    user = "postgres",
                                    port = "5432")
        
        print("Connected to Database!")


        #make it return the connection? still thinking of how it would be used.
        return  connection
   
    except psycopg2.Error as e:
        print(e)


def disconnectDatabase(connection):
    if connection is not None:
        connection.close()
        print("Connection Closed.")


def testingSelect(cursor):
    cursor.execute("SELECT * from students")
    ans = cursor.fetchall()
    
    print(ans)
    for row in ans:
        print("name is: " + row[1] + " " + row[2])

def validateUser(connection,username,password,memberType):
    cursor = connection.cursor()
    ans = []
    try:
        query = "SELECT * FROM {} WHERE email = %s AND passwd = %s".format(memberType)
        cursor.execute(query,(username,password))
        ans = cursor.fetchall()
        if(len(ans) == 1):
            print("exists")
            return True
        else:
            print("no no no")
            return False
    except psycopg2.DatabaseError as e:
        print("Error in ValidateUser!")

#Member Functions
def selectMember(connection,email):
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM members WHERE email = %s"
        cursor.execute(query,(email,))
        ans = cursor.fetchall()
        return ans
    except psycopg2.DatabaseError as e:
        print("Error selecting member!")
    return


def addMember(connection, email, passwd, first_name, age, gender, height, weight, target_weight, exercise_routine):
    cursor = connection.cursor()
    try:
        query = "INSERT INTO members (email, passwd, first_name, age, gender, height, weight, target_weight, exercise_routine) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (email, passwd, first_name, age, gender, height, weight, target_weight, exercise_routine))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error adding member!")
    return  

def updateMemberInformation(connection, email, passwd, first_name, age, gender, height, weight, target_weight, exercise_routine):
    cursor = connection.cursor()
    try:
        query = "UPDATE members SET passwd = %s, first_name = %s, age = %s, gender = %s, height = %s, weight = %s, target_weight = %s, exercise_routine = %s WHERE email = %s"
        cursor.execute(query, (passwd, first_name, age, gender, height, weight, target_weight, exercise_routine, email))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error updating member information!")
    return

def printDashboard(connection, email):
    # Displaying exercise routines, fitness achievements, health statistics
    cursor = connection.cursor()
    try:
        # Fitness achievements???????????????
        query = "SELECT exercise_routine FROM members WHERE email = %s"
        cursor.execute(query, (email,))
        exercise_routine = cursor.fetchall()
        query = "SELECT height FROM members WHERE email = %s"
        cursor.execute(query, (email,))
        height = cursor.fetchall()
        query = "SELECT weight FROM members WHERE email = %s"
        cursor.execute(query, (email,))
        weight = cursor.fetchall()
    except psycopg2.DatabaseError as e:
        print("Error printing dashboard!")
    return

def joinClass(connection, room_used, member_email, trainer_email, start_time, end_time, type_session, class_type):
    cursor = connection.cursor()
    try:
        query = "INSERT INTO schedule (room_used, member_email, trainer_email, start_time, end_time, type_session, class_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (room_used, member_email, trainer_email, start_time, end_time, type_session, class_type))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error joining class!")
    return

def rescheduleClass(connection):
    cursor = connection.cursor()
    return

def cancelClass(connection, schedule_id):
    cursor = connection.cursor()
    try:
        query = "DELETE FROM schedule WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id, ))
        connection.commit()
        query = "DELETE FROM scheduleStudents WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id, ))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error cancelling class!")
    return

#Trainer Functions
# "timing during the week and its start and end dates"
# Should we add start and end dates to the trainer table?
def setAvailability():
    return

def getMember(connection, first_name):
    cursor = connection.cursor()
    try:
        query = "SELECT first_name, age, gender, height, weight, target_weight, exercise_routine FROM members WHERE first_name = %s"
        cursor.execute(query, (first_name,))
        result = cursor.fetchall()
        return result
    except psycopg2.DatabaseError as e:
        print("Error getting member!")
    return 

#staff functions
# "Room booking management entails assigning a room to a class or any other event, such as a birthday party
# For room booking, administrators can inquire about:
#   The designated room
#   The type of event (class, birthday, etc.)
#   The room management component must, based on the event schedule, verify room availability. If the room is not available, it prompts the administrator to select an alternative option."
# Admin makes the bookings right? Members and trainers can't? (If someone wants to book something, the admin must do it on their behalf)

def roomBooking():
    # We could have a room table with room_id, start_time, end_time, date, eventType and then add to the room's schedule if the times don't overlap
    return

# "Class scheduling involves assigning members and trainers to a class, then determining its timing during the week and its start and end dates."
# Literally what. Does the staff make the class schedules? How would that work?
def classScheduling():
    return

def equipmentMaintenenceMonitoring(connection, equipment_name):
    cursor = connection.cursor()
    # Just update date in equipment
    try:
        query = "UPDATE equipment_maintenence SET last_checked = %s WHERE equipment_name = %s"
        cursor.execute(query, (equipment_name, ))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error monitoring equipment!")
    return 





def main():
    connection = connectToDatabase()
    #testingSelect(cursor)


    #validateUser(cursor,'Jim','Beam','students')
    #validateUser(cursor,'hey','Beam','students')
    
    #addMember(connection, 'test', 'test', 'test', 2, 'M', 5, 2, 5, 'round')
    #updateMemberInformation(connection, 'test', 'test', 'testING', 4, 'M', '5', '2', '5', 'rotund')
    #printDashboard(connection, 'test')
    #joinClass(connection, 1, 'test', 'trainerTest', '09:00:00', '10:00:00', 'solo', 'cardio')
    getMember(connection, 'testING')
    #print(validateUser(connection,'lujain@gmail.com','lujain','members'))
    print(selectMember(connection,'lujain@gmail.com'))
#main()