import numpy as np
import os
import cv2
import os
from CleanImages_Functions import *

scale = 0.2
height = 50
width = 50

# Ruta al dataset
data_dir= 'dataset/imagenes'
data_dir_clean = ['dataset/imagenes_clean_equalHist', 'dataset/imagenes_clean_fourier']

# Listar y cargar imágenes
image_array = []

for label in ["estrellas", "galaxias"]:

    data_dir_label = data_dir + "/" + label

    for dir in data_dir_clean:

        data_dir_process = dir + "/" + label

        os.makedirs(data_dir_process, exist_ok=True)

        file_names = sorted(os.listdir(data_dir_label))

        for fname in file_names:

            if fname.endswith(('.png', '.jpg', '.jpeg')):

                img_path = os.path.join(data_dir_label, fname)

                img = cv2.imread(img_path)

                pixels_totrim = 12

                img = img[pixels_totrim:-pixels_totrim,pixels_totrim:-pixels_totrim,:]

                img_processed = thresholdImg(img)

                # cv2.namedWindow(f"{fname}", cv2.WINDOW_NORMAL) 
                # cv2.imshow(f"{fname}", img_processed.astype(np.uint8))
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                            
                writeBool = cv2.imwrite(f"{data_dir_process}/{fname.replace(f"_{label}","")}", img_processed)




            



