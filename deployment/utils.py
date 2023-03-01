"""Deployment of Financial Inclusion model. Utilities"""


# helper functions for wrangle function

def group_household_size(x):
    if x<5:
        return 1
    elif x<10:
        return 2
    else:
        return 3

def group_age(x):
    if x>=15 and x<25:
        return (1)
    if x>=25 and x<35:
        return (2)
    if x>=35 and x<45:
        return (3)
    if x>=45 and x<55:
        return (4)
    if x>=55 and x<65:
        return (5)
    if x>=65 and x<75:
        return (6)
    if x>=75 and x<85:
        return (7)
    if x>=85 and x<95:
        return (8)
    if x>=95 and x<=105:
        return (9)

def wrangle(input, test=False):
    """ Wrangle function to process user input
    
    Args:
        filepath (str): path to the file containing data
        test (bool): False, track test file for necessary differences
                            in processing
    Return:
        df (pd.DataFrame): result of the wrangling process
    """
    df = pd.read_csv(input)
    
    # conert year to a datetime type
    df.year = pd.to_datetime(df.year.astype('int32'), format='%Y')

    # convert cellphone_access column to boolean
    df.cellphone_access = df.cellphone_access.astype('bool')

    if test == False:
        # convert target column, bank_account, to 0's and 1's
        df.bank_account = df.bank_account.map({'Yes':1, 'No':0})

    # create x group column
    df['age_group'] = list(map(group_age, df.age_of_respondent))

    # group household_sizes
    df['house_size_groups'] = list(map(group_household_size, df.household_size))

    # create 'Other' category in relationship_with_head column
    df.relationship_with_head = df.relationship_with_head.replace({'Other relative':'Other', 'Other non-relatives':'Other'})

    # set index
    df.set_index(df.uniqueid, inplace=True)

    # drop columns
    df.drop(columns=['uniqueid', 'age_of_respondent', 'household_size'], inplace=True)

    return df
