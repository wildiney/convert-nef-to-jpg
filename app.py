import os
import rawpy
from PIL import Image
from colorama import Fore, Back, Style


def convert_nef_to_jpg(origin, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for current_folder, subfolder, files in os.walk(origin):
        for file in files:
            if file.lower().endswith(".nef"):
                filepath_origin = os.path.join(current_folder, file)
                filepath_destination = os.path.join(
                    destination, os.path.relpath(filepath_origin, origin)
                )

                if (os.path.exists(filepath_destination.replace('.NEF', '.jpg'))):
                    print(Fore.YELLOW+"[WARN] " +
                          filepath_destination, "already exists")
                else:
                    print(Fore.GREEN+"[INFO] " + filepath_destination)
                    try:
                        os.makedirs(os.path.dirname(
                            filepath_destination), exist_ok=True)

                        with rawpy.imread(filepath_origin) as raw:
                            rgb = raw.postprocess(use_camera_wb=True)

                        Image.fromarray(rgb).save(
                            filepath_destination.replace('.NEF', '.jpg'), "JPEG")
                    except:
                        print(Fore.RED+"[ERRO] ", filepath_destination)


if __name__ == "__main__":
    convert_nef_to_jpg('', '')
