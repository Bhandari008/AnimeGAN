import onnxruntime as ort
import time, cv2, PIL
import numpy as np
from PIL import Image
import random

def set_providers():
    device_name = ort.get_device()
    if device_name == 'cpu':
        providers = ['CPUExecutionProvider']
    elif device_name == 'GPU':
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
    
    return providers


def Convert(img, scale, session):
    x = session.get_inputs()[0].name
    y = session.get_outputs()[0].name
    fake_img = session.run(None, {x : img})[0]
    images = (np.squeeze(fake_img) + 1.) / 2 * 255
    images = np.clip(images, 0, 255).astype(np.uint8)
    output_image = cv2.resize(images, (scale[1],scale[0]))
    return cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)

def process_img(img, x32=True):
    h, w = img.shape[:2]
    if x32: 
        def to_32s(x):
            return 256 if x < 256 else x - x%32
            img = cv2.resize(img, (to_32s(w), to_32s(h)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32) / 127.5 - 1.0
    return img

def load_test_data(image_path):
    img0 = cv2.imread(image_path).astype(np.float32)
    img = process_img(img0)
    img = np.expand_dims(img, axis=0)
    return img, img0.shape[:2]


def translate_image(image_path, model_name):
    number = random.randint(1,1000)
    providers = set_providers()
    session =  ort.InferenceSession(f'models/{model_name}.onnx', providers = providers)
    mat, scale = load_test_data(image_path)
    res = Convert(mat, scale, session)

    output_file = f"static/images/changed/{number}_styled_{model_name}.jpg"
    cv2.imwrite(output_file, res)

    return output_file
