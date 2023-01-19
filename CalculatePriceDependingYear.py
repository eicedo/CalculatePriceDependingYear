year_1962_to_1964 = 18500  
year_1965_to_1968 = 6000 
year_1969_to_1971 = 12000 
year_1972_to_1975 = 48000 
year_1976_to_1980 = 200000 
year_1981_to_1985 = 650000 
year_1986_to_2012 = 35000000
year_2013_to_2014 = 52000000  
year_outseide_range = 0

year = int(input('Enter the year of a Ferrari 250 GTO to display value: \n'))


if year >=1962 and year <=1964:
    value = year_1962_to_1964
elif year >= 1965 and year <= 1968:
    value = year_1965_to_1968
elif year >= 1969 and year <= 1971:
    value = year_1969_to_1971
elif year >= 1972 and year <= 1975:
    value = year_1972_to_1975
elif year >= 1976 and year <= 1980:
    value = year_1976_to_1980
elif year >= 1981 and year <= 1985:
    value = year_1981_to_1985
elif year >= 1986 and year <= 2012:
    value = year_1986_to_2012
elif year >= 2013 and year <= 2014:
    value = year_2013_to_2014
else :
    print('Input a year from 1962-2014.')
    value = year_outseide_range

print('Ferrari 250 GTO Value: $%d' % value)
