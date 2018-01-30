import cx_Oracle

def selectUserDirectQuery(user):
    connection = cx_Oracle.connect("alatel01", "adm123", "oraclesrv.dcs.bbk.ac.uk/pdmain.dcs.bbk.ac.uk")

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
    connection = cx_Oracle.connect("alatel01", "adm123", "oraclesrv.dcs.bbk.ac.uk/pdmain.dcs.bbk.ac.uk")

    cursor = connection.cursor()
    query = "SELECT TITLE, SUPERVISOR FROM PROJ_DETAILS WHERE STUDENT = :usr"
    cursor.prepare(query)
    cursor.execute(None, usr=user)
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