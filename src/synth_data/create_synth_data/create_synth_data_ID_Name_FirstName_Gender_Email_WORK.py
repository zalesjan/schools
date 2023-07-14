from pandas import pandas as pd
from faker import Faker

# Generate fake data using Faker library
fake = Faker()

# Define the number of rows for the table
num_rows = 10

# Create an empty table
table = pd.DataFrame(columns=['ID', 'Name', 'FirstName', 'Gender', 'Email', 'job/position', 'direct hours',	'hours', 'department', 'start_date', 'end_date', 'platovy stupen',	'platova trida'])

# Generate synthetic data and populate the table
for _ in range(num_rows):
    id = fake.random_int(min = 1, max = 200)
    name = fake.name()
    firstname = fake.first_name()
    gender = fake.random_elements(['male', 'female'])[0]
    email = fake.email()
    job_position = fake.random_elements(['teacher', 'care-taker'])[0]
    direct_hours= fake.random_int(min = 10, max = 40)
    hours= fake.random_int(min = 15, max = 22)
    department = fake.random_elements(['school', 'operation', 'kitchen'])[0]
    start_date = fake.random_elements(['open', 'yearly'])[0]
    end_date = fake.random_elements(['open', 'yearly'])[0]
    platovy_stupen = fake.random_int(min = 1, max = 14)
    platova_trida = fake.random_int(min = 1, max = 14)
    table = table._append({'ID': id,'Name': name, 'FirstName': firstname, 'Gender': gender, 'Email': email, 'job/position': job_position, 'direct hours': direct_hours, 'hours': hours, 'department': department, 'start_date': start_date, 'end_date': end_date, 'platovy stupen': platovy_stupen,	'platova trida': platova_trida}, ignore_index=True)

# Display the table
print(table)