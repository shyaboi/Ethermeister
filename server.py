from flask import Flask
from flask_cors import CORS
from send import send_eth
app = Flask(__name__)
cors = CORS(app)

@app.route('/send_eth/<string:eth_address>/<string:auth_token>')
#TODO check auth token on stripe API to confirm payment, and check if funds have already been sent
def get_eth_auth(eth_address, auth_token):
    print(eth_address, auth_token)
    
    #TODO check auth token w/strip server for payment confirmation
    return send_eth(eth_address)