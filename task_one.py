import csv
with open("employees.csv") as foo:
    file = csv.DictReader(foo)

    a = dict()
    for line in file:
        a.update(line)
        bar = a.get("SALARY")
        bar = int(bar)
        email = a.get('EMAIL')
        foo = a.get('PHONE_NUMBER')
        res = foo.replace(".", "")
        if bar >= 9000:
            print("{\n"f"name:{a['FIRST_NAME']} {a['LAST_NAME']}\nemail:{email}\nphone number:{res}\n""}\n")
            print(bar)





