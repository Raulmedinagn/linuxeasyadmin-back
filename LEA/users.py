import os,subprocess,json

def create_user(usr,password):
    os.system("useradd -p " + password + " " + usr)
    return os.system("grep -c " + usr + " /etc/passwd")

def delete_user(usr):
    os.system("userdel " + usr)
    return os.system("grep -c " + usr + " /etc/passwd")

def add_user_group(usr,group):
    pass

def delete_user_group(usr,group):
    pass

def change_user_password(usr,old_password,new_password):
    pass

def create_group(group):
    pass

def delete_group(group):
    pass

def get_users():
    out = subprocess.check_output("cut -d: -f1 /etc/passwd",shell=True)
    output = str(out)
    return output.split("\\n")

def get_user_groups(user):
    out = subprocess.check_output("groups " + user,shell=True)
    outStr = str(out) # TODO: change output format
    return json.dumps(outStr)
