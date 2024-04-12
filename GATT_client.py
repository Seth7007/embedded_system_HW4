#GATT_client.py:
from bluepy.btle import Peripheral, UUID
from bluepy.btle import DefaultDelegate

class ReadDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleNotification(self, cHandle, data):
        print ("Notification received:", int.from_bytes(data,"big")) #print Button Service notification value
#
print ("Connecting...")
dev = Peripheral("c4:5c:fc:95:18:2f", 'random') #change the MAC address of GATT server here
dev.setDelegate(ReadDelegate()) 

#
try:
    testService = dev.getServiceByUUID(UUID(0x180D)) # Heartrate service UUID 
    ch = dev.getCharacteristics(uuid=UUID(0x2A37))[0] # Heart Rate Measurement Characteristic UUID
    cccd = ch.getDescriptors(forUUID=0x2902)[0] # Get CCCD
    cccd.write(b'\x01\x00') # Enable notification
    while True:
        if dev.waitForNotifications(1.0):   
            # handleNotification() was called
            continue
        print("Waiting...") # No notification
#
finally:
    dev.disconnect()