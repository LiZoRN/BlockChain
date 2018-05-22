var Voting = artifacts.require("./Voting.sol");

module.exports = function(deployer) {
  // deployer.deploy(VotingContract,['Rama', 'Nick', 'Jose'], {gas: 6700000});
  deployer.deploy(Voting, 1000, web3.toWei('0.1', 'ether'), ['Rama', 'Nick', 'Jose']);
};
