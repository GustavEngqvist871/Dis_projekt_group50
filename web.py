from flask import Flask, render_template, request
import psycopg2
from datetime import date

app = Flask(__name__)
DATABASE = {
    'host': '::1',
    'database': 'Bade',
    'user': 'postgres',
    'password': 'ROOT'
}

# Function to connect to the PostgreSQL database
def connect_to_database():
    try:
        connection = psycopg2.connect(
            host=DATABASE['host'],
            database=DATABASE['database'],
            user=DATABASE['user'],
            password=DATABASE['password']
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")

# Function to check the current date against the data in the database
def check_date():
    try:
        connection = connect_to_database()
        if connection is None:
            return None

        today = date.today()
        current_date = (today - date(today.year, 1, 1)).days

        cursor = connection.cursor()
        cursor.execute(f"SELECT temperature FROM dag WHERE dag = {current_date}")
        result = cursor.fetchone()

        if result is not None:
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Error checking date: {str(e)}")
def checkwindtemp():
    try:
        connection = connect_to_database()
        if connection is None:
            return None
        today = date.today()
        current_date = (today - date(today.year, 1, 1)).days
        cursor = connection.cursor()
        cursor.execute(f"SELECT temperature, vind FROM dag WHERE dag = {current_date}")
        result1 = cursor.fetchone()
        if result1 is not None:
            temperature, wind = result1
            return temperature, wind
        else:
            return None
    except Exception as e:
        print(f"Error checking date: {str(e)}")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Check the date when the button is clicked
            result = check_date()
            if result is not None and result > 15:
                return render_template('index.html', result='Yes, it is beach weather!')
            else:
                return render_template('index.html', result='No, it is not beach weather.')
        except Exception as e:
            return render_template('error.html', error_message=str(e))
    else:
        return render_template('index.html')
@app.route('/windtemp', methods=['GET', 'POST'])
def windtemp():
    if request.method == 'POST':
        try:
            # Get the wind and temperature for the current date
            temperature, wind = checkwindtemp()
            if temperature is not None and wind is not None:
                return render_template('windtemp.html', temperature=temperature, wind=wind)
            else:
                return render_template('windtemp.html', temperature='N/A', wind='N/A')
        except Exception as e:
            return render_template('error.html', error_message=str(e))
    else:
        return render_template('windtemp.html')

@app.route('/error')
def error():
    return render_template('error.html', error_message='An error occurred.')

if __name__ == '__main__':
    app.run()
