from brownie import (
    accounts,
    GuessTheNewNumberChallenge,
    GuessTheNewNumberChallengeAttacker,
)
from web3 import Web3

eth_amount = Web3.toWei("1", "ether")
challenge_address = "0xF13A1c7a3500791B5414271f1A04B6A50991A88E"


def test_guess_new_number():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = GuessTheNewNumberChallenge.at(challenge_address)

    # deploy own hacker contract
    hacker = GuessTheNewNumberChallengeAttacker.deploy(
        challenge_address, {"from": account}
    )

    # call exploit function in hacker contract
    tx = hacker.exploit({"from": account, "value": eth_amount})
    tx.wait(1)

    # confirm challenge is completed
    assert challenge.isComplete()
