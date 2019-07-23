import pickle

# loading models only once on startup
model = pickle.load(open('models/rf.model', 'rb'))

# speed_std_scale = pickle.load(open('models/speed_std_scale.model', 'rb'))
# age_std_scale = pickle.load(open('models/age_std_scale.model', 'rb'))
# miles_std_scale = pickle.load(open('models/miles_std_scale.model', 'rb'))

def predict(speed, age, miles):
#     sample = [[speed_std_scale.transform([speed])[0],
#                age_std_scale.transform([age])[0],
#                miles_std_scale.transform([miles])[0]]]
    sample = [[speed, age, miles]]

    result = int(model.predict(sample)[0])
    prediction = model.predict_proba(sample)[0].tolist()
    
    return result, prediction