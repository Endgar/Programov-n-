with open('prijmeni.txt', 'r') as f:
    prijmeni = f.readlines()

with open('skript.sql', 'w') as f:
    for prijmeni in prijmeni:
        prijmeni = prijmeni.strip()
        f.write(f"CREATE DATABASE {prijmeni} CHARACTER SET utf8 COLLATE utf8_czech_ci;\n")
        f.write(f"CREATE USER '{prijmeni}'@'localhost' IDENTIFIED BY '{prijmeni}123.';\n")
        f.write(f"GRANT ALL PRIVILEGES ON {prijmeni}.* TO '{prijmeni}'@'localhost' WITH GRANT OPTION;\n")

#ahojky bleh
