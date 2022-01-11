from brownie import accounts, FuzzyIdentityChallenge, Name

challenge_address = "0x9103e12717de97B7Bdf142ec0804BaA061a690AF"


def test_fuzzy_identity():
    # load accounts
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = FuzzyIdentityChallenge.at(challenge_address)

    # deploy hacker contract
    hacker = Name.deploy({"from": account})
    # perform exploit
    # create a custom smart contract with name() function
    #

    # confirm that the challenge is completed
    assert challenge.isComplete()
