import psycopg2
from datetime import date, datetime
import math

#returns the cursor to execute
def connectToDatabase():
    try:
        #would change depending on the user
        #password = "admin" #trista
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
    cursor.execute("SELECT * from equipment_maintenence")
    ans = cursor.fetchall()
    
    print(ans)
    for row in ans:
        print("name is: " + row[2])

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
    cursor = connection.cursor()
    try:
        # Getting info
        query = "SELECT exercise_routine FROM members WHERE email = %s"
        cursor.execute(query, (email,))
        exercise_routine = cursor.fetchall()
        query = "SELECT height FROM members WHERE email = %s"
        cursor.execute(query, (email,))
        height = cursor.fetchall()
        query = "SELECT weight FROM members WHERE email = %s"
        cursor.execute(query, (email,))
        weight = cursor.fetchall()
        query = "SELECT target_weight FROM members WHERE email = %s"
        cursor.execute(query, (email,))
        target_weight = cursor.fetchall()
        # Calculate BMI
        BMI = round(weight[0][0] / (((height[0][0])/100)**2),2)
        isOverweight = BMI > 24.9
        weightChange = abs(weight[0][0] - target_weight[0][0])
        if weightChange == 0:
            achievement = "Congrats! You're achieved your target weight"
        else:
            achievement = "No achievement"

        # exercise_routine -> String of like "formula chasing"
        # height, weight, target_weight, BMI -> ints
        # isOverweight -> boolean
        # weightChange -> int
        # achievement -> String (achievement/none)
        return exercise_routine[0][0], height[0][0], weight[0][0], target_weight[0][0], BMI, isOverweight, weightChange, achievement
    except psycopg2.DatabaseError as e:
        print("Error printing dashboard!")
    return

def joinClass(connection, schedule_id, member_email):
    cursor = connection.cursor()
    try:
        query = "INSERT INTO scheduleStudents (schedule_id, member_email) VALUES (%s, %s);"
        cursor.execute(query, (schedule_id, member_email))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error joining class!")
    return

def cancelClass(connection, schedule_id, member_email):
    cursor = connection.cursor()
    try:
        query = "DELETE FROM scheduleStudents WHERE schedule_id = %s AND member_email = %s"
        cursor.execute(query, (schedule_id, member_email))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error cancelling class!")
    return

def printAvailableClasses(connection):
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM schedule s LEFT JOIN scheduleStudents stu ON s.schedule_id = stu.schedule_id WHERE stu.schedule_id IS NULL OR type_session = 'group'"
        cursor.execute(query)
        return(cursor.fetchall())

    except psycopg2.DatabaseError as e:
        print("Error printing available classes!")
    return

def printMembersClasses(connection, member_email):
    cursor = connection.cursor()
    try:
        query = "SELECT stu.schedule_id, room_used, trainer_email, start_time, end_time, type_session, class_type FROM schedule s LEFT JOIN scheduleStudents stu ON s.schedule_id = stu.schedule_id WHERE stu.schedule_id IS NOT NULL AND member_email = %s"
        cursor.execute(query, (member_email, ))
        return(cursor.fetchall())
    except psycopg2.DatabaseError as e:
        print("Error printing classes member joins!")   
    return

#Trainer Functions
# Just changing start_time, end_time
def setAvailability(connection, email, start_time, end_time):
    cursor = connection.cursor()
    try:
        query = "UPDATE trainer SET start_time = %s, end_time = %s WHERE email = %s"
        cursor.execute(query, (start_time, end_time, email))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error setting availability!")
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

# helper function
def findOverlaps(cursor, room_id, start_time, end_time):
    # Convert to date time object
    start_time_to_datetime = datetime.strptime(start_time, '%H:%M:%S').time()
    end_time_to_datetime = datetime.strptime(end_time, '%H:%M:%S').time()

    # get room_id and check the schedules in eventInfo and schedule
    query = "SELECT start_time, end_time FROM eventInfo WHERE room_used = %s UNION SELECT start_time, end_time FROM schedule WHERE room_used = %s"
    cursor.execute(query, (room_id, room_id))
    result = cursor.fetchall()

    # Check start and end times, if there are no overlaps, then new room booking can be added to either eventInfo or schedule
    for event in result:
        existing_start_time, existing_end_time = event
        if (start_time_to_datetime < existing_end_time) and (end_time_to_datetime > existing_start_time):
            print("No no no can't book here")
            return True
    return False

