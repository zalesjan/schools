from pandas import pandas as pd
from faker import Faker

# Generate fake data using Faker library
fake = Faker()

# Define the number of rows for the table
num_rows = 10

# Create an empty table
table = pd.DataFrame(columns=['Name', 'Age', 'Email'])

# Generate synthetic data and populate the table
for _ in range(num_rows):
    name = fake.name()
    age = fake.random_int(min=18, max=65)
    email = fake.email()
    table = table._append({'Name': name, 'Age': age, 'Email': email}, ignore_index=True)

# Display the table
print(table)