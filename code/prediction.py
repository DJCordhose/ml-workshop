import pickle

# loading models only once on startup
model = pickle.load(open('models/dt.model', 'rb'))

y_le = pickle.load(open('models/y_le.model', 'rb'))
speed_std_scale = pickle.load(open('models/speed_std_scale.model', 'rb'))
age_std_scale = pickle.load(open('models/age_std_scale.model', 'rb'))
miles_std_scale = pickle.load(open('models/miles_std_scale.model', 'rb'))

def predict(speed, age, miles):
    sample = [[speed_std_scale.transform([speed])[0],
               age_std_scale.transform([age])[0],
               miles_std_scale.transform([miles])[0]]]

    result = model.predict(sample)
    result_group = y_le.inverse_transform(result)[0]
    prediction = model.predict_proba(sample)[0].tolist()
    
    return result_group, prediction, y_le.classes_.tolist()