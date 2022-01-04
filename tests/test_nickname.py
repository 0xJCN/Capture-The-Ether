from brownie import accounts, CaptureTheEther, NicknameChallenge
from web3 import Web3

ctf_address = "0x71c46Ed333C35e4E6c62D32dc7C8F00D125b4fee"
challenge_address = "0xBE077Ab356BFA919ecde5e0b15322ad5CC3eEE7B"


def test_nickname():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get ctf and challenge contract
    ctf = CaptureTheEther.at(ctf_address)

    challenge = NicknameChallenge.at(challenge_address)

    # convert name into hex string with padding
    nickname = Web3.toHex(text="your-nickname")
    length = len(str(ctf.nicknameOf(account.address)))
    nickname = str(nickname) + ("0" * (length - len(nickname)))
    print(nickname)

    # set nickname by calling function
    tx = ctf.setNickname(nickname, {"from": account})
    tx.wait(1)
    print(ctf.nicknameOf(account.address))

    # assert that isComplete function returns true in challenge contract
    assert challenge.isComplete()
