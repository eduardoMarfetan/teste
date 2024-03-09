from apiip import apiip
import key

api_client = apiip('3c273867-17f2-4f27-9f62-cb59defd81f9')

info = api_client.get_location({
    'ip': "67.250.186.196", # '67.250.186.196, 188.79.34.191, 60.138.7.24' - for bulk request
    'output': "xml",
    'fields': "city, countryName, capital, currency.name",
    'languages': "pt-br",
})

print(info)