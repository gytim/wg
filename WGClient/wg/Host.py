from PyQt5.QtCore import QObject, QTimer, pyqtProperty, pyqtSignal
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine, qmlRegisterType

# password || key
class Host(QObject):
    def __init__(self
                    , it=-1, hostname='', user='', password='', typeAuth='psw'
                    , activeHost=False, branchGit='', branchSVN='', revisionGit='', revisionSVN=''
                    , username = ''
                    , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._it = it
        self._hostname = hostname
        self._user = user
        self._username = username
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
    def hostname(self):
        return self._hostname

    @pyqtProperty('QString')
    def user(self):
        return self._user

    @pyqtProperty('QString')
    def username(self):
        return self._username

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

