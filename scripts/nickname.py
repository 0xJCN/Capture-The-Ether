from brownie import CaptureTheEther, accounts, Contract, NicknameChallenge
from web3 import Web3


def set_nickname():
    account = accounts.load("Ropsten_test_net_account")
    contract = Contract.from_abi(
        "CaptureTheEther",
        "0x71c46Ed333C35e4E6c62D32dc7C8F00D125b4fee",
        CaptureTheEther.abi,
    )
    # get the hex of name
    nickname = Web3.toHex(text="SuperJay")
    print(nickname)
    # manually add padding to right side of hex string
    length = len(str(contract.nicknameOf(account.address)))
    nickname = str(nickname) + ("0" * (length - len(nickname)))
    # print new hex string of nickname with padding added
    print(nickname)
    # print old mapping
    print(contract.nicknameOf(account.address))
    # call function and set nickname to nickname
    transaction = contract.setNickname(nickname, {"from": account})
    transaction.wait(1)
    print(contract.nicknameOf(account.address))
    # check that first character of our hex string is not null
    # padding was needed to ensure that the first character was not null
    print(contract.nicknameOf(account.address)[0])
    name_contract = Contract.from_abi(
        "NicknameChallenge",
        "0xBE077Ab356BFA919ecde5e0b15322ad5CC3eEE7B",
        NicknameChallenge.abi,
    )
    if name_contract.isComplete():
        print("we did it!!!")


def main():
    set_nickname()
