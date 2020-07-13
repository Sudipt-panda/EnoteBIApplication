# EnoteBIApplication
Solution for ETL framework problem required for Enote BI Application

# How to guide:
## Database Creation
Please run the sql script *** EnoteBIAssignment.sql *** to create db or please create manually database with name :EnoteCode.
I had security inplace with user:root and password Pass@1234. Please update the code accordingly.

## Database Population
All the tables will be created from the input CSV file as recieved from the recruiting team.
Please install the requirements from requirements.txt file using the command *pip install -r requirements.txt*
Please run the python file *** db_populate.py *** to populate the db (the data preparation steps such as date formating, removing null rows etc. are included in this file)

## Report 
Please run the *** report.py *** file to see the desired query result.

