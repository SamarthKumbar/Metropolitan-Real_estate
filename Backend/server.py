from flask import Flask, request, jsonify
from flask_cors import CORS
import util
from pymongo import MongoClient

app = Flask(__name__)
CORS(app) 

client = MongoClient('mongodb+srv://samarth:sam45@cluster1.vocac4v.mongodb.net/')
db = client['ML']
collection = db['Blore']
collection1=db['Mumbai']
collection2=db['Chennai']
collection3=db['Delhi']

if client:
    print("Connected to MongoDB successfully")
else:
    print("Failed to connect to MongoDB")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response

@app.route('/get_location_names1', methods=['GET'])
def get_location_names1():
    response = jsonify({
        'locations': util.get_location_names1()
    })
    return response

@app.route('/get_location_names2', methods=['GET'])
def get_location_names2():
    response = jsonify({
        'locations': util.get_location_names2()
    })
    return response

@app.route('/get_location_names3', methods=['GET'])
def get_location_names3():
    response = jsonify({
        'locations': util.get_location_names3()
    })
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
    except KeyError as e:
        return jsonify({'error': 'Missing parameter: {}'.format(str(e))}), 400
    except ValueError as e:
        return jsonify({'error': 'Invalid value: {}'.format(str(e))}), 400
    
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    estimated_price = round(estimated_price / 100, 6)

    prediction_data = {
        'total_sqft': total_sqft,
        'location': location,
        'bhk': bhk,
        'bath': bath,
        'estimated_price': estimated_price
    }
    collection.insert_one(prediction_data)

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    return response

@app.route('/predict_home_price1', methods=['POST'])
def predict_home_price1():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        carparking = int(request.form['carparking'])
    except KeyError as e:
        return jsonify({'error': 'Missing parameter: {}'.format(str(e))}), 400
    except ValueError as e:
        return jsonify({'error': 'Invalid value: {}'.format(str(e))}), 400
    
    estimated_price = util.get_estimated_price1(location, total_sqft, bhk, carparking)  # Calculate estimated price
    new_estimated_price=round(estimated_price/100,6)
    prediction_data1 = {
        'total_sqft': total_sqft,
        'location': location,
        'bhk': bhk,
        'carparking': carparking,
        'estimated_price1': new_estimated_price
    }
    collection1.insert_one(prediction_data1)

    response = jsonify({
        'estimated_price': util.get_estimated_price1(location, total_sqft, bhk, carparking)
    })
    return response

@app.route('/predict_home_price2',methods=['POST'])
def predict_home_price2():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bathroom = int(request.form['bath'])
    estimated_price = util.get_estimated_price2(sqft,bathroom,bhk,location)  # Calculate estimated price
    new_estimated_price=round(estimated_price/100,6)

    prediction_data1 = {
        'sqft': sqft,
        'location': location,
        'bhk': bhk,
        'bathroom':bathroom,
        'estimated_price1': new_estimated_price
    }
    collection2.insert_one(prediction_data1)

    response = jsonify({
        'estimated_price': util.get_estimated_price2(sqft,bathroom,bhk,location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price3', methods=['POST'])
def predict_home_price3():
    area = float(request.form['area'])
    location = request.form['location']
    num_bedrooms= int(request.form['num_bedrooms'])
    resale= int(request.form['resale'])
    estimated_price = util.get_estimated_price3(location, area, num_bedrooms, resale)
    new_estimated_price=round(estimated_price/100,6)

    prediction_data1 = {
        'area': area,
        'location': location,
        'num_bedrooms': num_bedrooms,
        'resale':resale,
        'estimated_price1': new_estimated_price
    }
    collection3.insert_one(prediction_data1)

    response = jsonify({
        'estimated_price': util.get_estimated_price3(location, area, num_bedrooms, resale)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
