

## Aggregation using dicts

# Method 1 : Using Apply function - preferred for BIG datasets

# For Dict Creation :
# Format:  <'aggregated name'> : df[<'col name'>].func()


def my_agg(x):
    names = {
        'Amount mean': x['Amount'].mean(),
        'Amount std':  x['Amount'].std(),
        'Amount range': x['Amount'].max() - x['Amount'].min(),
        'Score Max':  x['Score'].max(),
        'Score Sum': x['Score'].sum(),
        'Amount Score Sum': (x['Amount'] * x['Score']).sum()}

    return pd.Series(names, index=['Amount range', 'Amount std', 'Amount mean',
                                   'Score Sum', 'Score Max', 'Amount Score Sum'])
								   
df.groupby('User').apply(my_agg)


# Method 2 : Using .agg() funtion - Preferred for ad-hoc analysis or smaller datasets
 

df.groupby('User')['Amount'].agg(['sum', 'count'])


# Output :

# #        sum  count
# # User              
# # user1  18.0      2
# # user2  20.5      3
# # user3  10.5      1

df = pd.DataFrame({"User": ["user1", "user2", "user2", "user3", "user2", "user1"],
              "Amount": [10.0, 5.0, 8.0, 10.5, 7.5, 8.0],
              'Other': [1,2,3,4,5,6]})

df.groupby('User').agg({'Amount' : ['sum', 'count'], 'Other':['max', 'std']})

# Output :

##       Amount       Other          
##          sum count   max       std
## User                              
## user1   18.0     2     6  3.535534
## user2   20.5     3     5  1.527525
## user3   10.5     1     4       NaN
