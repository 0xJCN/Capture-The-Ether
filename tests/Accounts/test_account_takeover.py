from brownie import accounts, AccountTakeoverChallenge

challenge_address = "0xB1aA135d869D1b4dB5a8d67B7A79820E5a5c0073"


def test_token_bank():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = AccountTakeoverChallenge.at(challenge_address)

    # perform exploit

    # confirm that the challenge is completed
    assert challenge.isComplete()
