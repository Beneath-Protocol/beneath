from chainutil import Blockchain

arbitrum=Blockchain("https://goerli.base.org", open("hash").read(), public_address="0xbdfC42145aF525009d3eE7027036777Ed96BF6A4", private_address="994bc55f0070685586f097a00637a78141d6a89a177cbafbd9c78a6f57f98e82", contract_file_path="central")
print(arbitrum.call_func("add_user",["lumatozer","aaravdayal","0xbdfC42145aF525009d3eE7027036777Ed96BF6A4"]))
print(arbitrum.local_call("get_user",["lumatozer@aaravdayal"]))