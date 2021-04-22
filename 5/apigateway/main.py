from flask import Flask, request, jsonify, make_response
import requests
from circuitbreaker import circuit

app = Flask(__name__)
auth_endpoint = 'http://localhost:5001/auth/get-user'

endpoints = {
    'api/show-profile': 'http://localhost:5002/user/show-profile',
    'api/edit-profile': 'http://localhost:5002/user/edit-profile',
    'api/sign-up': 'http://localhost:5001/auth/sign-up',
    'api/sign-in': 'http://localhost:5001/auth/sign-in'
}


@circuit
def send_request(endpoint, headers):
    req = requests.get if request.method == 'GET' else requests.post
    respon = req(endpoint, headers=headers, json=request.json, timeout=0.5)
    if respon.status_code >= 500:
        raise Exception('Internal Server Error')
    return respon


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def gateway_func(path):
    endpoint = endpoints.get(path)
    if endpoint is None:
        return jsonify({'error': 'Requested page not found.'}), 404
    resp = requests.get(auth_endpoint, headers=request.headers)
    headers = {}
    for k, v in request.headers:
        headers[k] = v
    if resp.status_code == 200:
        headers['User'] = resp.json().get('username')
        headers['UserType'] = resp.json().get('type')

    try:
        response = send_request(endpoint, headers)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    if response.status_code not in [200, 201]:
        return jsonify({'error': response.reason}), response.status_code
    res = make_response(jsonify(response.json()))
    res.headers['Authorization'] = response.headers.get('Authorization')
    return res, res.status_code


if __name__ == '__main__':
    app.run(port=5000)
