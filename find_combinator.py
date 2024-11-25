from itertools import permutations
from src.seed_generator import findMnemonic  
from src.addressCheck import checkBalance
from web3 import Web3
from colorama import Fore, Back, Style

words = []

with open('test.txt', 'r') as file:
    for line in file:

        words.append(line.strip())

# Generate all permutations of the words (be careful with large lists of words)
# Note: permutations(words) generates all permutations, but for larger lists,
# this will generate a huge number of combinations!
all_combinations = permutations(words)

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/df0e16f9d9944121b4b18431edbb3dac'))

idx = 0

for combination in all_combinations:
    mnemonic_phrase = " ".join(combination)
    
    keys_info = findMnemonic(mnemonic_phrase)
    
    priv = keys_info["private_key"]
    public = keys_info["public_key"]
    address = keys_info["address"]

    address_info = checkBalance(address, w3)

    balance = address_info["balance"]

    print(f"{Fore.YELLOW} Scan {Fore.WHITE} {idx} | {Fore.GREEN} {' '.join(combination)} {Fore.WHITE} | {Fore.GREEN} {priv[2:]} {Fore.WHITE} | {Fore.RED} {address} has {Fore.WHITE} {balance} {Fore.RED} ether")

    if balance > 0 :
        break

    idx += 1
