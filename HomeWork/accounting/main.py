from accounting.application.db.people import get_employees
from accounting.application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    today = datetime.today()
    calculate_salary(1000, today)
    get_employees(23, today)