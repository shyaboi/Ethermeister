from flask import Flask
from flask_cors import CORS
from send import send_eth
app = Flask(__name__)
cors = CORS(app)

@app.route('/send_eth/<string:eth_address>/<string:auth_token>')
def get_eth_auth(eth_address, auth_token):
    print(eth_address, auth_token)
    send_eth(eth_address)
    #TODO check auth token w/strip server for payment confirmation
    return f'Post {eth_address}'