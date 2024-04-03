import psycopg2
from datetime import date, datetime
import math

#returns the cursor to execute
def connectToDatabase():
    try:
        #would change depending on the user
        #password = "admin" #trista
        password = "comp3005" #lujain
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

def checkTrainerAvailability(cursor, start_time, end_time, trainer_email):
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
    else:
        return True

# returns true if the rescheduling was successful
def rescheduleClass(connection, schedule_id, start_time, end_time):
    cursor = connection.cursor()
    try:
        # find trainer for class
        query = "SELECT trainer_email FROM schedule WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id, ))
        result = cursor.fetchall()
        trainer_email = result[0][0]

        # check that it falls under trainer availability
        if (checkTrainerAvailability(cursor, start_time, end_time, trainer_email) == True):
            # Convert to date time object
            start_time_to_datetime = datetime.strptime(start_time, '%H:%M:%S').time()
            end_time_to_datetime = datetime.strptime(end_time, '%H:%M:%S').time()

            # get start and end times of trainer's other classes besides the one that wants to be changed
            query = "SELECT start_time, end_time FROM schedule WHERE trainer_email = %s AND schedule_id != %s"
            cursor.execute(query, (trainer_email, schedule_id))
            result = cursor.fetchall()

            # Check all start and end times of all trainer's classes to make sure there are no overlaps
            for event in result:
                existing_start_time, existing_end_time = event
                if (start_time_to_datetime < existing_end_time) and (end_time_to_datetime > existing_start_time):
                    print("No no no can't reschedule here")
                    return False

            # if all checking was good, change the start and end time of the class
            query = "UPDATE schedule SET start_time = %s, end_time = %s WHERE schedule_id = %s"
            cursor.execute(query, (start_time, end_time, schedule_id))
            connection.commit()

            # Send notification to trainer that class has been rescheduled
            notificationMessage = "Class with schedule_id " + str(schedule_id) + " has beeen rescheduled to " + str(start_time) + " to " + str(end_time)
            query = "UPDATE trainer SET notification = %s WHERE email = %s"
            cursor.execute(query, (notificationMessage, trainer_email))
            connection.commit()
            return True
        else:
            return False

    except psycopg2.DatabaseError as e:
        print("Error rescheduling class!", e)  
    return

def cancelClass(connection, schedule_id, member_email):
    cursor = connection.cursor()
    try:
        query = "DELETE FROM scheduleStudents WHERE schedule_id = %s AND member_email = %s"
        cursor.execute(query, (schedule_id, member_email))
        connection.commit()

        # find trainer for class
        query = "SELECT trainer_email FROM schedule WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id, ))
        result = cursor.fetchall()
        trainer_email = result[0][0]

        # find member name
        query = "SELECT first_name FROM members WHERE email = %s"
        cursor.execute(query, (member_email, ))
        result = cursor.fetchall()
        first_name = result[0][0]
        
        # Send notification to trainer that class has been rescheduled
        notificationMessage = "Member " + first_name + " dropped class with schedule_id " + str(schedule_id)
        query = "UPDATE trainer SET notification = %s WHERE email = %s"
        cursor.execute(query, (notificationMessage, trainer_email))
        connection.commit()
        return True

    except psycopg2.DatabaseError as e:
        print("Error cancelling class!")
    return

def printAvailableClasses(connection):
    cursor = connection.cursor()
    try:
        query = "SELECT s.schedule_id, room_used, trainer_email, start_time, end_time, type_session, class_type FROM schedule s LEFT JOIN scheduleStudents stu ON s.schedule_id = stu.schedule_id WHERE stu.schedule_id IS NULL OR type_session = 'group'"
        cursor.execute(query)
        return(cursor.fetchall())

    except psycopg2.DatabaseError as e:
        return("Error printing available classes!", False)

def printSoloMemberClasses(connection, member_email):
    cursor = connection.cursor()
    try:
        query = "SELECT s.schedule_id, room_used, trainer_email, start_time, end_time, type_session, class_type FROM schedule s LEFT JOIN scheduleStudents stu ON s.schedule_id = stu.schedule_id WHERE stu.schedule_id IS NOT NULL AND member_email = %s AND type_session = 'solo'"
        cursor.execute(query, (member_email, ))
        return(cursor.fetchall())
    except psycopg2.DatabaseError as e:
        print("Error printing member's solo classes!")   
    return

def printMembersClasses(connection, member_email):
    cursor = connection.cursor()
    try:
        query = "SELECT stu.schedule_id, room_used, trainer_email, start_time, end_time, type_session, class_type FROM schedule s LEFT JOIN scheduleStudents stu ON s.schedule_id = stu.schedule_id WHERE stu.schedule_id IS NOT NULL AND member_email = %s"
        cursor.execute(query, (member_email, ))
        return(cursor.fetchall())
    except psycopg2.DatabaseError as e:
        return("Error printing classes member joins!", False)   

