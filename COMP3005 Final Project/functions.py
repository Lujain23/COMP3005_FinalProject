import psycopg2


#returns the cursor to execute
def connectToDatabase():
    try:
        #would change depending on the user
        password = "admin"
        database = "GymManagementSystem"
        #database = "COMP3005FinalProject"

        connection = psycopg2.connect( database = database,
                                    host = "localhost",
                                    password = password,
                                    user = "postgres",
                                    port = "5432")
        
        print("Connected to Database!")

        connection.cursor()

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

def validateUser(cursor,username,password,memberType):
    #query = "SELECT * FROM %s WHERE email = %s AND passwd = %s"
    query = "SELECT * FROM students where first_name = %s AND last_name = %s" #testing
    #cursor.execute(query,(memberType,username,password))
    cursor.execute(query,(username,password)) #testing
    ans = cursor.fetchall()

    if(len(ans) == 1):
        print("exists")
    else:
        print("no no no")

#Member Functions
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
def setAvailability():
    return

def getMember(connection, first_name):
    cursor = connection.cursor()
    try:
        query = "SELECT first_name, age, gender, height, weight, target_weight, exercise_routine FROM members WHERE first_name = %s"
        cursor.execute(query, (first_name,))
        result = cursor.fetchall()
        print(result)
    except psycopg2.DatabaseError as e:
        print("Error getting member!")
    return

#staff functions
    



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
main()