import pandas as pd
def disc_cont_cat(dataframe,target):
    # numerical: discrete
    discrete = [
        var for var in dataframe.columns if dataframe[var].dtype != 'category' and var != target
        and dataframe[var].nunique() < 10
    ]

    # numerical: continuous
    continuous = [
        var for var in dataframe.columns
        if dataframe[var].dtype != 'category' and var != target and var not in discrete
    ]

    # categorical
    categorical = [var for var in dataframe.columns if dataframe[var].dtype == 'category' and dataframe[var].nunique() > 1]

    print('There are {} discrete variables'.format(len(discrete)))
    print('There are {} continuous variables'.format(len(continuous)))
    print('There are {} categorical variables'.format(len(categorical)))
    # print("numerical_features: ",len(numerical_features))
    # print("category_features: ",len(category_features))
    return discrete, continuous, categorical