import csv
import matplotlib.pyplot as plt
# conda install matplotlib
import os

from python.student_exercises.implementations.basics.my_array.my_array import average, median

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def read_sales_data() -> list[dict]:
    """
    Reads the sales data from the "sales_data.csv" file.

    Arguments: None

    Returns:
    - sales_data (list): List of dictionaries representing sales data.
    """
    sales_data = []
    sales_path = CURRENT_DIR +"/sales_data.csv"
    with open(sales_path, 'r') as fp:
        sales_data = list(csv.DictReader(fp))
    return sales_data


def read_employee_data() -> list[dict]:
    """
    Reads the employee data from the "employee_data.csv" file.

    Arguments: None

    Returns:
    - employee_data (list): List of dictionaries representing employee data.
    """
    employee_data = []
    employee_path = CURRENT_DIR +"/employee_data.csv"
    with open(employee_path, 'r') as fp:
        employee_data = list(csv.DictReader(fp))
    return employee_data


def calculate_total_sales(sales_data: list[dict]) -> float | int:
    """
    Calculates the total sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - total_sales (float): Total sales amount.
    """
    return sum(float(item['Amount']) for item in sales_data)


def calculate_average_sales(sales_data: list[dict]) -> float | int:
    """
    Calculates the average sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - average_sales (float): Average sales amount.
    """
    return average(list(int(item['Amount']) for item in sales_data))

def calculate_median_sales(sales_data: list[dict]) -> float | int:
    """
    Calculates the median sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - median_sales (float): Median sales amount.
    """
    
    return median(list(int(item['Amount']) for item in sales_data))

def calculate_total_salary_expenses(employee_data: list[dict]) -> float | int:
    """
    Calculates the total salary expenses.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - total_salary_expenses (float): Total salary expenses.
    """
    return sum(float(item['Salary']) for item in employee_data)


def calculate_average_salary(employee_data: list[dict]) -> float | int:
    """
    Calculates the average salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - average_salary (float): Average salary.
    """
    return average(list(int(item['Salary']) for item in employee_data))

def calculate_median_salary(employee_data: list[dict]) -> float | int:
    """
    Calculates the median salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - median_salary (float): Median salary.
    """
    return median(list(int(item['Salary']) for item in employee_data))


def find_employee_with_highest_sales(sales_data: list[dict], employee_data: list[dict]) -> tuple[str, str]:
    """
    Finds the employee with the highest sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - employee_name (str): Name of the employee with the highest sales amount.
    - department_name (str): Name of the department of the employee with the highest sales amount.
    """

    grouped_sales = {
        emp['EmployeeID']: {
            'EmployeeID': emp['EmployeeID'],
            'Department': emp['Department'],
            'Name': emp['Name'],
            'Salary': float(emp['Salary']),
            'Sales': sum([float(sale['Amount']) for sale in sales_data if sale['EmployeeID'] == emp['EmployeeID']])
        }
        for emp in employee_data
    }

    max_sale = max(grouped_sales.values(), key=lambda x: x['Sales'])

    return max_sale['Name'], max_sale['Department']


def find_department_with_highest_sales(sales_data: list[dict], employee_data: list[dict]) -> str:
    """
    Finds the department with the highest sales.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - department_name (str): Name of the department with the highest sales.
    """

    max_sales_department = {}
    for employee in employee_data:
        for sale in sales_data:
            if employee['EmployeeID'] == sale['EmployeeID']:
                max_sales_department.update({employee['Department']: max_sales_department.get(employee['Department'], 0) + int(sale['Amount'])})

    return max(max_sales_department, key=max_sales_department.get)


def plot_sales_by_department(sales_data, employee_data):
    """
    Plots a bar chart showing the total sales by department.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns: None
    """


    sales_by_department = {}
    for employee in employee_data:
        for sale in sales_data:
            if employee['EmployeeID'] == sale['EmployeeID']:
                sales_by_department.update(
                    {employee['Department']: sales_by_department.get(employee['Department'], 0) + int(sale['Amount'])})


    plt.bar(
        list(sales_by_department.keys()),
        list(sales_by_department.values()),
    )
    plt.grid(True)
    plt.title("Total Sales by Department")
    plt.show()
    pass


def plot_sales_vs_salary(sales_data, employee_data):
    """
    Plots a scatter plot showing the relationship between sales and salary.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns: None
    """


    # a list containing the salary by employee
    grouped_sales = {
        emp['EmployeeID']: {
            'Department': emp['Department'],
            'Salary': float(emp['Salary']),
            'Sales': sum([float(sale['Amount']) for sale in sales_data if sale['EmployeeID'] == emp['EmployeeID']])
        }
        for emp in employee_data
    }

    sales_values_ = [item['Sales'] for item in grouped_sales.values()]
    salary_values_ = [item['Salary'] for item in grouped_sales.values()]
    plt.scatter(x = sales_values_, y = salary_values_)
    plt.title('Relation between Sale Amount and Salary')
    plt.xlabel('Sale Amount')
    plt.ylabel('Salary')
    plt.show()
    pass


def main():
    # Read sales data
    sales_data = read_sales_data()

    # Read employee data
    employee_data = read_employee_data()

    # Calculate total sales amount
    total_sales = calculate_total_sales(sales_data)
    print("Total Sales Amount:", total_sales)

    # Calculate average sales amount
    average_sales = calculate_average_sales(sales_data)
    print("Average Sales Amount:", average_sales)

    # Calculate median sales amount
    median_sales = calculate_median_sales(sales_data)
    print("Median Sales Amount:", median_sales)

    # Calculate total salary expenses
    total_salary_expenses = calculate_total_salary_expenses(employee_data)
    print("Total Salary Expenses:", total_salary_expenses)

    # Calculate average salary
    average_salary = calculate_average_salary(employee_data)
    print("Average Salary:", average_salary)

    # Calculate median salary
    median_salary = calculate_median_salary(employee_data)
    print("Median Salary:", median_salary)

    # Find the employee with the highest sales amount
    highest_sales_employee, highest_sales_employee_dep = find_employee_with_highest_sales(sales_data, employee_data)
    print("Employee with Highest Sales Amount:", highest_sales_employee, highest_sales_employee_dep)

    # Find the department with the highest sales
    highest_sales_department = find_department_with_highest_sales(sales_data, employee_data)
    print("Department with Highest Sales:", highest_sales_department)

    # Plot total sales by department
    # plot_sales_by_department(sales_data, employee_data)

    # Plot sales vs. salary
    plot_sales_vs_salary(sales_data, employee_data)


if __name__ == '__main__':
    main()
