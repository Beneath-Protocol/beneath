from web3 import providers,Web3
import os,json,time,web3,requests


blockchains={
    "polygon":"https://rpc-mumbai.polygon.technology",
    "base":"https://goerli.base.org",
    "arbitrum":"http://127.0.0.1:8545",
    "scroll":"https://sepolia-rpc.scroll.io",
    "sepolia":"https://rpc-sepolia.rockx.com"
}

class Blockchain:
    def __init__(self, blockchain, contract_hash, public_address="0x70997970C51812dc3A010C7d01b50e0d17dc79C8", private_address="0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d", abi_file_path="/Users/aaravdayal/beneath-protocol/artifacts/contracts/email_server.sol/Email_server.json") -> None:
        rpc=blockchains[blockchain]
        self.provider=providers.rpc.HTTPProvider(rpc)
        self.hash=contract_hash
        self.w3=Web3(self.provider)
        self.caller = public_address
        self.private_key=private_address
        self.Chain_id = self.w3.eth.chain_id
        self.abi=json.loads(open(abi_file_path).read())["abi"]
    def call_func(self,name,args=[]):
        contract_address=self.hash
        contract = self.w3.eth.contract(address=contract_address,abi=self.abi)
        statement=f"call_function = contract.functions.{name}({','.join([json.dumps(x) for x in args])}).build_transaction("+"""
            {
                'from': self.caller,
                'nonce': self.w3.eth.get_transaction_count(self.caller),
                "gasPrice": self.w3.eth.gas_price
            }
        )
    """
        new_locals,new_globals={}|globals()|locals(),{}|globals()|locals()
        while True:
            try:
                exec(statement,new_globals,new_locals)
                break
            except requests.exceptions.HTTPError:
                time.sleep(1)
                continue
        call_function=new_locals["call_function"]
        tx_create = self.w3.eth.account.sign_transaction(call_function, self.private_key)
        while True:
            try:
                tx_hash = self.w3.eth.send_raw_transaction(tx_create.rawTransaction)
                break
            except Exception as e:
                if web3.exceptions.TimeExhausted==type(e):
                    return
                elif requests.exceptions.HTTPError==e:
                    time.sleep(1)
                    continue
                else:
                    raise e
        while True:
            try:
                self.w3.eth.wait_for_transaction_receipt(tx_hash)
                break
            except Exception as e:
                if web3.exceptions.TimeExhausted==type(e):
                    return
                elif requests.exceptions.HTTPError==e:
                    time.sleep(1)
                    continue
                else:
                    raise e
        return "0x"+"".join(["{:02X}".format(b).lower() for b in tx_hash])
    def local_call(self,name,args=[]):
        contract_address=self.hash
        contract = self.w3.eth.contract(address=contract_address,abi=self.abi)
        statement=f"call_function = contract.functions.{name}({','.join([json.dumps(x) for x in args])}).call()"
        new_locals,new_globals={}|globals()|locals(),{}|globals()|locals()
        while True:
            try:
                exec(statement,new_globals,new_locals)
                break
            except requests.exceptions.HTTPError:
                time.sleep(1)
                continue
        call_function=new_locals["call_function"]
        return call_function