import glob
import pandas as pd

from elsapy.elsclient import ElsClient
from elsapy.elsdoc import AbsDoc

file_list = []
for file_name in glob.glob('ds/dois.csv'):
    file_list.append(pd.read_csv(file_name, sep='|', dtype={'doi': str}))
prod = pd.concat(file_list)

myCl = ElsClient('b882c86b0a0f392f7290da07177add70')
for idx, row in prod.iterrows():
    doi_doc = AbsDoc(scp_id=row['doi'])
    f = open('output/found.csv', 'a', encoding='utf8')
    g = open('output/error.csv', 'a', encoding='utf8')

    if doi_doc.read(myCl):
        print(idx, row['doi'], doi_doc.data['coredata']['subtypeDescription'])
        f.write(str.format('{}|{}\n',
                           row['doi'],
                           str(doi_doc.data['coredata']['subtypeDescription'])))
    else:
        print(idx, row['doi'], 'No data about document type.')
        g.write(str.format('{}\n',
                           row['doi']))
f.close()
