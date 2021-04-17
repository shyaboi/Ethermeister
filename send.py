from web3 import Web3
import os
from dotenv import load_dotenv   
load_dotenv()

LINK = os.environ.get("LINK")
GANACHE = os.environ.get("GANACHE")

web3 = Web3(Web3.HTTPProvider(GANACHE))


print(web3.isConnected())

receiver_add = 'ADDRESS'
receiver_pk = 'PRIVATE_KEYS'

sender_add = 'ADDRESS'
sender_pk = 'PRIVATE_KEYS'

nonce = web3.eth.getTransactionCount(sender_add)

tx = {
    'nonce':nonce,
    'to': receiver_add,
    'value': web3.toWei(13, 'ether'),
    'gas':200000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, sender_pk)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))