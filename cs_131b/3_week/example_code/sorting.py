# add the JCPA to a dictionary of past treaties
treaties = {
'Nuclear Test Ban Treaty': 1963,
'Treaty of Peace with Japan': 1951,
'Hague Conventions': 1899,
'Peace of Olomouc': 1479,
'Treaty of Windsor': 1175,
'Ili River Treaty': 638
}
treaties [ 'Joint Comprehensive Plan of Action' ] = 2015
# Order treaties by name (key) functionally.
print (sorted(treaties))
# Order treaties by year (value) functionally.
print (sorted(treaties, key=treaties.get))
# Order list of years procedurally.
years = list(treaties.values())
years.sort()
print (years)