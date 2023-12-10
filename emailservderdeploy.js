const hre = require("hardhat");
const fs = require("fs");

async function main() {

    const lockedAmount = hre.ethers.utils.parseEther("0.001");
    const contract = await hre.ethers.deployContract("Email_server",["0xa8c0c11bf64af62cdca6f93d3769b88bdd7cb93d","0xd886e2286fd1073df82462ea1822119600af80b6"], {
        value: lockedAmount,
    });

    console.log(`${(await contract.deployed()).address}`);
    fs.writeFile("hash",contract.address,()=>{})
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});