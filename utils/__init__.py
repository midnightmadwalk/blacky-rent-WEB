from flask import Flask
import os

PORT = int(os.environ.get("PORT", 6969))
app = Flask(__name__)

@app.route('/hello')
def index():
    return 'hello'

app.run(host='0.0.0.0', port=PORT)
