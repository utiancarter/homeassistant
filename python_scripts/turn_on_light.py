warm_light_mireds = 500
cool_white_mireds = 326
daylight_mireds = 153

min_brightness_pct = 9
max_brightness_pct = 100

sleeptime_brightness_pct = 20
nighttime_brightness_pct = 60
daytime_brightness_pct = 100

entity_id = data.get("entity_id")

# transition = 1

# If the time is between midnight and 7am
if datetime.datetime.now().hour < 7:
    brightness = sleeptime_brightness_pct
    color_temp = warm_light_mireds
# If the time is between 6am and 8pm
elif datetime.datetime.now().hour > 20:
    brightness = nighttime_brightness_pct
    color_temp = cool_white_mireds
# If the time is after 8pm
else:
    brightness = nighttime_brightness_pct
    color_temp = daylight_mireds

current_weather_state = hass.states.get('weather.forecast_207a_home').state
logger.info(f'The weather is currently {current_weather_state}')

if current_weather_state in ['rainy', 'cloudy']:
    color_temp = daylight_mireds

if entity_id is not None:
    service_data = {"entity_id": entity_id, "color_temp": color_temp, "brightness_pct": brightness}
    hass.services.call("light", "turn_on", service_data, False)