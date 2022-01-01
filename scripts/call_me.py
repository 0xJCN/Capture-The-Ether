from brownie import CallMeChallenge, accounts, Contract


def call_function():

    account = accounts.load("Ropsten_test_net_account")
    contract = Contract.from_abi(
        "CallMeChallenge",
        "0xeFaD3a832C3bF8E42d67a35E7E803DF288333A8A",
        CallMeChallenge.abi,
    )
    print(contract.isComplete())
    transaction = contract.callme({"from": account})
    transaction.wait(1)
    print(contract.isComplete())


def main():
    call_function()
