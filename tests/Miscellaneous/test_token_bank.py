from brownie import accounts, TokenBankChallenge

challenge_address = "0x848c54016819585D635e7A3d13b916c04F926729"


def test_token_bank():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = TokenBankChallenge.at(challenge_address)

    # perform exploit
    # put tokenFallback function in hacker contract
    # send all tokens to hacker contract
    # deploy hacker contract

    # confirm that the challenge is completed
    assert challenge.isComplete()
