from itertools import permutations
from src.seed_generator import findMnemonic  
from src.addressCheck import checkBalance
from web3 import Web3
from colorama import Fore, Back, Style

def compareToAddress(target):
    words = []

    with open('test.txt', 'r') as file:
        for line in file:

            words.append(line.strip())

    all_combinations = permutations(words)

    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/df0e16f9d9944121b4b18431edbb3dac'))

    idx = 0

    for combination in all_combinations:
        mnemonic_phrase = " ".join(combination)
        
        keys_info = findMnemonic(mnemonic_phrase)
        
        priv = keys_info["private_key"]
        public = keys_info["public_key"]
        address = keys_info["address"]

        status = "Not equal"

        target = target.lower()

        if address == target:
            status
            print(f"{Fore.YELLOW} Scan {Fore.WHITE} {idx} | {Fore.GREEN} {' '.join(combination)} {Fore.WHITE} | {Fore.GREEN} {address} {Fore.WHITE} | {Fore.RED} they are {status}")
            break
        else:
            print(f"{Fore.YELLOW} Scan {Fore.WHITE} {idx} | {Fore.GREEN} {' '.join(combination)} {Fore.WHITE} | {Fore.GREEN} {address} {Fore.WHITE} | {Fore.RED} they are {status}")

        idx += 1

if __name__ == "__main__":
    compareToAddress()
