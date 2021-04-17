from db import add_new_wallet
from web3 import Web3
import web3
from dotenv import load_dotenv   
import os
load_dotenv()

LINK = os.environ.get("LINK")
GANACHE = os.environ.get("GANACHE")

w3 = Web3(Web3.HTTPProvider(GANACHE))

print(w3.isConnected())

add = 'address'

w3.isAddress(add)

wei_bal = w3.eth.getBalance(add)

print(wei_bal)

w3.eth.default_account = add

eth_bal = w3.fromWei(wei_bal, 'ether')

nonce = w3.eth.getTransactionCount(add)

print(eth_bal)
print(nonce)