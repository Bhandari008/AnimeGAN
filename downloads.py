import os
import wget

# create the directory if it doesn't exist
if not os.path.exists("models"):
    os.makedirs("models")

# URLs and filenames of the files to be downloaded
urls_and_filenames = {
    "https://docs.google.com/uc?export=download&id=1VPAPI84qaPUCHKHJLHiMK7BP_JE66xNe": "AnimeGAN_Hayao.onnx",
    "https://docs.google.com/uc?export=download&id=17XRNQgQoUAnu6SM5VgBuhqSBO4UAVNI1": "AnimeGANv2_Hayao.onnx",
    "https://docs.google.com/uc?export=download&id=10rQfe4obW0dkNtsQuWg-szC4diBzYFXK": "AnimeGANv2_Shinkai.onnx",
    "https://docs.google.com/uc?export=download&id=1X3Glf69Ter_n2Tj6p81VpGKx7U4Dq-tI": "AnimeGANv2_Paprika.onnx"
}

# download each file and save it to the models directory
for url, filename in urls_and_filenames.items():
    print(f'Downloading {filename}')
    filepath = os.path.join("models", filename)
    wget.download(url, filepath)

print("All files downloaded and saved to the 'models' directory.")
