from chainutil import Blockchain, blockchains
import litedb

for chain in blockchains:
    for x in litedb.get("deployed_servers_"+chain):
        arbitrum=Blockchain(chain, x, abi_file_path="/Users/aaravdayal/beneath-protocol/artifacts/contracts/email_server.sol/Email_server.json")
        print(arbitrum.call_func("send_web2_mail",["aludayalu@lumatozer","Hello","Test","aludayalu@lumatozer"]))