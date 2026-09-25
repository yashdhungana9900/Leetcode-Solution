class Solution(object):
    def getImportance(self, employees, id):
        employee_map = {}

        for employee in employees:
            employee_map[employee.id] = employee

        def dfs(emp_id):
            employee = employee_map[emp_id]

            total = employee.importance

            for sub_id in employee.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)