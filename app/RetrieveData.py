import requests
import os
import pandas as pd
from sklearn.utils import shuffle

scale = 0.2
height = 40
width = 40

#Load the imported data
for object in ["estrellas","galaxias"]:

    data_dir= 'dataset/imagenes'
    data_dir_label = data_dir + "/" + object
    file_names = list(map(lambda x: x.split("_")[0], sorted(os.listdir(data_dir_label))))

    file_name = f"{object}_10000_extended.csv"

    df = pd.read_csv(f"dataset/fotometria/raw/{file_name}", index_col=False, skiprows=1)

    df["id"] = range(1,len(df)+1)
    df["label"] = df.apply(lambda x: "0" if object == "estrellas" else "1", axis=1)

    df.to_csv(f"dataset/fotometria/conformed/{file_name}",index=False)
    
    for index,row in df.iterrows():
        
        if not row.empty:

            id,ra,dec = int(row["id"]),round(row["ra"],5),round(row["dec"],5)

            if str(id) not in file_names:

                # URL de la API
                url = f"http://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?ra={ra}&dec={dec}&scale={scale}&height={height}&width={width}"

                # Hacer la solicitud POST
                response = requests.get(url)

                # Verificar que la solicitud fue exitosa
                if response.status_code == 200:

                    # Crear una carpeta para guardar las imágenes
                    os.makedirs(f"dataset/imagenes/{object.lower()}", exist_ok=True)

                    img_name = f"{id}_{object}.jpg"
                    
                    # Descargar la imagen
                    img_data = response.content
                    img_path = os.path.join(f"dataset/imagenes/{object}", img_name)

                    with open(img_path, "wb") as img_file:
                        img_file.write(img_data)
                    
                    print(f"Imagen descargada: {img_name}")

                else:
                    print(f"Error en la solicitud: {response.status_code}")
                    print(response.text)
