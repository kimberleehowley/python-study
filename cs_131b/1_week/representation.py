# This program calculates how much more represented in the Senate a resident of Idaho is than a resident of Florida
#  Using US census data 2010-2019: https://www.census.gov/data/tables/time-series/demo/popest/2010s-state-total.html

fl_population = 21477737
id_population = 1787065

diff_population = 21477737 // 1787065  

print('Each US state has 2 senators, no matter its population.\n')
print('According to the most recent US census data, Florida has roughly ', diff_population,' times the population of Idaho. But, like Idaho, it only gets 2 Senators.\n')
print('Therefore, a resident of Idaho is roughly ', diff_population,' times more represented in the Senate than a resident of Florida.') 

