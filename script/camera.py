import numpy as np
import time
import imutils
import cv2
from harvesters.core import Harvester

class Camera (Harvester):

    def __init__(self):
        super().__init__()
        self.img_cap = None
        self.add_file('/usr/lib/ids/cti/ids_gevgentlk.cti') # for windows: 'C:/Program Files/IDS/ids_peak/ids_gevgentl/64/ids_gevgentlk.cti'
        self.update()
    
    def capture_image(self):
        # Create image acquirer
        self.img_cap = self.create_image_acquirer(list_index=0)
        self.img_cap.remote_device.node_map.PixelFormat.value = 'Mono8'
        # Camera params
        self.img_cap.remote_device.node_map.Width.value=2448
        self.img_cap.remote_device.node_map.Height.value=2048

        # Acquisition
        self.img_cap.start_acquisition()
 
        with self.img_cap.fetch_buffer() as buffer:
            component = buffer.payload.components[0]
            # reshape to a 2D array
            _2d = component.data.reshape(component.height, component.width)

        # Stop acquisition
        self.img_cap.stop_acquisition()
        return _2d

    def release_cti(self):
        # Disconnect device
        self.img_cap.destroy()
        self.reset()


# IMAGE PROCESSING 
if __name__ == "__main__":
    # Connection
    print("-------------------------------------------------------------------------")
    print('[CONNECTING] - running')
    print('Finding Devices...')
    cam = Camera()
    print(f'Devices found: {len(cam.device_info_list)}')
    
    print("-------------------------------------------------------------------------")
    print('[ACQUIRING] - running')
    # Image Capture
    sample_image = cam.capture_image()
    print("Done.")

    print("-------------------------------------------------------------------------")
    print('[PROCESSING HERE]')
    # Image Processing
    print("...")
    # Image Visualization
    # window = cv2.namedWindow('output', cv2.WINDOW_NORMAL) # test purposes
    # cv2.imshow('output', image_inspection)
    # cv2.waitKey(0)

    print("-------------------------------------------------------------------------")
    print('[DISCONNECTING] - running')
    print("Closing...")
    cam.release_cti()
    print("Closed.")
