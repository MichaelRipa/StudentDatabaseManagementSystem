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
        # Create cursor for executing PostgreSQL commands in db session
        self.cursor = self.conn.cursor()
        self.args = args

    def getAllStudents(self):
        self.cursor.execute(f'SELECT * FROM {args.default_table}')
        return(self.cursor.fetchall())

    def addStudent(self, first_name : str, last_name : str, email : str, enrollment_date : date):
        insert_sql = f'INSERT INTO {self.args.default_table} (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)'
        values = (first_name, last_name, email, enrollment_date)
        self.cursor.execute(insert_sql, values)

    def updateStudentEmail(self, new_email : str, student_id : int):
        update_sql = f'UPDATE {self.args.default_table} SET email = %s WHERE student_id = %s'
        values = (new_email, student_id)
        self.cursor.execute(update_sql, values)

    def deleteStudent(self, student_id : int):
        delete_sql = f'DELETE FROM {self.args.default_table} WHERE student_id = %s'
        values = (student_id,)
        self.cursor.execute(delete_sql, values)

        

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
    parser.add_argument('--commit', type=bool, required=False, default=False)

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
    q3 = db.updateStudentEmail('newemail@email.com', 1)
    print('Result:')
    pretty_print(db.getAllStudents())

    print('Question 4:')
    q4 = db.deleteStudent(1)
    print('Result:')
    pretty_print(db.getAllStudents())

    if args.commit:
        print('Commiting changes!')
        db.conn.commit()

    db.conn.close()
