# Mnemonic Phrase Scanner

This Python project scans Ethereum wallet addresses generated from permutations of a given set of words (mnemonic phrases) to identify wallets with non-zero balances.

## Features

- **Generate Ethereum Wallet Keys**: Derives private keys, public keys, and addresses from mnemonic phrases.
- **Check Ethereum Balances**: Connects to the Ethereum blockchain to check wallet balances.
- **Custom Word Lists**: Permutations of a word list can be supplied via a `test.txt` file.

## Requirements

- Python 3.7+
- Internet connection (to connect to the Ethereum mainnet)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment

   ```python -m venv venv
    source venv/bin/activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Set up an Infura project and replace the placeholder URL in the script with your Infura endpoint

## Usage
