from brownie import accounts, config, Contract, GuessTheRandomNumberChallenge
from web3 import Web3

eth_amount = Web3.toWei("1", "ether")
challenge_address = "0x96595D7Cdef47B0439b03e34Be45e55472c35e8f"


def test_guess_random_number():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = GuessTheRandomNumberChallenge.at(challenge_address)

    # set up web3
    rpc_url = config["wallets"]["endpoint"]
    w3 = Web3(Web3.HTTPProvider(rpc_url))

    # get storage at slot 0
    random_number = w3.eth.get_storage_at(challenge_address, 0)
    answer = Web3.toInt(random_number)

    # call guess function with answer as argument
    transaction = challenge.guess(answer, {"from": account, "value": eth_amount})
    transaction.wait(1)

    # assert isComplete function returns true
    assert challenge.isComplete()