# returns true if booking was successful
def roomBooking(connection, room_id, attendees, start_time, end_time):
    cursor = connection.cursor()
    try:
        if findOverlaps(cursor, room_id, start_time, end_time) == False:
            # if no overlaps, we can add the booking
            query = "INSERT INTO eventInfo(room_used, attendees, start_time, end_time) VALUES ( %s, %s, %s,%s);"
            cursor.execute(query, (room_id, attendees, start_time, end_time))
            connection.commit()
            return True
        
        else:
            return False

    except psycopg2.DatabaseError as e:
        print("Error booking room!", e)

# Returns true if booking was successful 
def classScheduling(connection, room_used, trainer_email, start_time, end_time, type_session, class_type):
    cursor = connection.cursor()
    try:
        # check to see trainer is available
        start_time_to_datetime = datetime.strptime(start_time, '%H:%M:%S').time()
        end_time_to_datetime = datetime.strptime(end_time, '%H:%M:%S').time()

        query = "SELECT start_time, end_time FROM trainer WHERE email = %s"
        cursor.execute(query, (trainer_email, ))
        result = cursor.fetchall()

        trainer_start_time = result[0][0]
        trainer_end_time = result[0][1]

        if (start_time_to_datetime <= trainer_start_time) or (end_time_to_datetime >= trainer_end_time):
            print("No no no can't book a class here")
            return False

        if findOverlaps(cursor, room_used, start_time, end_time) == False:
            # if no overlaps, we can add the booking
            query = "INSERT INTO schedule (room_used, trainer_email, start_time, end_time, type_session, class_type) VALUES (%s, %s, %s, %s, %s, %s);"
            cursor.execute(query, (room_used, trainer_email, start_time, end_time, type_session, class_type))
            connection.commit()
            return True
        
        else:
            return False

    except psycopg2.DatabaseError as e:
        print("Error booking room!", e)
    return

def equipmentMaintenenceMonitoring(connection, equipment_name):
    cursor = connection.cursor()
    # Just update date in equipment
    try:
        query = "UPDATE equipment_maintenence SET last_checked = %s WHERE equipment_name = %s"
        cursor.execute(query, (date.today(), equipment_name))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error monitoring equipment!")
    return 

def addEquipment(connection, equipment_name, room_id):
    cursor = connection.cursor()
    try:
        query = "INSERT INTO equipment_maintenence (equipment_name, room_id) VALUES (%s, %s)"
        cursor.execute(query, (equipment_name, room_id))
        connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error adding equipment!") 
    return

def main():
    connection = connectToDatabase()
    #testingSelect(cursor)

    #validateUser(cursor,'Jim','Beam','students')
    #validateUser(cursor,'hey','Beam','students')
    
    #addMember(connection, 'test', 'test', 'test', 2, 'M', 5, 2, 5, 'round')
    #updateMemberInformation(connection, 'test', 'test', 'testING', 4, 'M', '5', '2', '5', 'rotund')
    #print(printDashboard(connection, 'spongebob@squarepants.com'))
    #getMember(connection, 'testING')
    #print(validateUser(connection,'lujain@gmail.com','lujain','members'))
    #print(selectMember(connection,'lujain@gmail.com'))
    #equipmentMaintenenceMonitoring(connection, 'Treadmill')
    #testingSelect(connection.cursor())
    #setAvailability(connection, 'SandyCheeks@gmail.com', '5:00:00', '17:00:00')
    #roomBooking(connection, 1, 15, '8:00:00', '9:00:00')
    #classScheduling(connection, 1, 'SandyCheeks@gmail.com', '9:00:00', '10:00:00', 'group', 'cardio')
    #joinClass(connection, 6, 'plankton@chumbucket.org')
    #print(printAvailableClasses(connection))
    print(printMembersClasses(connection, 'plankton@chumbucket.org'))
    #cancelClass(connection, 7, 'plankton@chumbucket.org')
    #addEquipment(connection, 'skipping rope', 4)
main()