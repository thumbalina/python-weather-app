import requests,json
api_key="eee8ed69f434ad81b27a47ef58ceb194"
base_url="http://api.openweathermap.org/data/2.5/weather?q="
city_name=input("Enter city name:")
complete_url=base_url +city_name+"&units=metric"+ "&APPID=" + api_key 
response = requests.get(complete_url)
x=response.json()
print(x)
if x["cod"] != "404":
    y=x["main"]
    
   current_temperature=y["temp"]
   current_pressure=y["pressure"]
   current_humidity=y["humidity"]
    z=x["weather"]
   weather_description= z[0]["description"]    
   print("temperature (in celcius unit) = " + str(current_temperature)+
         "\n atmospheric pressure (in hPa unit)="+ str(current_pressure) + 
         "\n humidity(in percentage) = "+str(current_humidity)+
         "\n description = " + str(weather_description))
else:
   print("city not found")