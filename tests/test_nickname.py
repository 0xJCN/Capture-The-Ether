from brownie import CaptureTheEther, accounts, Contract, NicknameChallenge
from web3 import Web3


def test_nickname():
    # setup accounts and contracts
    account = accounts.load("Ropsten_test_net_account")
    capture_the_ether_contract = Contract.from_abi(
        "CaptureTheEther",
        "0x71c46Ed333C35e4E6c62D32dc7C8F00D125b4fee",
        CaptureTheEther.abi,
    )
    nickname_challenge_contract = Contract.from_abi(
        "NicknameChallenge",
        "0xBE077Ab356BFA919ecde5e0b15322ad5CC3eEE7B",
        NicknameChallenge.abi,
    )
    # convert name into hex string with padding
    nickname = Web3.toHex(text="SuperJay")
    length = len(str(capture_the_ether_contract.nicknameOf(account.address)))
    nickname = str(nickname) + ("0" * (length - len(nickname)))
    print(nickname)
    # set nickname by calling function
    transaction = capture_the_ether_contract.setNickname(nickname, {"from": account})
    transaction.wait(1)
    print(capture_the_ether_contract.nicknameOf(account.address))
    # assert that isComplete function returns true in challenge contract
    assert nickname_challenge_contract.isComplete()
