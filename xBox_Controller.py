from inputs import get_gamepad
from inputs import DeviceManager

#devices = DeviceManager()
while 1:
	events = get_gamepad()
	for event in events:
		print( event.code)
		