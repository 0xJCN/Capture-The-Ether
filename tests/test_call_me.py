from brownie import CallMeChallenge, accounts, Contract


def test_call_me():
    account = accounts.load("Ropsten_test_net_account")
    call_me_challenge_contract = Contract.from_abi(
        "CallMeChallenge",
        "0xeFaD3a832C3bF8E42d67a35E7E803DF288333A8A",
        CallMeChallenge.abi,
    )
    # this is also another way to interact with a deployed contract
    # call_me_challenge_contract = CallMeChallenge.at(
    #     "0xeFaD3a832C3bF8E42d67a35E7E803DF288333A8A"
    # )
    print(call_me_challenge_contract.isComplete())
    transaction = call_me_challenge_contract.callme({"from": account})
    transaction.wait(1)
    assert call_me_challenge_contract.isComplete()
