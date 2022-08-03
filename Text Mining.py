import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)


def date_sorter():
    
    #Your code here
    d1 = df.str.extract(r'(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2,4})').dropna(how = 'any')
    d2 = df.str.extract(r'(?:^| |~|[a-z])+-?(?P<day>)[\(]?(?P<month>\d{1,2})[/-](?P<year>\d{4})').dropna(how = 'any')
    d3 = df.str.extract(r'[^ ,.-/]+(?P<month> )[^0-9][^ ,.-/]+(?P<day> )[a-z\s|\W]+(?P<year>\d{4})\D').dropna(how = 'any')
    d3_1 = df.str.extract(r'(?P<month>)(?P<day>)^[\W*\D]?(?P<year>\d{4})').dropna(how = 'any')
    d3_2 = df.str.extract(r'(?P<month>)(?P<day>)[(](?P<year>\d{4})[-]').dropna(how = 'any')
    d3_3 = df.str.extract(r'(?P<month>)(?P<day>)[^?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]\s[a-z]*:\s+(?P<year>\d{4})\W').dropna(how = 'any')
    d3_4 = df.str.extract(r'(?P<month>)(?P<day>)[^?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]\s[a-z]*;\s+(?P<year>\d{4})\W').dropna(how = 'any')
    d3_5 = df.str.extract(r'(?P<month>)(?P<day>)[^?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec].[A-Za-z0-9],\s+(?P<year>\d{4}),').dropna(how = 'any')
    d3_6 = df.str.extract(r'[^ ,.-/](?P<month>) [^0-9][^ ,.-/](?P<day>)[\b0-9\s]+(?P<year>\d{4})\n').dropna(how = 'any')
    d3_7 = df.str.extract(r'(?P<month>)(?P<day>)[^?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec] [A-Z][a-z]\s+(?P<year>\d{4}).').dropna(how = 'any')
    d3_8 = df.str.extract(r'(?P<month>)(?P<day> )[a-z]{8} (?P<year>\d{4})').dropna(how = 'any')
    d3_9 = ## insert code ...
    d3_10 = ## insert code ...
    d4 = df.str.extract(r'(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[ ,.-]+(?P<day>\d{1,2})[ ,.-]+(?P<year>\d{2,4})').dropna(how = 'any')
    d5 = df.str.extract(r'(?P<day>\d{1,2})[ ,.-](?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[ ,.-](?P<year>\d{2,4})').dropna(how = 'any')
    d6 = df.str.extract(r'(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[ ,.](?P<day>\d{1,2})(?:th|st|rd),(?P<year>\d{2,4})').dropna(how = 'any')
    d7 = df.str.extract(r'\D(?P<day> )(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*),?[ ](?P<year>\d{4})').dropna(how = 'any')
    d7_1 = df.str.extract(r'^[\D\. ]?(?P<day>)(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[,. ]*(?P<year>\d{4})\D').dropna(how = 'any')
    d7_2 = df.str.extract(r'[^]*[\D\. ](?P<day>)(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)[,. ]*(?P<year>\d{4})\D').dropna(how = 'any')
    d7_3 = df.str.extract(r'\D(?P<day> )[()](?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*),?[ ](?P<year>\d{4})[)]').dropna(how = 'any')
    ## insert the remaining Regx Expression for d3_9 and d3_10 to complete the text mining task. Goodluck!

    def month(string):
        m = {'JAN': 1,'FEB': 2,'MAR': 3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}
        s = string.strip()[:3].upper()
        try:
            out = m[s]
            return out
        except:
            raise ValueError('Not a month')

    # testing the function
    #month('October')
    for index, row in d3.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3
    for index, row in d3_1.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])        
    d3_1
    for index, row in d3_2.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_2
    for index, row in d3_3.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_3
    for index, row in d3_4.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_4
    for index, row in d3_5.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_5
    for index, row in d3_6.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_6
    for index, row in d3_7.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_7
    for index, row in d3_8.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_8
    for index, row in d3_9.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_9
    for index, row in d3_10.iterrows():
        row['month'] = 'January'
        row['month'] = month(row['month'])
    d3_10
    for index, row in d4.iterrows():
        row['month'] = month(row['month'])
    d4
    for index, row in d5.iterrows():
        row['month'] = month(row['month'])
    d5
    for index, row in d7.iterrows():
        row['month'] = month(row['month'])
    d7
    for index, row in d7_1.iterrows():
        row['month'] = month(row['month'])
    d7_1
    for index, row in d7_2.iterrows():
        row['month'] = month(row['month'])
    d7_2
    for index, row in d7_3.iterrows():
        row['month'] = month(row['month'])
    d7_3

    dataset = [d1, d2, d3, d3_1, d3_2, d3_3, d3_4, d3_5, d3_6, d3_7, d3_8, d3_9, d3_10, d4, d5, d6, d7, d7_1, d7_2, d7_3]
    dataset_result = pd.concat(dataset)
    dataset_result = dataset_result.replace(r'^\s*$', 1 , regex=True)

    for index, row in dataset_result.iterrows():
        if len(row['year'])<3:
            row['year'] = '19'+row['year']
        if len(str(row['day'])) ==1:
            row['day'] = '0'+str(row['day'])
        if len(str(row['month'])) ==1:
            row['month'] = '0'+str(row['month'])
    dataset_result
    dataset_result = dataset_result.applymap(str)

    dataset_result["combine"] = dataset_result["month"]+'/'+dataset_result["day"]+'/'+dataset_result["year"]
    #print(dataset_result["combine"])
    #print(dataset_result.dtypes)
    dataset_result["combine"] = pd.to_datetime(dataset_result["combine"], format="%m/%d/%Y")
    final_answer = pd.to_datetime(dataset_result["combine"], format="%m/%d/%Y")
    final_answer = pd.DataFrame(final_answer)
    final_answer = final_answer.sort_values(ascending=True, by = "combine")
    final_answer.reset_index(inplace=True)
    final_answer['index'] = pd.Series(final_answer['index'])
    return final_answer['index'] #Your answer here
date_sorter()