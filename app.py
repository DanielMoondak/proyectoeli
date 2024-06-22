import os
from flask import Flask, jsonify, send_from_directory, render_template

app = Flask(__name__)

# Ruta para servir el archivo index.html desde la raíz del proyecto
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Ruta para servir archivos estáticos (CSS, JS, imágenes, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

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
