import cv2
import numpy as np
from PIL import ImageGrab

def screenRec():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.mp4",fourcc,5.0,(1400,768))
    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen_Rec",frame)
        out.write(frame)

        if cv2.waitKey() == 27:#press escape to exit
            break
    
    out.release()
    cv2.destroyAllWindows()


screenRec()
