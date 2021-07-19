# Video_OpenVibe
My code alow to display video with OpenVibe with the OpenCV library 

## Before you can use it you need to download : 
- Python 3.7.8 (only version of python that is allowed by OpenVibe)
- OpenCV 4.5.1 (with > *pip install opencv-python* and > *pip install opencv-contrib-python*)

You also need to **change the path** of the file in:

- On Protocole.py line 81

 
## Disclaimer: 
It cannot be used with long videos because while python is displaying the video Openvibe is not writting the EEG signal and it is stocked in the RAM. With my personnal computer with 8 Go of RAM I have no issue with a 10 second video. 
