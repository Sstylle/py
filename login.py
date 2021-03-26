# coding: utf-8


class Account(object):
    def __init__(self, username, password, des, state=0):
        self.username = username
        self.password = password
        self.des = des
        self.state = state

    def __str__(self):
        return 'user：%s' % self.username


class AccountManage(object):
    account = []

    def start(self):
        self.account.append(Account('sushaolin', '123456', '', 0))
        # print(self.account[0])

    def Menu(self):
        while True:
            if self.islogin():
                onlog = self.islogin()
                print('''
=======%s，欢迎回来，登出请输入q=======
1、function one
2、function two
3、……
                ''' % onlog.username)
                choice = input('请输入你的选择：')
                if choice == 'q':
                    self.logout(onlog)
                elif choice == '1':
                    pass
                elif choice == '2':
                    pass
                else:
                    print('请输入正确的选择！')
            else:
                print('''
=======登入系统=======
1.登入
2.注册
3.退出
                ''')
                choice = input('请输入你的选择：').strip()
                if choice == '1':
                    self.login()
                elif choice == '2':
                    self.register()
                elif choice == '3':
                    print('欢迎下次使⽤')
                    exit()
                else:
                    print('请输入正确的选择！')

    def login(self):
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        aObj = self.isAccountExist(username)
        # print(aObj)
        if aObj == False:
            print('用户不存在！请在首页输入2注册')
        else:
            if aObj.password == password:
                aObj.state = 1
                print('登录成功')
            else:
                print('密码错误')

    def isAccountExist(self, name):
        for account in self.account:
            if account.username == name:
                return account
            # elif not name:
            #     print()
        return False

    def islogin(self):
        for account in self.account:
            if account.state:
                return account
        return False

    def logout(self, acc):
        acc.state = 0
        print('登出成功。')

    def register(self):
        while True:
            print('\n', '注册'.center(20, '='))
            username = input('请输入用户名：').strip()
            password = input('请输入密码：').strip()
            if not bool(username) & bool(password):
                print('用户名和密码都不能为空！重新输入')
            if bool(self.isAccountExist(username)):
                print('''
该用户已存在
1、重新注册
2、返回首页
                ''')
                choice = input('请输入你的选择：').strip()
                if choice == '1':
                    pass
                elif choice == '2':
                    break
                else:
                    print('请输入正确的选择！')
            else:
                self.account.append(Account(username, password, '', state=1))
                # for account in self.account:
                #     print(account.username,account.state)
                print('注册成功！并登录成功！')
                break


if __name__ == '__main__':
    aManger = AccountManage()
    aManger.start()
    aManger.Menu()

    # pass
