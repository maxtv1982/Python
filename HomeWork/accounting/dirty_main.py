from accounting.application.db.people import *
from accounting.application.salary import *
from datetime import *

if __name__ == '__main__':
    today = datetime.today()
    calculate_salary(1000, today)
    get_employees(23, today)