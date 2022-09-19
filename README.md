# TBS_Robotics_Camera_for_Image_and_Video_Capture
TBS Robotics Camera for Image and Video Capture
## Preparation
- JETSON Nano
- RPi compatible camera module
- OpenCV (cv2) library
- JETSON nanocamera library
## Accessories
- Camera mount from Adafruit. https://www.adafruit.com/product/1434
  - Or we can laser cut it for custom design. 
- Camera lense focus tool from Adafuit https://www.adafruit.com/product/3518
## CV2 is powerful openCV graphic and image process library
- https://docs.opencv.org/4.x/index.html
- https://pypi.org/project/opencv-python/ 
## Preparation
- Install cv2 library to python
- Carefully connect camera cable to JETSON (or RPi) and camera module
- Avoid pulling camera cable from boards. The connector will break under excessive force.
- JETSON Nano has two camera I/O ports
## Run example python script
- The first camera `device_id` is `0` and the second camera is `1`
- Size resolution and frame rate can be adjusted
```
    camera0 = nano.Camera(device_id=0, flip=0, width=640, height=480, fps=20)
    camera1 = nano.Camera(device_id=1, flip=0, width=640, height=480, fps=20)
```
- Text can be added to the video using cv2 library
```
  cv2.putText(frame0,'Front',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
  cv2.putText(frame1,'Back',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
```
- Object boundary can be detected using cv2 libary as one simple example of powerful cv2 processing
- `python3 nanocamera_test1.py`
## Measure video capture and display latency 
- Video processing can cause delay in video and frustrate robot driving
- What would be acceptable latency in second to allow real-time feedback robot driving?
