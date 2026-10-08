record = "Lovelace;Ada;1815;mathematician;English"

parts = record.split(";")

surname = parts[0]
forename = parts[1]
born = parts[2]
role = parts[3]
ethnicity = parts[4]

print(f"{forename} {surname} was born in {born} and worked as a {role}.") # Ada Lovelace was born in 1815 and worked as a mathematician
print(f"Initials: {forename[0]}.{surname[0]}.") # Initials: A.L
print(f"{forename} {surname} was unfortunately {ethnicity}") # Ada lovelace was unfortunately Enligsh
