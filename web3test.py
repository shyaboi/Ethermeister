from web3 import Web3
import web3
from dotenv import load_dotenv   
import os
load_dotenv()
LINK = os.environ.get("LINK")

w3 = Web3(Web3.HTTPProvider(LINK))

print(w3.isConnected())

add = w3.eth.account.create('New Ethereum wallet added!')

pk = add._private_key

print(add._private_key.hex)

w3.isAddress(add)

wei_bal = w3.eth.getBalance(add._address)

print(wei_bal)

w3.eth.default_account = add

eth_bal = w3.fromWei(wei_bal, 'ether')

nonce = w3.eth.getTransactionCount(add._address)

print(eth_bal)

print(w3.eth.default_account._address)

print(add._private_key.hex)