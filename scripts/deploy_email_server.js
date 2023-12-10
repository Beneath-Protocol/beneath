const hre = require("hardhat");
const fs = require("fs");

async function main() {

    const lockedAmount = hre.ethers.utils.parseEther("0.001");
    const contract = await hre.ethers.deployContract("Email_server", {
        value: lockedAmount,
    });
    fs.writeFile("email_server_hash",contract.address,()=>{})
}
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});

// const hre = require("hardhat");
// const fs = require("fs");
// async function main() {
//     const lockedAmount = hre.ethers.utils.parseEther("0.001");
//     const contract = await hre.ethers.deployContract("BasicMessageReceiver", ["0xd0daae2231e9cb96b94c8512223533293c3693bf"], {
//         value: lockedAmount,
//     });
//     console.log(`${(await contract.deployed()).address}`);
//     fs.writeFile("hash",contract.address,()=>{})
// }
// main().catch((error) => {
//     console.error(error);
//     process.exitCode = 1;
// });