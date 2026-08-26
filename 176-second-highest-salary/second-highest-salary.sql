SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
where salary<(SELECT MAX(salary) AS SecondHighestSalary
FROM Employee);