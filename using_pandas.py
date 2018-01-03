# using pandas library for table manipulations
import pandas as pd

# read a csv file
ideabook = pd.read_csv('data/ideabook_vancouver.csv')
survey = pd.read_csv('data/survey_vancouver.csv')

# view the data
print ideabook[:3]
print survey[:3]

print ideabook.shape, survey.shape

print ideabook.columns
print survey.columns

# concatenate 2 dataframes row wise
survey_van = survey
survey_toronto = survey
survey_national = pd.concat([survey_van, survey_toronto])

# merge the data by column
data_merged = pd.merge(ideabook, survey, how='inner', on='ID')


sample_df = pd.DataFrame({'col1': ['K0', 'K0', 'K3', 'K3', 'K4', 'K5'],'col2': ['A0', 'A1', 'A0', 'A3', 'A0', 'A5']})
# count each element in the column
counts = sample_df.groupby('col1').count()
counts.columns = ['counts']
print counts

# get % of each element in column
percentages = []
for i in range(len(counts)):
    val = float(counts.ix[i])
    perc = float(val)/float(counts['counts'].sum())
    percentages.append(perc)

# add percentages as additional column
counts['percentages'] = percentages