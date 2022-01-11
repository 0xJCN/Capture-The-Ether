from brownie import accounts, CallMeChallenge

challenge_address = "0xeFaD3a832C3bF8E42d67a35E7E803DF288333A8A"


def test_call_me():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = CallMeChallenge.at(challenge_address)

    # call callme()
    tx = challenge.callme({"from": account})
    tx.wait(1)

    # confirm the challenge is completed
    assert challenge.isComplete()
