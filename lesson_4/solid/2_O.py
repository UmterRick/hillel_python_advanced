"""
O - open/closed
"""

class SalaryCalc:
    base_salary = 1000

    def calculate(self, employee_level):
        if employee_level == "trainee":
            return self.base_salary * 0.5

        elif employee_level == "junior":
            return self.base_salary

        elif employee_level == "middle":
            return self.base_salary * 1.5


class BaseSalaryCalculator:
    base_salary = 1000

    def calculate(self):
        return self.base_salary



class TraineeSalaryCalc(BaseSalaryCalculator):

    def calculate(self):
        return self.base_salary * 0.5







