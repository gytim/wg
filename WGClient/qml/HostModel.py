from PyQt5.QtCore import QObject, QTimer, pyqtProperty, pyqtSignal
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine, qmlRegisterType

# password || key
class Host(QObject):
    def __init__(self
                    , it=-1, host='', user='', password='', typeAuth='password'
                    , activeHost=False, branchGit='', branchSVN='', revisionGit='', revisionSVN=''
                    , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._it = it
        self._host = host
        self._user = user
        self._password = password
        self._typeAuth = typeAuth
        self._activeHost = activeHost
        self._branchGit = branchGit
        self._branchSVN = branchSVN
        self._revisionGit = revisionGit
        self._revisionSVN = revisionSVN

    @pyqtProperty('int')
    def it(self):
        return self._it

    @pyqtProperty('bool')
    def activeHost(self):
        return self._activeHost

    @pyqtProperty('QString')
    def host(self):
        return self._host

    @pyqtProperty('QString')
    def user(self):
        return self._user

    @pyqtProperty('QString')
    def password(self):
        return self._password

    @pyqtProperty('QString')
    def typeAuth(self):
        return self._typeAuth

    @pyqtProperty('QString')
    def branchGit(self):
        return self._branchGit

    @pyqtProperty('QString')
    def branchSVN(self):
        return self._branchSVN

    @pyqtProperty('QString')
    def revisionGit(self):
        return self._revisionGit

    @pyqtProperty('QString')
    def revisionSVN(self):
        return self._revisionSVN


class HostModel(QObject):

    hostsChanged = pyqtSignal()

    index = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hosts = []

    @pyqtProperty(QQmlListProperty, notify=hostsChanged)
    def hosts(self):
        return QQmlListProperty(Host, self, self._hosts)

    def addItem(self, host='', user='', password='', typeAuth='password'):
        h1 = Host()
        h1._it = self.index + 1
        h1._user = user
        h1._host = host
        h1._typeAuth = typeAuth
        h1._password = password

        self._hosts.append(h1)
        self.hostsChanged.emit()

        print(self.index)
        print(h1._it)

    def updateModel(self):
        for host in self._hosts:
            host._activeHost = True
            host._branchGit = 'master'
            host._branchSVN = 'origin'
            host._revisionGit = 'origin'
            host._revisionSVN = 'master'

        self.hostsChanged.emit()
