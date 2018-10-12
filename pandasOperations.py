import pandas as pd

def pandas_operations(file_name):
    data = pd.read_excel(file_name)
    data['Accepted Compound ID'] = data['Accepted Compound ID'].apply(lambda x: str(x).split()[-1])
    data['Accepted Compound ID'][4] = data['Accepted Compound ID'][4][-3:]

    PC = data[data['Accepted Compound ID'] == 'PC']
    LPC = data[data['Accepted Compound ID'] == 'LPC']
    plasmalogen = data[data['Accepted Compound ID'] == 'plasmalogen']

    data_new = data
    data_new['Retention Time Roundoff (in mins)'] = data['Retention time (min)'].apply(lambda x: int(round(abs(x))))

    sample_means = data.drop(['m/z', 'Accepted Compound ID', 'Retention time (min)'], axis=1)

    for col in sample_means:
        sample_means[col] = sample_means.groupby('Retention Time Roundoff (in mins)')[col].transform('mean')

    PC.to_csv("PC.csv", sep=',')
    LPC.to_csv("LPC.csv", sep=',')
    plasmalogen.to_csv("plasmalogen.csv", sep=',')
    data_new.to_csv("data_new.csv", sep=',')
    sample_means.to_csv("sample_means.csv", sep=',')

