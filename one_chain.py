import hashlib


def genesis_block_create(user_id):

    hardcoding = ["USER_ID",
                "USER_PASSWORD",
                "DATA"
    ]

    f = open("chain_db\\" + user_id + "_db","w")

    new_hash = hash(hardcoding)
    hardcoding.append(new_hash)

    f.write(str(hardcoding) + "\n")
    f.close()


    return 0

def next_block_create(user_id, user_pwd, data):
    
    hardcoding = [user_id,
                user_pwd,
                data
    ]

    # 회원가입된 체인인지 확인
    try:
        f = open("chain_db\\" + user_id + "_db","r")
        prev_block = f.readlines()
        f.close()
    except:
        return 0

    
    hardcoding.append(hashlib.sha512(str(prev_block[-1]).encode('utf-8')).hexdigest())
    f = open("chain_db\\" + user_id + "_db","a")
    f.write(str(hardcoding) + "\n")
    f.close()

    # 서버 블록 생성
    server_block = [
        "K-Shield Jr. DEFINITION TEAM",
        "2BD1144CFFE6D3A71A85B1ECFFE4D4EFA50EAD8186731E7FC8EE42FB4F814CE4C31E721FFE9F6DC9D4B2585F15F570045FC6A94EED99A1779E97C64142D3CF41",
        "Authentiacation Complete!!"
    ]

    f = open("chain_db\\" + user_id + "_db","r")
    prev_block = f.readlines()
    f.close()

    
    server_block.append(hashlib.sha512(str(prev_block[-1]).encode('utf-8')).hexdigest())
    f = open("chain_db\\" + user_id + "_db","a")
    f.write(str(server_block) + "\n")
    f.close()

    return 0

def hash(block):
    result = hashlib.sha512(str(block).encode('utf-8')).hexdigest()
    return result