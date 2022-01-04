from brownie import accounts, GuessTheNumberChallenge
from web3 import Web3

eth_amount = Web3.toWei("1", "ether")
challenge_address = "0x0E2065e6dA9Cf78117fF580441546c09ca28a9F0"


def test_guess_the_number():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = GuessTheNumberChallenge.at(challenge_address)

    # call guess with 42 as an argument
    tx = challenge.guess(42, {"from": account, "value": eth_amount})
    tx.wait(1)

    # assert isComplete is true
    assert challenge.isComplete()
