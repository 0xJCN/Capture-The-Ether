from brownie import accounts, GuessTheSecretNumberChallenge
from web3 import Web3

eth_amount = Web3.toWei("1", "ether")
challenge_address = "0x4239B64FF74F810A9FC9C8b2de3B68Cd646Af2ba"
answer_hash = "0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365"


def brute_force_hash(answer_hash: str, bytes: int):
    # brutefoce hash to check against answer hash
    # guess function takes in an uint8 which can be any number from 0 -> 255
    for i in range(bytes):
        hexbytes = Web3.keccak(i)
        # convert to hash/hex format
        hash = Web3.toHex(hexbytes)
        if hash == answer_hash:
            print(hash, i)
            return i
        continue
    print("No answer found within this range")


def test_guess_the_secret_number():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = GuessTheSecretNumberChallenge.at(challenge_address)

    # call guess function with brute_force_hash return value as an argument
    answer = brute_force_hash(answer_hash, (2 ** 8))
    tx = challenge.guess(answer, {"from": account, "value": eth_amount})
    tx.wait(1)

    # assert isComplete() return true
    assert challenge.isComplete()
