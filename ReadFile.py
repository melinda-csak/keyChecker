# TODO: read file into a format that is useable for future usage (for example dataFrame?)


# importing values from a .CSV file to create Pandas DataFrame
import pandas
# loading data into a DataFrame object
# What's the separator? Is there a header?
sep = input("Separator character:" )
header = input("Header yes(1) or no(0): ")
data = pandas.read_csv(input("Insert file path: "), sep, header)
df = pandas.DataFrame(data)
# loading Pandas DataFrame into an SQL database
#df.to_sql()