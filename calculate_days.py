# Create a program using maths and f-Strings that tells
# us how many days, weeks, months we have left
# if we live until 90 years old.

age = input("enter current age: ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
month_remaining = years_remaining * 12

print(f"you have {days_remaining} days,{weeks_remaining} "
      f"weeks and {month_remaining} months are left")

"""o/p=>
enter current age: 30
you have 21900 days,3120 weeks and 720 months are left
"""