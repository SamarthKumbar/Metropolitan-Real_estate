import pickle
import json
import numpy as np

__locations = None
__locations1 = None
__locations2=None
__locations3=None
__data_columns = None
__data_columns1 = None
__data_columns2 = None
__data_columns3 = None
__model = None
__model1 = None
__model2 = None
__model3 = None

def get_estimated_price(location, sqft, bhk, bath):
    
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    else:
        print("Warning: Location not found in the data. Using default features for prediction.")

    return round(__model.predict([x])[0], 2)

def get_estimated_price1(location, total_sqft, bhk,carparking ):
    try:
        loc_index = __data_columns1.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns1))
    x[0] = total_sqft
    x[1] = carparking
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    else:
        print("Warning: Location not found in the data. Using default features for prediction.")

    return round(__model1.predict([x])[0],2)

def get_estimated_price2(INT_SQFT, N_BATHROOM, N_ROOM, location):
    try:
        loc_index = __data_columns2.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns2))
    x[0] = INT_SQFT
    x[1] = N_BATHROOM
    x[2] = N_ROOM
    if loc_index >= 0:
        x[loc_index] = 1

    return __model2.predict([x])[0]

def get_estimated_price3(location, area, num_bedrooms, resale):

    if not isinstance(area, (int, float)):
        raise ValueError("Area must be an integer or float.")

    # Print debug information
    print("Area:", area)

    loc_index = __data_columns3.index(location)

    X = np.zeros(len(__data_columns3))
    X[0] = area
    X[1] = num_bedrooms
    X[2] = resale
    if loc_index >= 0:
        X[loc_index] = 1

    return __model3.predict([X])[0]


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns, __locations, __data_columns1, __locations1,__data_columns2,__locations2,__data_columns3,__locations3, __model, __model1,__model2,__model3

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    
    with open("./artifacts/columns1.json", "r") as f:
        __data_columns1 = json.load(f)['data_columns']
        __locations1 = __data_columns1[3:]

    with open("./artifacts/columns2.json", "r") as f:
        __data_columns2 = json.load(f)['data_columns']
        __locations2 = __data_columns2[3:]  # first 3 columns are sqft, bath, bhk
    
    with open("./artifacts/columnsss.json", "r") as f:
        __data_columns3 = json.load(f)['data_columns']
        __locations3 = __data_columns3[3:]

    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)

    if __model1 is None:
        with open('./artifacts/mumbai_home_prices_model.pickle', 'rb') as f:  # Change the file path to your second pickle file
            __model1 = pickle.load(f)
    
    if __model2 is None:
        with open('./artifacts/chennai_home_prices_model.pickle', 'rb') as f:  # Change the file path to your second pickle file
            __model2 = pickle.load(f)
    
    if __model3 is None:
        with open('./artifacts/Delhi_home_prices_model.pickle', 'rb') as f:  # Change the file path to your second pickle file
            __model3 = pickle.load(f)

    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_location_names1():
    return __locations1

def get_location_names2():
    return __locations2

def get_location_names3():
    return __locations3
    
def get_data_columns():
    return __data_columns

def get_data_columns1():
    return __data_columns1

def get_data_columns1():
    return __data_columns2

def get_data_columns1():
    return __data_columns3

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_location_names1())
    print(get_location_names2())
    print(get_location_names3())
    print(get_estimated_price3('59 Sector 22 Road',2000, 2, 0))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price2(2000, 2, 2,'adyar'))   # other location
