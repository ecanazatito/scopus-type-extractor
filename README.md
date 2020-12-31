# scopus-type-extractor
Extracts the document type from scopus dois. The source code can change for extract each value you want but in this moments only extracts the document type.

# Instructions
1. Create a conda env using **env-scopus.yml** file
```
conda env create -f env-scopus.yml
conda activate env-scopus
```
2. Add the list of dois inside **dois.csv** file with a header called **doi** inside ``/ds`` 
3. Run the ``main.py`` file
```
python main.py
```
4. Watch the results in ``/output``. In **found.csv** the accesible dois and in **error.csv** the inaccesibles dois. 

# Notes
In line 12 on **main.py** file is the API token. You can create yours in https://dev.elsevier.com/

# Libs used in the project
1. pandas
2. elsapy (https://pypi.org/project/elsapy/)
