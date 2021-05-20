from flask import Flask, json, jsonify, request

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

# TEST
@app.route('/', methods=['GET'])
def test():
    return jsonify({
        "status": 1,
        "message": 'Test completed successfully!',
        "data": ''
    })


if __name__ == '__main__':
    # Change this before deploying
    # app.run(debug=True)
    app.run()
