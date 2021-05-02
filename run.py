from flask import Flask,request
import prediction

app = Flask(__name__)

@app.route('/predict',methods = ['POST'])
def predict():
    #print("Welcome")
    data = request.form
    output = prediction.Predict_Output(data)
    return output

if __name__ =="__main__":
    app.run(debug=True,port=7001)