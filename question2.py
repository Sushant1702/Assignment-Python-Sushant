standard_deduction = 10000
gross_income = input("Gross income is :")
count_of_dependent = input("Number of dependents are :")
dependent_deduction = 3000*int(count_of_dependent)
taxable_income = float(gross_income) - int(standard_deduction) - int(dependent_deduction)
print("taxable income :",taxable_income)
tax = int(taxable_income)*0.2
print("Total tax is :",tax)