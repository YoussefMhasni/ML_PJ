import numpy as np
import os
import joblib
def encoder(filename):
  from PIL import Image
  image=Image.open(filename).resize((32,32)).convert('RGB')
  image=np.array(image)
  vect= np.concatenate((image[:,:,0].ravel(), image[:,:,1].ravel(),image[:,:,2].ravel()))
  return vect[None,:]

def model():
  model_path = os.path.join(os.getcwd(), "artifacts", "best_model.pkl")
  print(model_path)
  model = joblib.load(open(model_path, 'rb'))
  return model