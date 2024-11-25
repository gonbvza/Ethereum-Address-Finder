from bip32 import BIP32
from mnemonic import Mnemonic
from eth_keys import keys

def findMnemonic(mnemonic_phrase):
    # Create Mnemonic instance and generate seed from the given mnemonic
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic_phrase, passphrase="")  # Empty passphrase
    
    # Initialize BIP32 with the generated seed
    bip32 = BIP32.from_seed(seed)
    
    # Correct Ethereum BIP44 path: "m/44'/60'/0'/0/0"
    path = "m/44'/60'/0'/0/0"
    
    # Derive the private key from the BIP44 path
    xpriv = bip32.get_privkey_from_path(path)
    
    # Create the corresponding Ethereum private key object using eth_keys
    eth_private_key = keys.PrivateKey(xpriv)
    
    # Derive the corresponding public key
    eth_public_key = eth_private_key.public_key
    
    # Return the private and public keys in hex format
    return {
        "private_key": eth_private_key.to_hex(),
        "public_key": eth_public_key.to_hex(),
        "address": eth_public_key.to_address()
    }

