This is embedded system HW4 

Two program, one runs a GATT server on STM32 to provide button service while another one runs a GATT client on Raspberry Pi to recive notification from server

The repository contains two codes:

main.cpp: modify from main.cpp of BLE_GattServer_AddService project(URL:https://github.com/ARMmbed/mbed-os-example-ble/tree/development/BLE_GattServer_AddService) to provid button service
To run this program, import BLE_GattServer_AddService project into mbed studio following the step taught in class and replace the original main.cpp with this one and the code is ready to run. 
Note that the program will print the MAC address of the device, which will need to be used in GATT_client.py

GATT_client.py: Use bluepy package to run a GATT client on Raspberry Pi
To run this program, modify the following line in GATT_clinet.py:

dev = Peripheral("c4:5c:fc:95:18:2f", 'random') #change the MAC address of GATT server here

After the modification, the code is ready to run.

Running program:
1. Runs GATT server on STM32 first(main.cpp)
2. Runs GATT client on Raspberry Pi(GATT_client.py)
3. If successfully connected, the Raspberry pi terminal should print Notification
4. While the user button is pressed, the notification received is 1 otherwise it is 0 
