from chainutil import Blockchain, blockchains
import litedb, os, threading, time, json, uuid, hashlib, traceback, chainutil
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import subprocess

processing_txs=False

def address_to_details(address):
    address_details=litedb.get(address.split("@")[1])
    return {
        "contract_hash":address_details["contract"],
        "blockchain":address_details["blockchain"]
    }

def mail_thread():
    import time, imaplib
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('beneathprotocol@gmail.com', 'payp dfju wdzl ipzy')
    mail.list()
    latest_email_uid = ''

    while True:
        mail.select("Inbox", readonly=True)
        result, data = mail.uid('search', None, "ALL")
        ids = data[0]
        id_list = ids.split()
        if data[0].split()[-1] == latest_email_uid:
            time.sleep(10)
        else:
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', data[0].split()[-1], '(RFC822)')
            raw_mail = data[0][1]
            try:
                if b"ethmail:" in raw_mail and raw_mail.count(b"Reply by sending")!=1 not in raw_mail and raw_mail.split(b"ethmail:")[1].split(b"\n")[0].strip()!=b"":
                    to_email=raw_mail.split(b"ethmail:")[1].split(b"\n")[0].strip().decode()
                    address_details=address_to_details(to_email)
                    user_object=central_server.local_call("get_user",[to_email])
                    print(user_object)
                    if user_object[0]!="":
                        domain_object_call=central_server.local_call("get_domain",[to_email.split("@")[1]])
                        unique_id=uuid.uuid4().__str__()
                        litedb.set(unique_id, {"owner":to_email,"data":b"\n".join(raw_mail.split(b"ethmail:")[1].split(b"\n")[1:5]).strip().decode()})
                        Blockchain(litedb.get(to_email.split("@")[1])["blockchain"], domain_object_call[3], abi_file_path="/Users/aaravdayal/beneath-protocol/artifacts/contracts/email_server.sol/Email_server.json").call_func("recv_mail",[raw_mail.split(b"To: ")[1].split(b"\n")[0].decode().strip(),unique_id,"web2",to_email])
                        print("Sent web3 mail to",to_email)
            except:
                import traceback
                traceback.print_exc()
            time.sleep(10)

threading.Thread(target=mail_thread).start()

def send_mail(to,message,subject):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = "Beneath Protocol beneathprotocol@gmail.com"
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    sender_mail="beneathprotocol@gmail.com"
    mailserver.login(sender_mail, "payp dfju wdzl ipzy")

    mailserver.sendmail(sender_mail,to,msg.as_string())

def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def load_key_from_hex(hex_key):
    key_bytes = hex_to_bytes(hex_key)
    return serialization.load_pem_public_key(
        key_bytes,
        backend=default_backend()
    )

