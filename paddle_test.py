from PIL import Image
import numpy as np
import os

def load_image(file):
    im = Image.open(file).convert('L')
    im = im.resize((28, 28), Image.ANTIALIAS)
    im = np.array(im).astype(np.float32).flatten()
    im = im / 255.0
    return im

test_data = []
cur_dir = os.getcwd()
test_data.append((load_image(cur_dir + '/image/infer_3.png'),))

probs = paddle.infer(output_layer=predict, parameters=parameters, input=test_data)
lab = np.argsort(-probs)
print "Lable of image/infer_3.png is: %d" % lab[0][0]


