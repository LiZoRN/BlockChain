var VotingContract = artifacts.require("./Voting.sol");

module.exports = function(deployer) {
  deployer.deploy(VotingContract,['Rama', 'Nick', 'Jose'], {gas: 6700000});
};
