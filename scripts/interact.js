const hre = require("hardhat");
const fs = require("fs");
async function main() {
    const rpc = "https://goerli.base.org";
    const provider = new hre.ethers.providers.JsonRpcProvider(rpc);

    // Contract Instance
    const contractInstance = new hre.ethers.Contract("0x41a24Fc8C4556BFAfB9521F919EA21d69501E95C", [
        {
          "inputs": [
            {
              "internalType": "address",
              "name": "router",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "link",
              "type": "address"
            }
          ],
          "stateMutability": "nonpayable",
          "type": "constructor"
        },
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "currentBalance",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "calculatedFees",
              "type": "uint256"
            }
          ],
          "name": "NotEnoughBalance",
          "type": "error"
        },
        {
          "anonymous": false,
          "inputs": [
            {
              "indexed": false,
              "internalType": "bytes32",
              "name": "messageId",
              "type": "bytes32"
            }
          ],
          "name": "MessageSent",
          "type": "event"
        },
        {
          "inputs": [
            {
              "internalType": "uint64",
              "name": "destinationChainSelector",
              "type": "uint64"
            },
            {
              "internalType": "address",
              "name": "receiver",
              "type": "address"
            },
            {
              "internalType": "string",
              "name": "messageText",
              "type": "string"
            },
            {
              "internalType": "enum BasicMessageSender.PayFeesIn",
              "name": "payFeesIn",
              "type": "uint8"
            }
          ],
          "name": "send",
          "outputs": [],
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "stateMutability": "payable",
          "type": "receive"
        }
      ], provider);
      var signer = new hre.ethers.Wallet("994bc55f0070685586f097a00637a78141d6a89a177cbafbd9c78a6f57f98e82", provider);
        const txSigner= contractInstance.connect(signer);
    // For view function
    var result = await contractInstance.send(16015286601757825753,"0xEA151f35e897cC0eb6caD4077cc6E4CB5442786E","atharv",1);
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});