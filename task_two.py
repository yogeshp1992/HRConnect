import csv
import datetime

with open("employees.csv") as foo:
    file = csv.DictReader(foo)
    a = dict()
    for line in file:
        a.update(line)
        # first name,last name
        first_name = a.get('FIRST_NAME')
        last_name = a.get('LAST_NAME')

        # HIRE DATE
        hire_date = a.get('HIRE_DATE')
        res_date = datetime.datetime.strptime(hire_date, "%d-%b-%y")


        # get salary data
        salary = a.get("SALARY")
        salary = int(salary)

        # get department id
        D_id = a.get('DEPARTMENT_ID')
        D_id = int(D_id)

        if salary > 4200 and D_id >= 30 and D_id <= 110:
            print(f"{res_date}:\n{first_name} {last_name},\n")
