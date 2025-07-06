# Шаг 1
import csv

source_file = open("202009-citibike-tripdata.csv", "r")
citibike_reader = csv.DictReader(source_file)

print(*citibike_reader.fieldnames, sep='\n')

# Шаг 2
subscriber_count = 0
customer_count = 0
other_user_count = 0

# Шаг 3
for row in citibike_reader:
    if row["usertype"] == "Subscriber":
        subscriber_count += 1
    elif row["usertype"] == "Customer":
        customer_count += 1
    else:
        other_user_count += 1

# Шаг 4
print(f"Number of subscribers: {subscriber_count}")
print(f"Number of customers: {customer_count}")
print(f"Number of 'other' users: {other_user_count}")