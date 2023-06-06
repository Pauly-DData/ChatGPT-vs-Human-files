import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

data_chatgpt = {
    'Module': 1119,
    'Import': 429,
    'Assign': 2519,
    'Expr': 2803,
    'alias': 910,
    'Name': 12471,
    'Call': 5236,
    'Store': 3073,
    'Attribute': 3960,
    'Constant': 6013,
    'Load': 15094,
    'keyword': 1786,
    'Subscript': 864,
    'Index': 787,
    'Tuple': 350,
    'List': 523,
    'Slice': 157,
    'For': 150,
    'If': 78,
    'JoinedStr': 16,
    'FormattedValue': 16,
    'FunctionDef': 54,
    'arguments': 93,
    'arg': 142,
    'Compare': 213,
    'Return': 53,
    'Eq': 83,
    'Lambda': 39,
    'Assert': 9,
    'GtE': 21,
    'BinOp': 297,
    'Mult': 72,
    'Dict': 76,
    'UnaryOp': 73,
    'USub': 66,
    'Sub': 69,
    'ImportFrom': 362,
    'ExtSlice': 74,
    'With': 26,
    'withitem': 26,
    'FloorDiv': 2,
    'ListComp': 46,
    'comprehension': 54,
    'Div': 48,
    'BoolOp': 8,
    'And': 5,
    'Not': 7,
    'IsNot': 1,
    'Add': 129,
    'ClassDef': 2,
    'Try': 3,
    'ExceptHandler': 3,
    'Continue': 2,
    'AugAssign': 41,
    'In': 21,
    'Delete': 5,
    'Del': 5,
    'Pow': 15,
    'NotEq': 7,
    'LtE': 27,
    'Gt': 23,
    'Lt': 24,
    'Or': 3,
    'While': 10,
    'NotIn': 6,
    'Break': 6,
    'Mod': 2,
    'Starred': 4,
    'SetComp': 2,
    'GeneratorExp': 4,
    'Set': 2,
    'IfExp': 2,
    'DictComp': 2,
    'BitAnd': 1,
    'Nonlocal': 1,
    'Raise': 1,
    'Yield': 2,
    'AnnAssign': 2
}

data_github = {
    'Module': 567,
    'Import': 120,
    'Assign': 929,
    'Expr': 1116,
    'alias': 251,
    'Name': 4666,
    'Call': 2121,
    'Store': 1046,
    'Attribute': 1571,
    'Constant': 2337,
    'Load': 5834,
    'keyword': 838,
    'Subscript': 305,
    'Index': 276,
    'Tuple': 150,
    'List': 187,
    'Slice': 76,
    'For': 1,
    'If': 0,
    'JoinedStr': 0,
    'FormattedValue': 0,
    'FunctionDef': 0,
    'arguments': 18,
    'arg': 22,
    'Compare': 53,
    'Return': 0,
    'Eq': 19,
    'Lambda': 18,
    'Assert': 2,
    'GtE': 8,
    'BinOp': 112,
    'Mult': 37,
    'Dict': 24,
    'UnaryOp': 33,
    'USub': 33,
    'Sub': 31,
    'ImportFrom': 119,
    'ExtSlice': 41,
    'With': 0,
    'withitem': 0,
    'FloorDiv': 0,
    'ListComp': 17,
    'comprehension': 19,
    'Div': 15,
    'BoolOp': 2,
    'And': 1,
    'Not': 0,
    'IsNot': 0,
    'Add': 25,
    'ClassDef': 0,
    'Try': 0,
    'ExceptHandler': 0,
    'Continue': 0,
    'AugAssign': 1,
    'In': 1,
    'Delete': 1,
    'Del': 4,
    'Pow': 1,
    'NotEq': 3,
    'LtE': 9,
    'Gt': 10,
    'Lt': 1,
    'Or': 0,
    'While': 2,
    'NotIn': 0,
    'Break': 0,
    'Mod': 2,
    'Starred': 1,
    'SetComp': 1,
    'GeneratorExp': 0,
    'Set': 0,
    'IfExp': 1,
    'DictComp': 1,
    'BitAnd': 0,
    'Nonlocal': 0,
    'Raise': 0,
    'Yield': 1,
    'AnnAssign': 1
}

# your existing code goes here

mean_chatgpt = {k: v / 764 for k, v in data_chatgpt.items()}
mean_github = {k: v / 764 for k, v in data_github.items()}

sd_chatgpt = {
    k: np.sqrt((v / 764) * (1 - v / 764)) if v <= 764 else 0
    for k, v in data_chatgpt.items()
}
sd_github = {
    k: np.sqrt((v / 764) * (1 - v / 764)) if v <= 764 else 0
    for k, v in data_github.items()
}

# Convert the dictionaries to pandas DataFrames
df_mean_chatgpt = pd.DataFrame.from_dict(mean_chatgpt, orient='index', columns=['Mean_ChatGPT'])
df_mean_github = pd.DataFrame.from_dict(mean_github, orient='index', columns=['Mean_GitHub'])
df_sd_chatgpt = pd.DataFrame.from_dict(sd_chatgpt, orient='index', columns=['SD_ChatGPT'])
df_sd_github = pd.DataFrame.from_dict(sd_github, orient='index', columns=['SD_GitHub'])

# Merge the dataframes
df = pd.concat([df_mean_chatgpt, df_mean_github, df_sd_chatgpt, df_sd_github], axis=1)

# Add empty columns for t-test and p-value
df['t-test'] = np.nan
df['p-value'] = np.nan

# For each item, calculate the t-test and p-value
for item in df.index:
    chatgpt_values = np.repeat([0, 1], [int((1 - df.loc[item, 'Mean_ChatGPT']) * 764), int(df.loc[item, 'Mean_ChatGPT'] * 764)])
    github_values = np.repeat([0, 1], [int((1 - df.loc[item, 'Mean_GitHub']) * 764), int(df.loc[item, 'Mean_GitHub'] * 764)])

    t_test, p_value = ttest_ind(chatgpt_values, github_values, equal_var=False)
    
    df.loc[item, 't-test'] = t_test
    df.loc[item, 'p-value'] = p_value

# Write the updated dataframe to an Excel file
df.to_excel('results_with_ttests.xlsx')


