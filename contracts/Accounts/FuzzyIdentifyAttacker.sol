//SPDX-License-Identifier: MIT
pragma solidity 0.8.11;

contract Name {
    function name() public view returns (bytes32) {
        return bytes32("smarx");
    }
}
