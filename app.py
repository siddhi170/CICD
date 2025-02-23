from flask import Flask
s
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins CI/CD Pipeline - Updated!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
