import pandas as pd
import string
import bokeh

data = pd.read_csv('private_data/stakeholder_data.csv')

len(data) #277

data.columns = list(string.ascii_uppercase)[:len(data.columns)]+['unnamed']


def agg_column(column, cat):
    rows = []
    for i in set(column):
        row = []
        row.append(i)
        row.append(column.tolist().count(i))
        row.append(cat)
        rows.append(row)
    return pd.DataFrame(rows, columns = ['label', 'value','cat'])


# aggregate gender column M
age_df = agg_column(data['M'],'age')
age_df.to_csv('private_data/stakeholder_demographics/age_agg.csv')

highest_degree = agg_column(data['L'], 'degree')
highest_degree.to_csv('private_data/stakeholder_demographics/degree_agg.csv')

method_technical = agg_column(data['J'], 'method_obtain_tech_skill')
method_technical.to_csv('private_data/stakeholder_demographics/method_technical_agg.csv')

organization = agg_column(data['F'], 'organization')
organization.to_csv('private_data/stakeholder_demographics/organization_agg.csv')

position = agg_column(data['C'], 'position')
position.to_csv('private_data/stakeholder_demographics/position_agg.csv')

role = agg_column(data['D'], 'role')
role.to_csv('private_data/stakeholder_demographics/role_agg.csv')


####################################################################

import pandas as pd
import string
import bokeh

data = pd.read_csv('private_data/intech_data.csv')

len(data) #638

data.columns = list(string.ascii_uppercase)[:len(data.columns)]+['unnamed']


def agg_column(column, cat):
    rows = []
    for i in set(column):
        row = []
        row.append(i)
        row.append(column.tolist().count(i))
        row.append(cat)
        rows.append(row)
    return pd.DataFrame(rows, columns = ['label', 'value','cat'])


# aggregate gender column M
age_df = agg_column(data['M'],'age')
age_df.to_csv('private_data/intech_demographics/age_agg.csv')

highest_degree = agg_column(data['L'], 'degree')
highest_degree.to_csv('private_data/intech_demographics/degree_agg.csv')

method_technical = agg_column(data['J'], 'method_obtain_tech_skill')
method_technical.to_csv('private_data/intech_demographics/method_technical_agg.csv')

organization = agg_column(data['F'], 'organization')
organization.to_csv('private_data/intech_demographics/organization_agg.csv')

position = agg_column(data['C'], 'position')
position.to_csv('private_data/intech_demographics/position_agg.csv')

role = agg_column(data['D'], 'role')
role.to_csv('private_data/intech_demographics/role_agg.csv')