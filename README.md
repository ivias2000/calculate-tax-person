This code defines a function calc_tax that calculates the tax amount for a person based on their income and provides information about the person with the highest income in a predefined list of names, families, and incomes.
![Income-Tax-Rules-for-Fixed-Deposit](https://github.com/ivias2000/calculate-tax-person/assets/125237611/019db67e-76fd-4f48-a8d9-229db087675c)

Here's how the code works:

The function calc_tax takes two parameters: name and income. The name parameter represents the full name of the person (e.g., "Javad Ezzati"), and the income parameter represents the person's income (default value is 0).

The function initializes three lists:

names: A list of first names.
families: A list of last names (family names).
incomes: A list of corresponding incomes.
The name parameter is split into first and last names (assuming the input format is "First Last"), and the first name is added to the names list, and the last name is added to the families list.

If the income parameter is not provided or is set to 0, the function prompts the user to input the income value. The provided income is then converted to an integer and added to the incomes list.

The function calculates the tax amount based on the provided income:

If the income is greater than or equal to 35,000,000 Toman, the tax rate is 12% of the income.
Otherwise, if the income is less than 35,000,000 Toman, the tax rate is 9% of the income.
The function finds the person with the highest income (max_income) from the incomes list and retrieves their index (max_income_index) in the incomes list.

The function then prints:

The lists of names, families, and incomes (including the new data).
The calculated tax amount for the provided person's income.
The name and family of the person with the highest income and their income.
Note: The function modifies the predefined lists (names, families, and incomes) by adding new elements for the provided person's name and income.# calculate-tax-person
