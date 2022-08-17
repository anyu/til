# Python Inheritance

Syntax:
```python
class BaseClass:
    {Body}
class DerivedClass(BaseClass):
    {Body}
```

Example:
```python
# modules.py

# base class (aka. superclass)
class Employee:
	# __init__ func is called every time an object is created from the class
	# the constructor for all intents & purposes (though some argue __new__
	# plays part of that role)
	# `self` = reference to the current instance of the class
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def get_report(self):
		return f"{self.name} ${self.salary}"

# derived class (aka. subclass), inherits from Employee
class Manager(Employee):
	def __init__(self, name, salary, leads_department):
		# calls superclass' init func
		super().__init__(name, salary)
		self.leads_department = leads_department

	def get_report(self):
		return f"{self.name} ${self.salary}, leads {self.leads_department} dep."

# main.py

employees = [
	Employee("Vera", 2000),
	Employee("Chuck", 2000),
	Manager("Dave", 2300, "IT"),
]

# reports.py

for e in employees:
	print(e.get_report())
```

outputs
```sh
Vera $2000
Chuck $2000
Dave $2300, leads IT dep.
```

## Method Resolution Order (MRO)

- MRO tells Python how to look for inherited methods
- check a class's MRO: `<class>.__mro__`
- All methods that are called with super() need to have a call to their superclass’s version of that method.
