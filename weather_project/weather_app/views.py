# from django.shortcuts import render

# # Create your views here.
# import datetime
# import requests 
# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     # file_path=r"C:\Users\nutan\OneDrive\Desktop\django\Django Weather\API_Key"
#     # API_KEY = open(file_path,"r").read()
#     API_KEY = "ced7c88b64b658095351f9cb5034dc7d"
#     # current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}-&appid={}"
#     current_weather_url = "https://api.openweathermap.org/data/2.5/weather?id=524901&appid={API_KEY}"
#     # forecast_weather_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}-&lon={}-&exclude=current,minutely,hourly,alerts&appid={}"
#     forecast_weather_url ="https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API_KEY}"
#     if request.method == "POST":
#         city1 = request.POST['city1']
#         city2 = request.POST.get('city2',None)
#         weather_data1,daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_weather_url)
#         if city2:
#             weather_data2,daily_forecasts2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url, forecast_weather_url)

#         else:
#            weather_data2, daily_forecasts2 = None, None 
#         context={
#             "weather_data1": weather_data1,
#             "daily_forecasts1" : daily_forecasts1,
#             "weather_data2": weather_data2,
#             "daily_forecasts2" : daily_forecasts2
#         }
#         return render(request,"weather_html/index.html", context)

#     else:
#         return render(request,"weather_html/index.html")
    
# def fetch_weather_and_forecast(city, api_key,current_weather_url,forecast_weather_url):
#     response = requests.get(current_weather_url.format(city,api_key)).json()
#     print(response)
#     # if 'coord' not in response:
#     #     # Handle the case where 'coord' key is missing in the response
#     #     return None, None

#     lat,lon = response['cod']['lat'], response['cod']['lon']
#     forecast_response = requests.get(forecast_weather_url.format(lat,lon,api_key)).json()
#     weather_data = {
#         "city" :city,
#         "temperature" : round(response['main']['temp'] - 273.15,2),
#         "description" : response['weather'][0]['description'],
#         "icon" : response['weather'][0]['icon']
#     }

#     daily_forecasts = []
#     for daily_data in forecast_response['daily'][:5]:
#         daily_forecasts.append({
#             "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
#             "min_temp" : round(daily_data['temp']['min']- 273.15,2),
#             "max_temp" : round(daily_data['temp']['max']- 273.15,2),
#             "description" : daily_data['weather'][0]['description'],
#             "icon" : daily_data['weather'][0]['icon']
#         })
#     return weather_data,daily_forecasts
                                    

from django.shortcuts import render
import requests
import datetime

def index(request):
    api_key = 'ced7c88b64b658095351f9cb5034dc7d'
    # api_key2 = '35c256dfbcd240acdcfdeb0daa452dec'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    # forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'
    forecast_url = 'https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'
    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, api_key, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, api_key, current_weather_url,
                                                                         forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            'weather_data1': weather_data1,
            'daily_forecasts1': daily_forecasts1,
            'weather_data2': weather_data2,
            'daily_forecasts2': daily_forecasts2,
        }

        return render(request, 'weather_html/index.html', context)
    else:
        return render(request, 'weather_html/index.html')


def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    print("response",response)
    print("forecast: ",forecast_response)

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    daily_forecasts = []
    # for daily_data in forecast_response['daily']:
    #     daily_forecasts.append({
    #         'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
    #         'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
    #         'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
    #         'description': daily_data['weather'][0]['description'],
    #         'icon': daily_data['weather'][0]['icon'],
    #     })

    return weather_data, daily_forecasts