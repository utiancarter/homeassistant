warm_light_mireds = 500
cool_white_mireds = 326
daylight_mireds = 153

min_brightness_pct = 9
max_brightness_pct = 100

sleeptime_brightness_pct = 20
nighttime_brightness_pct = 60
daytime_brightness_pct = 100

# Get list of entity_ids whose state is "on" and is not a group
lights_on = [light for light in hass.states.entity_ids(domain_filter = 'light') if ((hass.states.get(light).state == 'on') & ('icon' not in hass.states.get(light).as_dict().keys()))]

# Remove lights which color_mode is color_temp:
for light in lights_on:
    if hass.states.get(light).color_mode == 'color_temp':
        lights_on.remove(light)

logger.info(f'The sun is setting! These lights were found on and set to color_temp: {", ".join(lights_on)}')

def adjust_light(light, mireds, brightness_pct):
    service_data = {
        "entity_id": light, 
        "color_temp": mireds, 
        "brightness_pct": brightness_pct
        }
    hass.services.call("light", "turn_on", service_data, False)

for light in lights_on:
    adjust_light(light, daylight_mireds, nighttime_brightness_pct)