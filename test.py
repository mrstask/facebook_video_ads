import csv
audiences_name = ['katya', 'eva']
audience = list()


with open('samples/audience.csv', newline='') as f:
    file_reader = csv.reader(f, delimiter=',', quotechar='|')
    next(file_reader, None)
    for line in file_reader:
        audience_name, email, phone = line
        audience.append([audience_name, email])

for name in audiences_name:
    users = list()
    for user in audience:
        if user[0].strip() == name.strip():
            users.append(user[1])
    print(users)