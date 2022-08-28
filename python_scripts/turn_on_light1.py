light = dict()

light["warm_light_mireds"] = 500
light["cool_white_mireds"] = 326
light["daylight_mireds"] = 153

light['min_brightness_pct'] = 9
light['max_brightness_pct'] = 100

sleeptime_brightness_pct = 20
nighttime_brightness_pct = 60
daytime_brightness_pct = 100

entity_id = data.get("entity_id")

transition = 1

# if datetime.datetime.now().hour < 6:
#     brightness = sleeptime_brightness_pct
#     color_temp = light["warm_light_mireds"]
# elif datetime.datetime.now().hour > 20:
#     brightness = nighttime_brightness_pct
#     color_temp = light["warm_light_mireds"]
# else:
#     brightness = daytime_brightness_pct
#     color_temp = light["warm_light_mireds"]

brightness = daytime_brightness_pct
color_temp = light['warm_light_mireds']

# if hass.states.get('weather.forecast_207a_home') in ['Rainy', 'Cloudy']:
#     color_temp = light["daylight_mireds"]

if entity_id is not None:
    service_data = {"entity_id": entity_id, "color_temp": color_temp, "brightness_pct": brightness}
    hass.services.call("light", "turn_on", service_data, False)
