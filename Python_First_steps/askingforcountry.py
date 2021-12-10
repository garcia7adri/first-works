#asking for a country, add in it to a dictionary and count for repetitions.

countryList=[]
for i in range (5):

    country=input("Please enter your country: ")
    countryList.append(country.capitalize())

CountryDictionary={}
for country in countryList:
    if country in CountryDictionary:
        CountryDictionary[country]+=1
    else:
        CountryDictionary[country]=1
print (CountryDictionary)