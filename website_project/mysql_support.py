from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection Configuration
db_config = {
    'user': 'root',
    'password': '1111',
    'host': 'localhost',
    'database': 'mywork'
}

@app.route('/students', methods=['GET'])
def get_students():
    try:
        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(**db_config)

        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Retrieve data from the highschool_students table
        query = "SELECT * FROM highschool_students"
        cursor.execute(query)
        students = cursor.fetchall()

        # Format the data as desired
        student_data = []
        for student in students:
            student_data.append({
                'student_no': student[0],
                'student_name': student[1],
                'grade': student[2],
                'class': student[3],
                'gender': student[4],
                'age': student[5],
                'enter_date': student[6].strftime('%Y-%m-%d')
            })

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Return the data as a JSON response
        return {'students': student_data}

    except mysql.connector.Error as error:
        return {'error': str(error)}


@app.route('/students', methods=['POST'])
def add_student():
    try:
        # Get the student data from the request body
        student = request.json

        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(**db_config)

        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Insert the new student data into the highschool_students table
        query = "INSERT INTO highschool_students (student_no, student_name,\
            grade, class, gender, age, enter_date) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (
            student['student_no'],
            student['student_name'],
            student['grade'],
            student['class'],
            student['gender'],
            student['age'],
            student['enter_date']
        )
        cursor.execute(query, values)

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Return a success message
        return {'message': 'Student added successfully'}

    except mysql.connector.Error as error:
        return {'error': str(error)}


if __name__ == '__main__':
    app.run()
