import mysql.connector

def selectUserDirectQuery(user):
    connection = mysql.connector.connect(user='dkm_cw', password='dkm_cw',
                                  host='localhost',
                                  database='dkm_cw')
    cursor = connection.cursor()
    query = ("SELECT TITLE, SUPERVISOR FROM PROJ_DETAILS WHERE STUDENT = '" + user + "'")

    cursor.execute(query)
    print(query)
    try:
        print("Execute Direct Select:: Select correctly executed -> Input: " + user + " - Output: ")
        for row in cursor:
            print(row)
    except Exception as e:
        print("Error -> Input: " + user + " - Output: " + str(e))

    cursor.close()
    connection.close()


def selectUserPrepareStatement(user):
    connection = mysql.connector.connect(user='dkm_cw', password='dkm_cw',
                                  host='localhost',
                                  database='dkm_cw')
    cursor = connection.cursor()
    query = ("SELECT TITLE, SUPERVISOR FROM PROJ_DETAILS WHERE STUDENT = %s")
    cursor.execute(query, (user,))
    print(query)
    try:
        print("Execute Prepare Statement Select:: Select correctly executed -> Input: " + user + " - Output: ")
        for row in cursor:
            print(row)
    except Exception as e:
        print("Error -> Input: " + user + " - Output: " + str(e))

    cursor.close()
    connection.close()

selectUserDirectQuery("mary01")
print()
selectUserDirectQuery("mary01' or 'dummy'='dummy")
print()
selectUserPrepareStatement("mary01")
print()
selectUserPrepareStatement("mary01' or 'dummy'='dummy")
