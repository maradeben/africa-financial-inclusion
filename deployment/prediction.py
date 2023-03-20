from utils import wrangle
import pickle
import wget

# load model
path_to_model = '../models/final_model.pkl'


try:
    with open(path_to_model, 'rb') as file:
        model = pickle.load(file)
except:
    url = 'https://github.com/maradeben/africa-financial-inclusion/raw/master/models/inclusion_model2.pkl'
    file = wget.download(url = url)
    with open(file, 'rb') as mod:
        model = pickle.load(mod)

    

def predict(data):
    """Make predictions"""
    processed = wrangle(data, test=True)
    result = model.predict(processed)
    output = ''
    if result == 0:
        output = "Not Likely To Have Bank Account"
    else:
        output = "Likely To Have a Bank Account"
    return output
