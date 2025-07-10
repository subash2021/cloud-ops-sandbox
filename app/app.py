from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

# Creat the flask app
app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route('/')
def main():
    return "Hello, Cloud Ops Engineer! The website in running."

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)