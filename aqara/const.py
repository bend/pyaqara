"""Constants of the aqara protocol"""

MCAST_ADDR = "224.0.0.50"
MCAST_PORT = 4321

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 9898

GATEWAY_PORT = 9898

AQARA_DEVICE_HT = 'sensor_ht'
AQARA_DEVICE_HT1 = 'weather.v1'
AQARA_DEVICE_MOTION = 'motion'
AQARA_DEVICE_MOTION2 = 'sensor_motion.aq2'
AQARA_DEVICE_MAGNET = 'magnet'
AQARA_DEVICE_MAGNET2 = 'sensor_magnet.aq2'
AQARA_DEVICE_SWITCH = 'switch'
AQARA_DEVICE_SWITCH2 = 'sensor_switch.aq2'
AQARA_DEVICE_GATEWAY = 'gateway'
AQARA_DEVICE_PLUG = 'plug'

AQARA_SWITCH_ACTION_CLICK = 'click'
AQARA_SWITCH_ACTION_DOUBLE_CLICK = 'double_click'
AQARA_SWITCH_ACTION_LONG_CLICK_PRESS = 'long_click_press'
AQARA_SWITCH_ACTION_LONG_CLICK_RELEASE = 'long_click_release'

AQARA_MID_STOP = 10000

AQARA_ENCRYPT_IV = b'\x17\x99\x6d\x09\x3d\x28\xdd\xb3\xba\x69\x5a\x2e\x6f\x58\x56\x2e'

AQARA_EVENT_NEW_GATEWAY = 'aqara_new_gateway'
AQARA_EVENT_NEW_DEVICE = 'aqara_new_device'

AQARA_DATA_VOLTAGE = "voltage"
AQARA_DATA_STATUS = "status"
AQARA_DATA_TEMPERATURE = "temperature"
AQARA_DATA_HUMIDITY = "humidity"
AQARA_DATA_PRESSURE = "pressure"
AQARA_DATA_ACTION = "action"
AQARA_DATA_RGB = "rgb"
AQARA_DATA_ILLUMINATION = "illumination"
