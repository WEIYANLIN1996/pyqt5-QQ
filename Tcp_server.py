#-*-coding:utf-8-*-

from socket import *
import threading



address='127.0.0.1'
port=6337
buffsize=1024
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(10)     #最大连接数

client_list=[]

user_list=[[2097557613,123456],[2097557614,123456],[2097557615,123456],[2097557616,123456],[2097557617,123456],[2097557618,123456]]
user_l=len(user_list)
user_client=[]
group_list=[['tcp群'],['兼职群'],['同学群'],['学习资料群']]

def login(logindata,clientsock):

    for x in range(0,user_l):
        print("登录请求"+str(logindata[1]))
        if len(user_client)>=1:
            ul=len(user_client)

            if str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])!=str(logindata[2]):
                login_bkinfo = 'flase-pw'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])==str(logindata[2]):
                for user_cl in range(0, ul):
                    if str(user_client[user_cl][0]) == str(logindata[1]):
                        login_bkinfo = 'flase-login'
                        clientsock.send(login_bkinfo.encode())
                        break
                    elif user_cl == ul - 1:
                        usercl=[]
                        usercl.append(logindata[1])
                        usercl.append(clientsock)
                        login_bkinfo = 'true'
                        user_client.append(usercl)
                        print(user_client)
                        clientsock.send(login_bkinfo.encode())
                break
            elif x==user_l-1:
                login_bkinfo = 'flase-user'
                clientsock.send(login_bkinfo.encode())

        else:

            if str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])!=str(logindata[2]):
                login_bkinfo = 'flase-pw'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])==str(logindata[2]):
                usercl=[]
                usercl.append(logindata[1])
                usercl.append(clientsock)
                login_bkinfo = 'true'
                user_client.append(usercl)
                print(user_client)
                clientsock.send(login_bkinfo.encode())
                break
            elif x==user_l-1:
                login_bkinfo = 'flase-user'
                clientsock.send(login_bkinfo.encode())






def tcplink(clientsock,clientaddress):
    group_l = len(group_list)
    while True:
        recvdata=clientsock.recv(buffsize).decode('utf-8')
        logindata=recvdata.split(' ')
        print(logindata)
        if str(logindata[0])=='login':
            login(logindata,clientsock)

        elif str(logindata[0])=='wechat_req':
            #reqci=1
            for y in range(0,group_l):
                if str(group_list[y][0])==str(logindata[1]):
                    requser=str(logindata[2])+' '+'加入'
                    group_list[y].append(clientsock)
                    groupl=len(group_list[y])
                    if groupl>2:
                        for h in range(1,groupl):
                            group_list[y][h].send(requser.encode())
                    else:
                        clientsock.send(requser.encode())
                    break

        elif str(logindata[0])=='wechat':
            for wl in range(0,group_l):
                if str(group_list[wl][0])==str(logindata[1]):
                    senddata=str(logindata[2])+":"+str(logindata[3])
                    l = len(group_list[wl])
                    try:
                        if l >=2:
                            for x in range(1, l):
                                group_list[wl][x].send(senddata.encode())
                        else:
                            clientsock.send(senddata.encode())
                            break
                        print("群聊信息" + str(senddata)+str(clientaddress))
                    except ValueError:
                        break

        elif str(logindata[0])=='personal':
            #print(logindata)
            user_cl = len(user_client)
            #print(user_client)
            send_info = str(logindata[1])+":"+str(logindata[3])
            z=1
            for pl in range(0,user_cl):
                if user_client[pl][0]==logindata[2]:
                    user_client[pl][1].send(send_info.encode())
                    #clientsock.send(send_info.encode())
                    break
                elif z==user_cl:
                    back=str(logindata[2])+'不在线'
                    clientsock.send(back.encode())
                z+=1

        elif str(logindata[0])=='':
            print('无法识别：')
            print(logindata[0])
            break

    clientsock.close()
    del client_list[-1]




while True:
    clientsock,clientaddress=s.accept()
    client_list.append(clientsock)
    print('connect from:',clientaddress)
    '''joinfo=str(clientaddress)
    try:
        ld=len(client_list)
        for x in range(0, ld):
            client_list[x].send(joinfo.encode())
    except ValueError:
        continue
    '''
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))  #新创建的线程
    t.start()
s.close()



