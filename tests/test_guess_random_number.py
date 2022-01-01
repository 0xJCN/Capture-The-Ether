from brownie import accounts, Contract, GuessTheRandomNumberChallenge
from web3 import Web3

tx_hash = "0xb4eaed3d02a2818de1b2861291340ab7da406cccbe00615dd3187daa84389905"
eth_amount = Web3.toWei("1", "ether")


def test_guess_random_number():
    # setup accounts and contracts
    account = accounts.load("Ropsten_test_net_account")
    random_number_challenge_contract = GuessTheRandomNumberChallenge.at(
        "0x96595D7Cdef47B0439b03e34Be45e55472c35e8f"
    )
    # set up web3 and get block information via transaction hash
    w3 = Web3(
        Web3.HTTPProvider(
            "https://eth-ropsten.alchemyapi.io/v2/JNoTP19e7VPqcG8MrmeoXUlykdGCNgrF"
        )
    )
    tx = w3.eth.get_transaction(tx_hash)
    block = w3.eth.get_block(tx.blockNumber)
    block_timestamp = block.timestamp
    parent_block_hash = block.parentHash
    # calculate answer and truncate to uint8
    answer_in_bytes = Web3.solidityKeccak(
        ["bytes1", "uint256"], [parent_block_hash, block_timestamp]
    )
    answer_in_hex = Web3.toHex(answer_in_bytes)
    answer = Web3.toInt(hexstr=answer_in_hex[-2:])
    print(f"The not-so-random number was: {answer}")

    ### another way to solve this problem is to query the EVM storage of this contract
    # random_number = w3.eth.get_storage_at(
    #     "0x96595D7Cdef47B0439b03e34Be45e55472c35e8f", 0
    # )
    # answer_2 = Web3.toInt(random_number)
    # print(answer_2)

    # call guess function with answer hash
    transaction = random_number_challenge_contract.guess(
        answer, {"from": account, "value": eth_amount}
    )
    transaction.wait(1)
    print(transaction.info())
    # assert isComplete function returns true
    assert random_number_challenge_contract.isComplete()
