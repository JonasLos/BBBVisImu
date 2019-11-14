# BBBVisImu
Program to send IMU data to laptop via wifi/UDP and run a visualization of the imu. 

Visualization Code was largely adopted from https://github.com/thecountoftuscany/PyTeapot-Quaternion-Euler-cube-rotation and only slightly modified to simplify data input. 

IMU2Quat_UDP.py is run on the Beaglebone Blue. It requires installation of rcpy if not already installed. 

UDPtoVis.py will run on a laptop. It requires installation of pygame and OpenGL if not already installed. 

You may need to adjust the Socket/UDP settings according to your own beaglebone and Laptop.
