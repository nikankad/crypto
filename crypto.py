import requests
#change name of coin in the response variable for the current price of that coin, look at the url for more options,  can get data for multiple currencies as well.
#variables
#alot of coins and currencies are avaliable, check https://www.coingecko.com/en/api#explore-api and the "/coins/{id}" tab for more options
crypto = "bitcoin" #can be many different cryptocurrencies, like ethereum
currency = "usd"   #can be many different currencies, like eur

response = requests.get('https://api.coingecko.com/api/v3/coins/'+crypto+'.json')
data = response.json()
rate = data["market_data"]["current_price"][currency]

#formats price to have a comma, for eg 42322 will be 42,322, uncomment it to activate
#rate = "{:,}".format(rate)

print(rate)
