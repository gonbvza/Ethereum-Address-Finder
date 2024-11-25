from eth_keys import keys
from web3 import Web3

def checkBalance(eth_address, w3):

    eth_address_str = str(eth_address).lower()

    eth_address_checksum = Web3.to_checksum_address(eth_address_str)

    balance = w3.eth.get_balance(eth_address_checksum)

    balance_in_ether = w3.from_wei(balance, 'ether')

    return {
        "balance": balance_in_ether
    }
