from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from bs4 import BeautifulSoup
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite') # Will use DATABASE_URL if it exists, otherwise use sqlite for local development.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BeachData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    beach_name = db.Column(db.String(100))
    data = db.Column(db.JSON)  # Here we'll store our record data for each beach

    def set_data(self, data):
        self.data = json.dumps(data)  # Convert data to JSON string

    def get_data(self):
        return json.loads(self.data)  # Convert JSON string to Python object




def scrape_beach_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    number_element_raw = soup.find('span', class_='water-cce').text
    number_element = number_element_raw[5:]



    if number_element is None:
        return None

    return float(number_element)

def get_data():
    endpoint = "https://data.cityofchicago.org/resource/xvsz-3xcj.json"

    response = requests.get(endpoint)
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        return {}

    data = json.loads(response.text)

    beach_urls =  { '57th Street':"https://www.chicagoparkdistrict.com/parks-facilities/57th-street-beach", 
                    'Oakwood':"https://www.chicagoparkdistrict.com/parks-facilities/oakwood-beach", 
                    'Margaret T Burroughs (31st)':"https://www.chicagoparkdistrict.com/parks-facilities/margaret-t-burroughs-beach", '12th Street':"https://www.chicagoparkdistrict.com/parks-facilities/12th-street-beach", 
                    'Ohio Street':"https://www.chicagoparkdistrict.com/parks-facilities/ohio-street-beach", 'Oak Street':"https://www.chicagoparkdistrict.com/parks-facilities/oak-street-beach", 'North Avenue':"https://www.chicagoparkdistrict.com/parks-facilities/north-avenue-beach", 'Foster':"https://www.chicagoparkdistrict.com/parks-facilities/foster-beach", 'Osterman':"https://www.chicagoparkdistrict.com/parks-facilities/osterman-beach", 
                    'Hartigan (Albion)':"https://www.chicagoparkdistrict.com/parks-facilities/hartigan-beach", 'Leone':"https://www.chicagoparkdistrict.com/parks-facilities/leone-beach", 'Marion Mahony Griffin (Jarvis)':"https://www.chicagoparkdistrict.com/parks-facilities/marion-mahony-griffin-beach"}

    for record in data:
        beach_name = record.get('beach_name', '')
        if beach_name in beach_urls:
            record['scraped_number'] = scrape_beach_data(beach_urls[beach_name])
            
            # Check if a record for this beach already exists
            beach_record = BeachData.query.filter_by(beach_name=beach_name).first()

        if beach_record:
            # Update existing record
            beach_record.set_data(record)
        else:
            # Create new record
            beach_record = BeachData(beach_name=beach_name)
            beach_record.set_data(record)
            db.session.add(beach_record)
        


    return {record.get('beach_name', ''): record for record in data}


def order_data(data):
    beach_order = ['57th Street', 'Oakwood', 'Margaret T Burroughs (31st)', '12th Street', 
                   'Ohio Street', 'Oak Street', 'North Avenue', 'Foster', 'Osterman', 
                   'Hartigan (Albion)', 'Leone', 'Marion Mahony Griffin (Jarvis)', 'Howard', 
                   'Rogers', 'Juneway']

    beach_positions = {beach: position for position, beach in enumerate(beach_order)}

    # Convert the dictionary values to a list and sort
    return sorted(data.values(), key=lambda record: beach_positions.get(record['beach_name'], float('inf')))

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    # Pull all the data from the database
    beach_records = BeachData.query.all()
    data = {beach.beach_name: beach.data for beach in beach_records}
    ordered_data = order_data(data)
    return render_template('index.html', data=ordered_data)

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8009)