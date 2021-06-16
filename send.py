from web3 import Web3
import os
# from db import update_bal
from dotenv import load_dotenv
load_dotenv()
# import sqlite3

def send_eth(receiver_add):
    # LINK = os.environ.get("LINK")
    GANACHE = os.environ.get("GANACHE")
    TESTSPUBKEY = os.environ.get("TESTSPUBKEY")
    TESTSPRIVKEY = os.environ.get("TESTSPRIVKEY")
    TESTRPUBKEY = os.environ.get("TESTRPUBKEY")

    web3 = Web3(Web3.HTTPProvider(GANACHE))


    print(web3.isConnected())

    sender_add = TESTSPUBKEY
    sender_pk = TESTSPRIVKEY

    receiver_add = receiver_add
    receiver_pk = 'receiver_pk'


    nonce = web3.eth.getTransactionCount(sender_add)

    tx = {
        'nonce':nonce,
        'to': receiver_add,
        'value': web3.toWei(5.22, 'ether'),
        'gas':200000,
        'gasPrice': web3.toWei('1', 'wei')
    }




    signed_tx = web3.eth.account.signTransaction(tx, sender_pk)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(web3.toHex(tx_hash))

    # update_bal(receiver_add)