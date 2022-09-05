# sometimes, e-prime doesn't read the images ( We still don't know why). This basic script will fix the whole process.

import os
import cv2

def fix_bullshit(path, new_path):
    for file in os.listdir(path):
        img = cv2.imread(os.path.join(path, file))
        cv2.imwrite(os.path.join(new_path, file[:-3] + 'bmp'), img)
        
fix_bullshit(r'C:\Users\altunenes\Desktop\imagefolder', r'C:\Users\altunenes\Desktop\exportfolder')