def encrypt_data(public_key, data):
    ciphertext = public_key.encrypt(
        data.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def load_private_key_from_hex(hex_key):
    key_bytes = hex_to_bytes(hex_key)
    return serialization.load_pem_private_key(
        key_bytes,
        password=None,
        backend=default_backend()
    )

def decrypt_data(private_key, encrypted_data):
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data.decode('utf-8')

from flask import Flask, Response, request
import flask

central_server=Blockchain("arbitrum", open("hash").read(), abi_file_path="/Users/aaravdayal/beneath-protocol/artifacts/contracts/central.sol/Central.json")

app=Flask(__name__)

def make_response(data):
    if type(data)!=str:
        data=json.dumps(data)
    resp=Response(data)
    resp.headers["Access-Control-Allow-Origin"]="*"
    return resp

threading.Thread(target=(lambda: os.system("node lightousenode.mjs"))).start()
time.sleep(1)

def web2_mail():
    pass

def mail_event_loop():
    logs_={}
    while True:
        for chain in blockchains:
            if chain not in logs_:
                logs_[chain]=[]
            for x in litedb.get("deployed_servers_"+chain):
                try:
                    server_hash=x
                    logs = Blockchain(chain,x).w3.eth.contract(address=x,abi=json.loads(open("artifacts/contracts/email_server.sol/Email_server.json").read())["abi"]).events.external_mail().get_logs()
                    if logs_[chain]!=logs:
                        for x in logs:
                            if x not in logs_:
                                if central_server.local_call("get_user",[x["args"]["from"]])[0]!="":
                                    send_mail(x["args"]["to"],"Email from: "+x["args"]["from"]+"\n"+"Reply by sending:\nethmail: "+x["args"]["from"]+"\n"+"Content"+"\n\n"+x["args"]["content"],x["args"]["subject"])
                        logs_[chain]=logs
                except:
                    traceback.print_exc()
        time.sleep(2)

threading.Thread(target=mail_event_loop).start()

@app.get("/register")
def register():
    global processing_txs
    while processing_txs:
        time.sleep(0.5)
    args=dict(request.args)
    if central_server.local_call("get_domain",[args["domain"]])[0]=="":
        processing_txs=True
        try:
            args["chain"]=args["chain"].lower()
            uid=hashlib.sha256(args["public_key"].encode()+"__abhishek bhaiya__".encode()).hexdigest()
            litedb.set(args["domain"], {"owner":args["public_key"], "blockchain":args["chain"], "domain":args["domain"]})
            litedb.set(args["username"]+"@"+args["domain"],{"uid":uid, "password":args["password"]})
            print("Deploying contract")
            print(f"npx hardhat run --network {args['chain']} scripts/deploy_email_server.js")
            subprocess.run(f"npx hardhat run --network {args['chain']} scripts/deploy_email_server.js".split())
            time.sleep(5)
            print("Deployed contract")
            email_server_hash=open("email_server_hash").read()
            central_server.call_func("add_domain",[args["domain"], args["chain"], email_server_hash])
            litedb.set(args["domain"], {"owner":args["public_key"], "blockchain":args["chain"], "domain":args["domain"], "contract":email_server_hash})
            print("Adding domain")
            central_server.call_func("add_user",[args["domain"],args["username"],args["public_key"]])
            print("Adding user")
            servers_key="deployed_servers_"+args['chain']
            litedb.set(servers_key,litedb.get(servers_key)+[open("email_server_hash").read()])
            processing_txs=False
            return make_response(uid)
        except:
            processing_txs=False
            traceback.print_exc()
            return make_response(False)
    if litedb.get(args["username"]+"@"+args["domain"])["password"]==args["password"]:
        return make_response(litedb.get(args["username"]+"@"+args["domain"])["uid"])
    return make_response(False)

@app.get("/login")
def login():
    args=dict(request.args)
    try:
        if litedb.get(args["account"])["password"]==args["password"]:
            return make_response(litedb.get(args["account"])["uid"])
        else:
            return make_response(False)
    except:
        return make_response(False)

@app.get("/upload_mail_data")
def mails():
    unique_id=uuid.uuid4().__str__()
    litedb.set(unique_id, {"owner":request.args["owner"],"data":request.args["data"], "timestamp":time.time()})
    return make_response(unique_id)

@app.get("/download_decrypted_mail_data")
def decrypted_mail():
    args=dict(request.args)
    try:
        data=litedb.get(args["id"])
        if args["owner"]==hashlib.sha256(data["owner"].encode()+"__abhishek bhaiya__".encode()).hexdigest():
            return make_response(data["data"])
        else:
            return make_response("error")
    except:
        traceback.print_exc()
        return make_response(False)

@app.get("/send_mail")
def mail():
    args=dict(request.args)
    if litedb.get(args["username"]+"@"+args["domain"])["password"]==args["password"]:
        send_mail(args["to"],args["message"],args["subject"]+" : "+args["from"])
        return make_response("")
    return make_response(False)

@app.get("/send_mail_web3")
def send_web3_mail():
    args=dict(request.args)
    if litedb.get(args["username"]+"@"+args["domain"])["password"]==args["password"]:
        address_details=address_to_details(args["to"])
        unique_id=uuid.uuid4().__str__()
        litedb.set(unique_id, {"owner":request.args["from"],"data":"Subject: "+args["subject"]+"\n"+args["message"], "timestamp":time.time()})
        Blockchain(address_details["blockchain"], address_details["contract_hash"]).call_func("recv_mail",[args["from"],unique_id,"web3",args["to"]])
        return make_response(True)
    return make_response(False)

@app.get("/get_mails")
def all_mails():
    args=dict(request.args)
    user_object=litedb.get(args["username"]+"@"+args["domain"])
    if user_object["password"]==args["password"]:
        address_details=address_to_details(args["username"]+"@"+args["domain"])
        all_mails=Blockchain(address_details["blockchain"], address_details["contract_hash"]).local_call("get_all_mails",[])
        constructed_mails=[]
        for x in all_mails:
            try:
                date=litedb.get(x[1])["timestamp"]
            except:
                date=0
            x=list(x)
            x[1]=litedb.get(x[1])["data"]
            constructed_mails.append({"from":x[0],"content":x[1],"web":x[2],"to":x[3],"date":date})
        return make_response(constructed_mails)

app.run(port=8000)