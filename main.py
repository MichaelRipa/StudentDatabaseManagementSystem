from argparse import ArgumentParser
from datetime import date
import psycopg2

class PostgreSQLDatabase:
    def __init__(self, args):
        # Initialize DB connection
        self.conn = psycopg2.connect(
            database=args.database,
            host=args.host,
            user=args.user,
            password=args.password,
            port=args.port
        )
        self.cursor = self.conn.cursor()

    def getAllStudents(self):
        self.cursor.execute(f'SELECT * FROM {args.default_table}')
        return(self.cursor.fetchall())

    def addStudent(self, first_name : str, last_name : str, email : str, enrollment_date : date):
        pass

    def updateStudentEmail(self, student_id : int, new_email : str):
            pass

    def deleteStudent(self, student_id : int):
        pass

def pretty_print(table):
    '''Helper function which prints query results in consistent format'''
    for record in table:
        line = ''
        for attr in record:
            line += ' ' + str(attr) + ' '
        print(line)

if __name__ == '__main__':
    parser = ArgumentParser()        
    parser.add_argument('--password', type=str)        
    parser.add_argument('--database', type=str, required=False, default='studentdb')        
    parser.add_argument('--host', type=str, required=False, default='localhost')        
    parser.add_argument('--user', type=str, required=False, default='postgres')        
    parser.add_argument('--port', type=int, required=False, default=5432)        
    parser.add_argument('--default_table', type=str, required=False, default='students')        

    args = parser.parse_args()

    db = PostgreSQLDatabase(args)

    print('Question 1:')
    q1 = db.getAllStudents()
    pretty_print(q1)

    print('Question 2:')
    q2 = db.addStudent('first','last','firstlast@email.com',date(1970,1,1))
    print('Result:')
    pretty_print(db.getAllStudents())

    print('Question 3:')
    q3 = db.updateStudentEmail(1,'newemail@email.com')
    print('Result:')
    pretty_print(db.getAllStudents())

    print('Question 4:')
    q4 = db.deleteStudent(1)
    print('Result:')
    pretty_print(db.getAllStudents())
