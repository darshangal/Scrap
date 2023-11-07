from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_ipo_data', methods=['GET'])
def get_ipo_data():
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, type, GMP, Price, Gain, Duration FROM IpoData')
        data = cursor.fetchall()
        conn.close()

        ipo_data = []
        for row in data:
            ipo_data.append({
                'id': row[0],
                'name': row[1],
                'type': row[2],
                'GMP': row[3],
                'Price': row[4],
                'Gain': row[5],
                'Duration': row[6]
            })

        return jsonify({'ipo_data': ipo_data})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
