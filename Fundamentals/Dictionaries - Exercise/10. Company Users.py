company = {}

while True:
    command = input()
    if command == 'End':
        break
    company_name, employee_id = command.split(' -> ')
    if company_name not in company:
        company[company_name] = []
    if employee_id not in company[company_name]:
        company[company_name] += [employee_id]

for k in company.keys():
    print(f"{k}")
    for index in company[k]:
        print(f"-- {index}")
