from base.models import Assessment
import pdftables_api
import pandas as pd
c = pdftables_api.Client('fd12p22l1tli')
c.csv('/content/Year 3 CS Assessment Map (1).pdf', 'output.csv')

df = pd.read_csv('output.csv')

for i, row in df.iterrows():
    a = Assessment()
    a.module = row['Module']
    a.contribution = row['Contribution']
    a.Title = row['Title']
    a.type = row['Type']
    a.Hand_out_date = row['Hand out date']
    a.hand_in_date = row['Hand in date']
    a.save()
