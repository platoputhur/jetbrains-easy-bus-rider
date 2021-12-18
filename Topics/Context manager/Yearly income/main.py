# write your code here
with open('salary.txt') as salary_file, open('salary_year.txt', 'w') as salary_year_file:
    for line in salary_file:
        annual_salary = int(line) * 12
        salary_year_file.write(f"{annual_salary}\n")