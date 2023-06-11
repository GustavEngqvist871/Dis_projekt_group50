## Initialization ✔

Clone / download repository files and run the following to install the required packages 
$pip install -U Flask
$pip install psycopg2

2. Run tabels.sql in pgadmin:
Create a new database in pgAdmin (preferably named Bade)
open query 
open tabels.sql in the query
execute the query

3. web.py file:
open the file
make sure the database information is correct:
    DATABASE = {
    'host': '::1',
    'database': 'Bade',
    'user': 'postgres',
    'password': 'root'
}
run the file
ctr+leftmouse click on the link 

