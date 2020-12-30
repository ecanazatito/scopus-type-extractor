# scopus-type-extractor
Extracts the document type from scopus dois. The source code can change for extract each value you want but in this moments only extracts the document type.

# Requeriments
1. Add the environment to anaconda using the YML file.

# Operation
1. Add the list of dois inside ``dois.csv`` file with a header called **doi** inside ``/ds`` 
2. Run the ``main.py`` file
3. Watch the results in ``/output``. In ``found.csv`` the accesible dois and in ``error.csv`` the inaccesibles dois. 

# Libs used in the project
1. pandas
2. elsapy (https://pypi.org/project/elsapy/)
