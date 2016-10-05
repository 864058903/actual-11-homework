#encoding: utf-8

path = "user.txt"
f1 = open(path, 'r')
user_dict = dict([ (line.split(":")[0], line.split(":")[1] ) for line in f1.readlines() ])
f1.close()
print user_dict


def update_user():
    print user_dict
    cnt = [ "%s:%s:%s" % (x,y,"\n") for x,y in user_dict.itmes() ]
    f2 = open("user.txt", "w")
    for i in cnt:
        f2.write(i)

def register():
    print "add user here!"
    name = raw_input("Please enter your name: ")
    if name not in user_dict.keys():
        passwd = raw_input("PASSWD: ")
        if passwd != "":
            user_dict[name] = passwd
            update_user()
            print "Succsesfully. "
        else:
            print "passwd can't be empty."
    else:
        print "username is already be used."

def login():
    print "login here."
    name = raw_input("Please enter your login name:")
    passwd = raw_input("Please enter your passwd: ")
    if user_dict.get(name) != passwd :
        print "something is error. Please check your input."
    else:
        update_user()
        print "congratulations."
        user_m(name)

def user_m(name):
    print "Hi, %s. weclome to login in." % name
    while True:
        cmd = raw_input("You can wathc other user name by '1', edit passwd by '2', exit input '3' ")
        if cmd == "3":
            break
        elif cmd == "1":
            user_list = user_dict.keys()[:]
            user_list.remove(name)
            print user_list
        elif cmd == "2":
            new_pass = raw_input("New passwd here:")
            if new_pass != "":
                user_dict[name] = new_pass
                update_user()
                print "passwd update."
            else:
                print "passwd can't be empty."

print "welcome to systerm. "

while True:
    command = raw_input("""Enter your command:
            1. regiter
            2. login
            3. exit
            """)
    if command == "1":
        register()
    elif command == "2":
        login()
    elif command == "3":
        break
    else:
        continue
