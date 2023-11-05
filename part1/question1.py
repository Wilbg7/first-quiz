def get_city_temperature(city):
   if city == "Quito":
      return "22 degrees and sunny"
   if city == "Sao Paulo":
      return "17 degrees and cloudy"
   if city == "San Francisco":
      return "16 degrees and sunny"
   if city == "New York":
      return "14 degrees"
   else:
      return "City not found"


def get_city_weather(city):
  sky_condition = None

  if city == "Sao Paulo":
     sky_condition = "cloudy"
  elif city == "New York":
     sky_condition = "rainy"

  temperature = get_city_temperature(city)

  if sky_condition is None:
     return temperature
  else:
     return temperature + " and " + sky_condition
