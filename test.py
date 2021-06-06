#!/usr/bin/env python3

import os
import homeassistantclient

TOKEN = os.getenv('HA_ACCESS_TOKEN')

api = homeassistantclient.HAAPI(host="192.168.33.168:8123", access_token=TOKEN)
hlt = api.get_state(entity_id="sensor.hlt_temp")

print(hlt["state"])
