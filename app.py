import os
from flask import Flask, jsonify, send_from_directory, render_template
import pandas as pd

app = Flask(__name__)

# Ruta para servir el archivo index.html desde la carpeta static
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Ruta para servir el dashboard.html desde la carpeta templates
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Ruta para obtener datos del archivo CSV como JSON
@app.route('/data')
def get_data():
    try:
        csv_path = os.path.join(os.path.dirname(__file__), 'wifi.csv')
        df = pd.read_csv(csv_path)
        data = df.to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)