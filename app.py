# Backend для Booking.com
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Пример данных об отелях
hotels = [
    {
        'id': 1,
        'name': 'Гранд Отель',
        'city': 'Санкт-Петербург',
        'price': 5000,
        'rating': 4.8,
        'available': True
    },
    {
        'id': 2,
        'name': 'Отель Центральный',
        'city': 'Москва',
        'price': 7000,
        'rating': 4.5,
        'available': True
    }
]

@app.route('/')
def index():
    return jsonify({'message': 'Booking.com API'})

@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    city = request.args.get('city')
    if city:
        filtered = [h for h in hotels if h['city'] == city]
        return jsonify(filtered)
    return jsonify(hotels)

@app.route('/api/hotels/<int:hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotel = next((h for h in hotels if h['id'] == hotel_id), None)
    if hotel:
        return jsonify(hotel)
    return jsonify({'error': 'Hotel not found'}), 404

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    data = request.json
    booking = {
        'hotel_id': data.get('hotel_id'),
        'checkin': data.get('checkin'),
        'checkout': data.get('checkout'),
        'guests': data.get('guests'),
        'created_at': datetime.now().isoformat()
    }
    return jsonify({'message': 'Booking created', 'booking': booking}), 201

if __name__ == '__main__':
    app.run(debug=True)