from brownie import accounts, PublicKeyChallenge

challenge_address = "0xE37825FEc41975b8A9FF49012F02BB2f1B52D993"


def test_public_key():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = PublicKeyChallenge.at(challenge_address)

    # perform exploit
    print(challenge.isComplete())

    # confirm that the challenge is completed
    assert challenge.isComplete()
