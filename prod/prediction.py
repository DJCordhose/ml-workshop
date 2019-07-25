import pickle

# loading models only once on startup
model = pickle.load(open('models/model.pickle', 'rb'))

def predict(speed, age, miles):
    sample = [[speed, age, miles]]

    result = int(model.predict(sample)[0])
    prediction = model.predict_proba(sample)[0].tolist()
    
    return result, prediction