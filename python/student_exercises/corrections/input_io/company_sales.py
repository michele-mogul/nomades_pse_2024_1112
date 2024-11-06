import csv
# import matplotlib.pyplot as plt
# conda install matplotlib
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def read_sales_data() -> list[dict]:
    """
    Reads the sales data from the "sales_data.csv" file.

    Arguments: None

    Returns:
    - sales_data (list): List of dictionaries representing sales data.
    """
    sales_path = os.path.join(CURRENT_DIR, "sales_data.csv")
    sales_data = []
    with open(sales_path) as file:  
      reader = csv.DictReader(file)
      for d in reader:
          d.update({'Amount': int(d['Amount'])})
          sales_data.append(d)
    return sales_data


def read_employee_data() -> list[dict]:
    """
    Reads the employee data from the "employee_data.csv" file.

    Arguments: None

    Returns:
    - employee_data (list): List of dictionaries representing employee data.
    """
    employee_path = os.path.join(CURRENT_DIR, "employee_data.csv")
    employee_data = []
    with open(employee_path) as file:  
      reader = csv.DictReader(file)
      for d in reader:
        d.update({'Salary': int(d['Salary'])})
        employee_data.append(d)
    return employee_data


def calculate_total_sales(sales_data: list[dict]) -> float | int:
    """
    Calculates the total sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - total_sales (float): Total sales amount.
    """
    # total_sales_amount = 0
    # for sale_data in sales_data:
    #   total_sales_amount += sale_data["Amount"]
    # return total_sales_amount
    return sum(sale_data["Amount"] for sale_data in sales_data)


def calculate_average_sales(sales_data: list[dict]) -> float | int:
    """
    Calculates the average sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - average_sales (float): Average sales amount.
    """
    return calculate_total_sales(sales_data) / len(sales_data)

def calculate_median_sales(sales_data: list[dict]) -> float | int:
    """
    Calculates the median sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - median_sales (float): Median sales amount.
    """
    list_amounts: list[int] = sorted([d['Amount'] for d in sales_data])
    mid: int = len(list_amounts) // 2
    return list_amounts[mid] if len(list_amounts) % 2 == 1 else (list_amounts[mid-1] + list_amounts[mid])/2


def calculate_total_salary_expenses(employee_data: list[dict]) -> float | int:
    """
    Calculates the total salary expenses.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - total_salary_expenses (float): Total salary expenses.
    """
    return sum([d["Salary"] for d in employee_data])


def calculate_average_salary(employee_data: list[dict]) -> float | int:
    """
    Calculates the average salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - average_salary (float): Average salary.
    """
    return calculate_total_salary_expenses(employee_data) / len(employee_data)

def calculate_median_salary(employee_data: list[dict]) -> float | int:
    """
    Calculates the median salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - median_salary (float): Median salary.
    """
    list_amounts: list[int] = sorted([d['Salary'] for d in employee_data])
    mid: int = len(list_amounts) // 2
    return list_amounts[mid] if len(list_amounts) % 2 == 1 else (list_amounts[mid-1] + list_amounts[mid])/2


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
    emp_d: dict[str, int] = {}
    for sale in sales_data:
      emp_d[sale['EmployeeID']] = emp_d.get(sale['EmployeeID'], 0) + sale['Amount']

    # max_amount = 0
    # max_id = ""
    key = lambda dict_key: emp_d.get(dict_key)
    # for emp_id in emp_d:
    #    if key(emp_id) > max_amount:
    #       max_id = emp_id
    #       max_amount = key(emp_id) 
    # print(max_amount, max_id)
    
    # max_id: str = max(emp_d, key=lambda dict_key: len(dict_key))
    max_id: str = max(emp_d, key=emp_d.get)
    print(max_id)
    for e in employee_data:
        if e["EmployeeID"] == max_id: 
          best_employee = e
          break
    
    return best_employee["Name"], best_employee["Department"]


def find_department_with_highest_sales(sales_data: list[dict], employee_data: list[dict]) -> str:
    """
    Finds the department with the highest sales.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - department_name (str): Name of the department with the highest sales.
    """
    return None


# def plot_sales_by_department(sales_data, employee_data):
#     """
#     Plots a bar chart showing the total sales by department.

#     Arguments:
#     - sales_data (list): List of dictionaries representing sales data.
#     - employee_data (list): List of dictionaries representing employee data.

#     Returns: None
#     """
#     pass


# def plot_sales_vs_salary(sales_data, employee_data):
#     """
#     Plots a scatter plot showing the relationship between sales and salary.

#     Arguments:
#     - sales_data (list): List of dictionaries representing sales data.
#     - employee_data (list): List of dictionaries representing employee data.

#     Returns: None
#     """
#     pass


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
    # plot_sales_vs_salary(sales_data, employee_data)


if __name__ == '__main__':
    main()
