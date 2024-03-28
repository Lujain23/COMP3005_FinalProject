import psycopg2


#returns the cursor to execute
def connectToDatabase():
    try:
        #would change depending on the user
        password = "comp3005"
        #database = "GymManagementSystem"
        database = "COMP3005_A3_database"

        connection = psycopg2.connect( database = database,
                                    host = "localhost",
                                    password = password,
                                    user = "postgres",
                                    port = "5432")
        
        print("Connected to Database!")

        connection.cursor()

        #make it return the connection? still thinking of how it would be used.
        return  connection.cursor()
   
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
    query = "SELECT * FROM %s WHERE email = %s AND passwd = %s"
    #query = "SELECT * FROM students where first_name = %s AND last_name = %s" #testing
    cursor.execute(query,(memberType,username,password))
    #cursor.execute(query,(username,password)) #testing
    ans = cursor.fetchall()

    if(len(ans) == 1):
        print("exists")
    else:
        print("no no no")
    



def main():
    cursor = connectToDatabase()
    #testingSelect(cursor)


    validateUser(cursor,'Jim','Beam','students')
    validateUser(cursor,'hey','Beam','students')
    



main()