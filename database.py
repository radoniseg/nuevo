import mysql.connector

class DataBase:
    def __init__(self):
        self.conn=mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='Machado199222',
		database='evaluacion'
		)

        self.mycursor=self.conn.cursor()
    
    def vistadb(self):
        myselect="SELECT * FROM paciente"
        self.mycursor.execute(myselect)
        return self.mycursor.fetchall()
    

