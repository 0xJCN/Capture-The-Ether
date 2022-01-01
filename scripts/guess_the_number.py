from brownie import accounts, GuessTheNumberChallenge, Contract
from web3 import Web3


def guess_number():
    account = accounts.load("Ropsten_test_net_account")
    contract = Contract.from_abi(
        "GuessTheNumberChallenge",
        "0x0E2065e6dA9Cf78117fF580441546c09ca28a9F0",
        GuessTheNumberChallenge.abi,
    )
    value = Web3.toWei("1", "ether")
    transaction2 = contract.guess(42, {"from": account, "value": value})
    transaction2.wait(1)
    contract.isComplete()


def main():
    guess_number()
