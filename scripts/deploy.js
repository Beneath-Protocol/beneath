const hre = require("hardhat");
const fs = require("fs");

async function main() {

    const lockedAmount = hre.ethers.utils.parseEther("0.001");
    const contract = await hre.ethers.deployContract("Central", {
        value: lockedAmount,
    });

    console.log(`${(await contract.deployed()).address}`);
    fs.writeFile("hash",contract.address,()=>{})
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});