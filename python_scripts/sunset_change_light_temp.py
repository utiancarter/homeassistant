warm_light_mireds = 500
cool_white_mireds = 326
daylight_mireds = 153

min_brightness_pct = 9
max_brightness_pct = 100

sleeptime_brightness_pct = 20
nighttime_brightness_pct = 60
daytime_brightness_pct = 100

lights_on = [light for light in hass.states.entity_ids(domain_filter = 'light') if hass.states.get(light).state == 'on']

logger.info(f'The sun is setting! These lights were found on: {", ".join(lights_on)}')

for light in lights_on:
    service_data = {
        "entity_id": light.entity_id, 
        "color_temp": warm_light_mireds, 
        "brightness_pct": nighttime_brightness_pct
        }
    hass.services.call("light", "turn_on", service_data, False)