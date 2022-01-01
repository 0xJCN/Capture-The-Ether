from brownie import accounts, Contract, exceptions, GuessTheNumberChallenge
from web3 import Web3
import pytest

# need 1 ether to interact with contract and call guess function
AMOUNT_OF_ETHER_REQUIRED = Web3.toWei("1", "ether")


def test_guess_the_number():
    # set up account and contract
    account = accounts.load("Ropsten_test_net_account")
    guess_the_number_contract = Contract.from_abi(
        "GuessTheNumberChallenge",
        "0x0E2065e6dA9Cf78117fF580441546c09ca28a9F0",
        GuessTheNumberChallenge.abi,
    )
    # run exploit
    exploit = guess_the_number_contract.guess(
        42, {"from": account, "value": AMOUNT_OF_ETHER_REQUIRED}
    )
    exploit.wait(1)
    print(exploit.info())
    # assert isComplete is true
    assert guess_the_number_contract.isComplete()
