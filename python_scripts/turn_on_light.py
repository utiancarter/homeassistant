color = dict()
color["warm_light"] = [252, 249, 217] # HEX = FCF9D9 https://www.color-name.com/warm-light.color
color["cool_white"] = [244, 253, 255] # HEX = F4FDFF https://www.color-name.com/cool-white.color
color["daylight"] = [244, 233, 155] # HEX = F4E99B https://www.color-name.com/sunlight.color

nighttime_brightness = 25
daytime_brightness = 100

entity_id = data.get("entity_id")
rgb_color = data.get("rgb_color", [255, 255, 255])

if datetime.datetime.now().hour < 6:
    brightness = nighttime_brightness
else:
    brightness = daytime_brightness

if entity_id is not None:
    service_data = {"entity_id": entity_id, "rgb_color": rgb_color, "brightness": 255}
    hass.services.call("light", "turn_on", service_data, False)
