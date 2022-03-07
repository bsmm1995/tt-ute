from controller import predict_heart_disease
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "The API is working..."


@app.route('/predict', methods=['POST'])
def predict():
    try:
        response = request.get_json(force=True)
        model = response["model"]
        data = response["data"]
        prediction = predict_heart_disease(model, data)
        result = create_response(False, 200, "Successful prediction", prediction.tolist())
    except FileNotFoundError as e:
        result = create_response(True, 500, str(e), None)
    except ValueError as e:
        result = create_response(True, 500, str(e), None)
    except KeyError as e:
        result = create_response(True, 500, str(e), None)

    return result, 200, {'Content-Type': 'application/json'}


def create_response(error, status, message, auto):
    return {
        'error': error,
        'status': status,
        'message': message,
        'auto': auto
    }


if __name__ == '__main__':
    app.run()
