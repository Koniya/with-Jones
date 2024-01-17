"""
countries = ["Kenya", "Philippines", "Sweden"]
countries [2] = "Barbados"

print(countries)


countries = ["Kenya", "Philippines", ["Sweden", "Switzerland"]]
countries [2][1] = "USA"

print (countries)
"""
countries = ["Kenya", "Philippines", ["Sweden", "Switzerland",["Netherlands", "Africa"]], "Canada", "Qatar"]
Africa_index = countries[2][2][1].index("Africa")
countries[2][2][1].append(Africa_index + 1, "Japan")
#countries [2][2][1] = "Japan"
print (countries)
