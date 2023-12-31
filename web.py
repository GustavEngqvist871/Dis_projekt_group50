from flask import Flask, render_template, request
import psycopg2
from datetime import date

app = Flask(__name__)
DATABASE = {
    'host': '::1',
    'database': 'Bade',
    'user': 'postgres',
    'password': 'root'
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

def retrieve_data_from_database(selected_date):
    try:
        connection = connect_to_database()
        if connection is None:
            return None


        cursor = connection.cursor()
        cursor.execute(f"SELECT temperature, vind FROM dag WHERE dag = {selected_date}")
        result2 = cursor.fetchone()

        if result2 is not None:
            temperature, wind = result2
            return temperature, wind
        else:
            return None
    except Exception as e:
        print(f"Error retrieving data from the database: {str(e)}")

def get_day_of_year(selected_date):
    try:
        selected_date_obj = date.fromisoformat(selected_date)
        start_of_year = date(selected_date_obj.year, 1, 1)
        day_of_year = (selected_date_obj - start_of_year).days + 1
        return day_of_year
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Check the date when the button is clicked
            result = check_date()
            if result is not None and result > 13:
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

@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        try:
            selected_date = request.form['date']
            day_of_year = get_day_of_year(selected_date)
            print(day_of_year)
            if day_of_year is None:
                return render_template('error.html', error_message='Invalid date format.')
            
            temperature, wind = retrieve_data_from_database(day_of_year)
            
            if temperature is not None and wind is not None:
                return render_template('data.html', temperature=temperature, wind=wind)
            else:
                return render_template('data.html', temperature='N/A', wind='N/A')
        except Exception as e:
            return render_template('error.html', error_message=str(e))
@app.route('/error')
def error():
    return render_template('error.html', error_message='An error occurred.')

if __name__ == '__main__':
    app.run()

