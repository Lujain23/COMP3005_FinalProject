import psycopg2


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

        #make it return the connection? still thinking of how it would be used.
        return connection
   
    except psycopg2.Error as e:
        print(e)


def disconnectDatabase(connection):
    if connection is not None:
        connection.close()
        print("Connection Closed.")


def testingSelect(connection):
    cur = connection.cursor()
    cur.execute("SELECT * from students")
    ans = cur.fetchall()
    
    for row in ans:
        print("name is: " + row[1] + " " + row[2])


def main():
    connection = connectToDatabase()
    testingSelect(connection)

main()

#would have to create function handlers
