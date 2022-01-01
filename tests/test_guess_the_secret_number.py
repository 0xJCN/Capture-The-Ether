from brownie import accounts, Contract, GuessTheSecretNumberChallenge
from web3 import Web3

AMOUNT_OF_ETHER_TO_PAY = Web3.toWei("1", "ether")


def brute_force_hash(answer_hash: str, bytes: int):
    # brutefoce hash to check against answer hash
    # guess function takes in an uint8 which can potentially be any number from 0 - 255
    for i in range(bytes):
        hexbytes = Web3.keccak(i)
        # convert to hash/hex format
        hash = Web3.toHex(hexbytes)
        if hash == answer_hash:
            print(hash, i)
            return i
        continue
    # add error handling
    print("No answer found within this range")


def test_guess_the_secret_number():
    # setup account and challenge contract
    account = accounts.load("Ropsten_test_net_account")
    secret_number_challenge_contract = Contract.from_abi(
        "GuessTheSecretNumberChallenge",
        "0x4239B64FF74F810A9FC9C8b2de3B68Cd646Af2ba",
        GuessTheSecretNumberChallenge.abi,
    )
    # call guess function with brute_force_hash return value as the parameter/answer
    answer = brute_force_hash(
        "0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365", (2 ** 8)
    )
    transaction = secret_number_challenge_contract.guess(
        answer, {"from": account, "value": AMOUNT_OF_ETHER_TO_PAY}
    )
    transaction.wait(1)
    # print transaction information
    print(transaction.info())
    # assert isComplete() return true
    assert secret_number_challenge_contract.isComplete()
