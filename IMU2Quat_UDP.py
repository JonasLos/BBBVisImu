from time import sleep
import time
import getopt,sys
import math
import socket
import json
import rcpy
import rcpy.mpu9250 as mpu9250

UDP_IP_ADDRESS = "192.168.8.98"
UDP_PORT_NO = 5005

mpu9250.initialize(enable_dmp = True, dmp_sample_rate = 4, enable_magnetometer = True)

while(1):

        enable_magnetometer = True
        enable_fusion = True
        ImuArr = []

        # set state to rcpy.RUNNING
        rcpy.set_state(rcpy.RUNNING)

        if rcpy.get_state() == rcpy.RUNNING:
                data = mpu9250.read()
                quaternation = data['quat']
                q1 = data['quat'][0]
                q2 = data['quat'][1]
                q3 = data['quat'][2]
                q4 = data['quat'][3]
                ImuArr = (q1, q2, q3, q4)

                sendArr = json.dumps({"b":ImuArr})

                clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                clientSock.sendto(sendArr.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))

                if( socket.error == True):

                        print("Something went wrong connecting to the server!")
                        exit()

