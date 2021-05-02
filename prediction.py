import pickle

model = pickle.load(open('D:\E Drive\Data\my Own Notes\Flask\Linear_Advert\linear_model.pickle','rb'))

def Predict_Output(data):
    TV = int(data['TV'])
    radio = int(data['radio'])
    newspaper = int(data['newspaper'])
    predict = str((model.predict([[TV,radio,newspaper]]))[0])
    return predict

