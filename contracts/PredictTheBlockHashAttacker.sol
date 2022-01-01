// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

interface IPredictTheBlockHashChallenge {
    function isComplete() external view returns (bool);

    function lockInGuess(bytes32 hash) external payable;

    function settle() external;
}

contract PredictTheBlockHashAttacker {
    IPredictTheBlockHashChallenge challenge;
    address payable owner;
    uint256 public currentBlockNumber;

    constructor(address _challenge) {
        challenge = IPredictTheBlockHashChallenge(_challenge);
        owner = payable(msg.sender);
    }

    function lockInMyGuess(bytes32 _hash) external payable {
        require(msg.value == 1 ether);
        challenge.lockInGuess{value: 1 ether}(_hash);
    }
}
