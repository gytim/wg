# Типовой класс с данными по хосту
"""
Начальные обязятельные данные
    user : имя пользователя пример 'Вася Пупкин'
    hostname : адрес ПК, принимаю за ключ
    hostuser : пользователь
    typeAuth : тип подключения 'psw' или 'key'
    passOrKey : строка пароль или ключ

Обновлятся после подключения
    activeHost : bool активность хоста
    branchGit : ветка git
    revisionGit : коммит git
    branchSVN : ветка subversion
    revisionSVN : ревезия subversion
"""
class Host:
    def __init__(self, _user, _hostname, _hostuser):
        self.user = _user
        self.hostname = _hostname
        self.hostuser = _hostuser
        self.typeAuth = 'psw'
        self.passOrKey = _hostuser

        self.activeHost = False
        self.branchGit = ''
        self.revisionGit = ''
        self.branchSVN = ''
        self.revisionSVN = ''

    def setPassword(self, _password):
        self.typeAuth = 'psw'
        self.passOrKey = _password

    def setKey(self, _key):
        self.typeAuth = 'key'
        self.passOrKey = _key

    def setGit(self, branch, revision):
        self.branchGit = branch
        self.revisionGit = revision

    def setSVN(self, branch, revision):
        self.branchSVN = branch
        self.revisionSVN = revision

    def getGit(self):
        return self.branchGit, self.revisionGit

    def getSVN(self):
        return self.branchSVN, self.revisionSVN

    def password(self):
        return self.passOrKey

    def key(self):
        return self.passOrKey
