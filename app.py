from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    print(f"Request from: {request.remote_addr}")
    return "Hello from Flask integrated with AWS!"

if __name__ == "__main__":
    app.run(debug=True)







