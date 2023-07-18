def calc_tax(name, income=0):
        names = ["Javad", "Navid", "Tannaz", "Taraneh", "Parsa"]
        families = ["Ezzati", "Mohammadzadeh", "Tabatabaei", "Alidousti", "Pirouzfar"]
        incomes = [23_000_000, 45_000_000, 32_000_000, 37_000_000, 47_000_000]
	
        name_split = name.split()
        names.append(name_split[0])
        families.append(name_split[1])

        if income == 0:
        	income = input("Lotfan mizane daramad ra vared konid: ")
        	income = int(income)
        incomes.append(income)
        
        if income >= 35_000_000:
        	tax = income * 0.12
        else:
        	tax = income * 0.09

        max_income = max(incomes)
        max_income_index = incomes.index(max_income)

        print(names)
        print(families)
        print(incomes)
        print("Maliate " + name + " barabar ast ba " + str(int(tax)) + " Toman")
        print(names[max_income_index] + " " + families[max_income_index] + " bishtarin daramad ra darad.")
        




