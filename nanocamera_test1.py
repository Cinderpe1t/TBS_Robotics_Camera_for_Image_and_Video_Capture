import cv2
#from nanocamera.NanoCam import Camera
import nanocamera as nano

if __name__ == '__main__':
    # Create the Camera instance
    camera0 = nano.Camera(device_id=0, flip=0, width=640, height=480, fps=20)
    camera1 = nano.Camera(device_id=1, flip=0, width=640, height=480, fps=20)

    print('CSI Camera ready? - ', camera0.isReady())
    while camera0.isReady() and camera1.isReady():
        try:
            # read the camera image
            #frame0 = camera0.read()
            #frame1 = camera1.read()
            # display the frame
            #cv2.putText(frame0,'Front',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
            #cv2.putText(frame1,'Back',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
            cv2.imshow("0F", camera0.read())
            cv2.imshow("1B", camera1.read())
            if cv2.waitKey(3) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break

    # close the camera instance
    camera0.release()    
    camera1.release()

    # remove camera object
    del camera0
    del camera1