#Trainer Functions
def setAvailability(connection, email, start_time, end_time):
    cursor = connection.cursor()
    try:
        # get trainer's current class list
        query = "SELECT start_time, end_time FROM schedule WHERE trainer_email = %s"
        cursor.execute(query, (email, ))
        result = cursor.fetchall()

        # Convert to date time object
        start_time_to_datetime = datetime.strptime(start_time, '%H:%M:%S').time()
        end_time_to_datetime = datetime.strptime(end_time, '%H:%M:%S').time()

        # Check all start and end times of all trainer's classes to make sure they can change their schedule
        for event in result:
            existing_start_time, existing_end_time = event
            if (start_time_to_datetime > existing_start_time) or (end_time_to_datetime < existing_end_time):
                print("Error: new availability conflicts with current classes")
                return False

        # No conflicts -> update normally
        query = "UPDATE trainer SET start_time = %s, end_time = %s WHERE email = %s"
        cursor.execute(query, (start_time, end_time, email))
        connection.commit()
        return True

    except psycopg2.DatabaseError as e:
        print("Error setting availability!")
    return False

def getMember(connection, first_name):
    cursor = connection.cursor()
    try:
        query = "SELECT first_name, age, gender, height, weight, target_weight, exercise_routine FROM members WHERE first_name = %s"
        cursor.execute(query, (first_name,))
        result = cursor.fetchall()
        return result
    except psycopg2.DatabaseError as e:
        return("Error getting member!", False)

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

def staffCancelClass(connection, schedule_id):
    cursor = connection.cursor()
    try:
        # delete in scheduleStudents
        query = "DELETE FROM scheduleStudents WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id, ))
        connection.commit()

        # find trainer for class
        query = "SELECT trainer_email FROM schedule WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id, ))
        result = cursor.fetchall()
        trainer_email = result[0][0]

        # delete in schedule
        query = "DELETE FROM schedule WHERE schedule_id = %s"
        cursor.execute(query, (schedule_id, ))
        connection.commit()
        
        # Send notification to trainer that class has been rescheduled
        notificationMessage = "Class with schedule_id " + str(schedule_id) + " has beeen cancelled"
        query = "UPDATE trainer SET notification = %s WHERE email = %s"
        cursor.execute(query, (notificationMessage, trainer_email))
        connection.commit()

    except psycopg2.DatabaseError as e:
        print("Error cancelling class!")
    return

def staffCancelRoomBooking(connection, event_id):
    cursor = connection.cursor()
    try:
        # delete in scheduleStudents
        query = "DELETE FROM eventInfo WHERE event_id = %s"
        cursor.execute(query, (event_id, ))
        connection.commit()
        return True
    
    except psycopg2.DatabaseError as e:
        print("Error cancelling room booking!")
    return False

def modifyRoomBooking(connection, event_id, start_time, end_time):
    cursor = connection.cursor()
    try:
        # find room_id of event_id
        query = "SELECT room_used FROM eventInfo WHERE event_id = %s"
        cursor.execute(query, (event_id, ))
        result = cursor.fetchall()
        room_used = result[0][0]

        # if there's no overlaps with the new time, we can reschedule
        # Convert to date time object
        start_time_to_datetime = datetime.strptime(start_time, '%H:%M:%S').time()
        end_time_to_datetime = datetime.strptime(end_time, '%H:%M:%S').time()

        # get all schedules for current room minus the schedule we want to change
        query = "SELECT start_time, end_time FROM eventInfo WHERE room_used = %s AND event_id != %s UNION SELECT start_time, end_time FROM schedule WHERE room_used = %s"
        cursor.execute(query, (room_used, event_id, room_used))
        result = cursor.fetchall()

        # Check start and end times, if there are no overlaps, then room booking can be modified
        for event in result:
            existing_start_time, existing_end_time = event
            if (start_time_to_datetime < existing_end_time) and (end_time_to_datetime > existing_start_time):
                print("Error: cannot modify room booking")
                return False
        
        query = "UPDATE eventInfo SET start_time = %s, end_time = %s WHERE event_id = %s"
        cursor.execute(query, (start_time, end_time, event_id))
        connection.commit()
        return True
    except psycopg2.DatabaseError as e:
        print("Error modifying room booking!")
    return False

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
    #setAvailability(connection, 'LarryLobster@gmail.com', '6:00:00', '17:00:00')
    #roomBooking(connection, 1, 15, '8:00:00', '9:00:00')
    #classScheduling(connection, 1, 'SandyCheeks@gmail.com', '9:00:00', '10:00:00', 'group', 'cardio')
    #joinClass(connection, 6, 'plankton@chumbucket.org')
    #print(printAvailableClasses(connection))
    #print(printMembersClasses(connection, 'plankton@chumbucket.org'))
    #cancelClass(connection, 1, 'spongebob@squarepants.com')
    #addEquipment(connection, 'skipping rope', 4)
    #rescheduleClass(connection, 1, "7:30:00", "8:30:00")
    #printSoloMemberClasses(connection, 'spongebob@squarepants.com')
    #staffCancelClass(connection, 1)
    #staffCancelRoomBooking(connection, 3)
    #modifyRoomBooking(connection, 4, "8:00:00", "9:00:00")
main()