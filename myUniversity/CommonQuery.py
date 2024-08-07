from msilib.schema import Class
from cv2 import HOUGH_STANDARD
import psycopg2

class CommonQuery:
    def __init__(self,user,password,database,host,port):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port
    
    def getDictFromQuery(self,query:str):
        try:
            connection = psycopg2.connect(user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port,
                                        database=self.database)
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as ex:
            print(str(ex))
        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def executeQuery(self,query:str):
        try:
            connection = psycopg2.connect(user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port,
                                        database=self.database)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            
            count = cursor.rowcount
            print(count, "Record inserted successfully into Alumno table")

        except Exception as ex:
            print(str(ex))
        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        
        