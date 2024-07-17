from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
data = pd.read_csv('cleaned_car.csv')

model = pickle.load(open('LinearRegression.pkl','rb'))
@app.route('/')

def index():
    companies = sorted(data['company'].unique()) 
    car_models = sorted(data['name'].unique())
    year = sorted(data['year'].unique(), reverse=True)
    fuel_type = sorted(data['fuel_type'].unique())

    return render_template('index.html', companies=companies, car_models=car_models, years= year,fuel_type=fuel_type)

@app.route('/predict', methods = ['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilometers'))
    print(company, car_model, year, fuel_type, kms_driven)

prediction = model.predict(pd.DataFrame([['car_model', 'company', 'year', 'fuel_type', 'kms_driven']]))
if __name__ == "__main__":
    app.run(debug=True)