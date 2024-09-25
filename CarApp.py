import streamlit as st
import pickle
import pandas as pd

# Modeli yükle
with open(r'C:\ml-models\LinearRegressionModel.pkl', 'rb') as file:
    model = pickle.load(file)

# Uygulama başlığı
st.title("Car Price Predictor")

# Kullanıcıdan girdi alın
company = st.selectbox("Select Company", options=["Select Company", 'Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 
                                                  'Audi', 'Toyota', 'Renault', 'Honda', 'Datsun', 'Mitsubishi', 
                                                  'Tata', 'Volkswagen', 'Chevrolet', 'Mini', 'BMW', 'Nissan', 
                                                  'Hindustan', 'Fiat', 'Force', 'Mercedes', 'Land', 'Jaguar', 
                                                  'Jeep', 'Volvo'], key="company_select")

car_models = {
    'Hyundai': ['Hyundai Santro Xing', 'Hyundai Grand i10', 'Hyundai Eon', 'Hyundai Elite i20', 
                'Hyundai i20 Sportz', 'Hyundai i20 Magna', 'Hyundai i20 Asta', 
                'Hyundai Verna Transform', 'Hyundai Verna Fluidic', 'Hyundai Elantra SX', 
                'Hyundai Creta 1.6', 'Hyundai i10 Magna', 'Hyundai Accent GLX', 
                'Hyundai Santro', 'Hyundai Getz GLE', 'Hyundai Sonata Transform', 
                'Hyundai Xcent Base', 'Hyundai Accent Executive', 'Hyundai i10 Era'],
    
    'Mahindra': ['Mahindra Jeep CL550', 'Mahindra Scorpio SLE', 'Mahindra Bolero DI', 
                 'Mahindra Scorpio S10', 'Mahindra Scorpio S4', 'Mahindra Scorpio VLX', 
                 'Mahindra Quanto C8', 'Mahindra XUV500 W8', 'Mahindra Thar CRDe', 
                 'Mahindra KUV100 K8', 'Mahindra Xylo E4', 'Mahindra XUV500 W10', 
                 'Mahindra TUV300 T4', 'Mahindra TUV300 T8', 'Mahindra Xylo D2'],
    
    'Ford': ['Ford EcoSport Titanium', 'Ford Figo', 'Ford EcoSport Ambiente', 
             'Ford Fiesta SXi', 'Ford Ikon 1.6', 'Ford Ikon 1.3', 
             'Ford Fusion 1.4', 'Ford Endeavor 4x4', 'Ford EcoSport Trend'],
    
    'Maruti': ['Maruti Suzuki Alto', 'Maruti Suzuki Stingray', 'Maruti Suzuki Swift', 
               'Maruti Suzuki Dzire', 'Maruti Suzuki Wagon', 'Maruti Suzuki Vitara', 
               'Maruti Suzuki Baleno', 'Maruti Suzuki Ertiga', 'Maruti Suzuki Ciaz', 
               'Maruti Suzuki 800', 'Maruti Suzuki Zen', 'Maruti Suzuki Omni', 
               'Maruti Suzuki S', 'Maruti Suzuki Estilo', 'Maruti Suzuki Eeco'],
    
    'Skoda': ['Skoda Octavia', 'Skoda Superb', 'Skoda Rapid', 
              'Skoda Fabia', 'Skoda Fabia Classic', 'Skoda Yeti Ambition', 
              'Skoda Laura', 'Skoda Rapid Elegance', 'Skoda Octavia Classic'],
    
    'Audi': ['Audi A4', 'Audi Q5', 'Audi A6 2.0', 'Audi A3 Cabriolet', 
             'Audi A8', 'Audi Q3 2.0', 'Audi A4 1.8'],
    
    'Toyota': ['Toyota Corolla', 'Toyota Camry', 'Toyota Innova', 
               'Toyota Fortuner', 'Toyota Etios GD', 'Toyota Etios Liva', 
               'Toyota Qualis', 'Toyota Corolla Altis', 'Toyota Fortuner 3.0'],
    
    'Renault': ['Renault Kwid', 'Renault Duster', 'Renault Lodgy', 
                'Renault Duster 85', 'Renault Scala RxL', 'Renault Duster 110', 
                'Renault Kwid 1.0', 'Renault Duster 110PS'],
    
    'Honda': ['Honda City', 'Honda Amaze', 'Honda Accord', 
              'Honda City ZX', 'Honda Brio', 'Honda Jazz S', 
              'Honda Mobilio', 'Honda WR V'],
    
    'Datsun': ['Datsun Go', 'Datsun Redi-Go', 'Datsun Go Plus', 
               'Datsun GO T'],
    
    'Mitsubishi': ['Mitsubishi Pajero', 'Mitsubishi Outlander', 
                   'Mitsubishi Lancer 1.8', 'Mitsubishi Pajero Sport'],
    
    'Tata': ['Tata Nexon', 'Tata Tiago', 'Tata Harrier', 
             'Tata Indigo eCS', 'Tata Indica V2', 'Tata Nano Cx', 
             'Tata Sumo Victa', 'Tata Manza Aura', 'Tata Zest XE', 
             'Tata Vista Quadrajet', 'Tata Bolt XM'],
    
    'Volkswagen': ['Volkswagen Polo', 'Volkswagen Vento', 'Volkswagen Passat Diesel', 
                   'Volkswagen Jetta Highline', 'Volkswagen Jetta Comfortline', 
                   'Volkswagen Polo Comfortline', 'Volkswagen Polo Trendline', 
                   'Volkswagen Vento Highline', 'Volkswagen Polo Highline'],
    
    'Chevrolet': ['Chevrolet Beat', 'Chevrolet Tavera', 'Chevrolet Spark', 
                  'Chevrolet Spark LS', 'Chevrolet Spark LT', 
                  'Chevrolet Beat Diesel', 'Chevrolet Enjoy'],
    
    'Mini': ['Mini Cooper', 'Mini Countryman'],
    
    'BMW': ['BMW 3 Series', 'BMW 5 Series', 'BMW 7 Series', 
            'BMW X1', 'BMW X1 sDrive20d', 'BMW X1 xDrive20d', 
            'BMW X5'],
    
    'Nissan': ['Nissan Micra', 'Nissan Sunny', 'Nissan Terrano XL', 
               'Nissan X Trail'],
    
    'Hindustan': ['Hindustan Ambassador'],
    
    'Fiat': ['Fiat Punto', 'Fiat Linea'],
    
    'Force': ['Force Gurkha', 'Force Motors One'],
    
    'Mercedes': ['Mercedes-Benz C-Class', 'Mercedes-Benz E-Class', 
                 'Mercedes Benz GLA', 'Mercedes Benz A', 
                 'Mercedes Benz B'],
    
    'Land': ['Land Rover Defender', 'Land Rover Discovery', 'Land Rover Freelander'],
    
    'Jaguar': ['Jaguar XE', 'Jaguar XF', 'Jaguar F-PACE'],
    
    'Jeep': ['Jeep Compass', 'Jeep Wrangler', 'Jeep Wrangler Unlimited'],
    
    'Volvo': ['Volvo XC90', 'Volvo S60', 'Volvo S80 Summum'],
}

# Şirket seçimine bağlı olarak araç modelini filtrele
if company != "Select Company":
    car_model_options = car_models[company]
else:
    car_model_options = ["Select Model"]

car_model = st.selectbox("Select Model", options=car_model_options, key="car_model_select")

year = st.selectbox("Select Year of Purchase", options=list(range(2000, 2023)), key="year_select")
fuel_type = st.selectbox("Select Fuel Type", options=["Petrol", "Diesel", "LPG"], key="fuel_type_select")
kms_driven = st.number_input("Enter the Number of Kilometres Driven", min_value=0, max_value=1000000)

# Tahmin için buton
if st.button("Predict Price"):
    # Girdi verilerini bir DataFrame olarak hazırlayın
    input_data = pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]], 
                               columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    
    # Tahmin yapın
    prediction = model.predict(input_data)
    
    # Tahmini göster
    if prediction[0] < 0:
        st.warning("Bu özelliklere sahip bir araba bulunmamaktadır.")
    else:
        st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")
