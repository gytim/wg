from PyQt5.QtCore import QObject, QTimer, pyqtProperty, pyqtSignal
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine, qmlRegisterType

from wg.Host import Host
import wg.Request as request

class HostModel(QObject):

    hostsChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = -1
        self.hostList = []

    @pyqtProperty(QQmlListProperty, notify=hostsChanged)
    def hosts(self):
        return QQmlListProperty(Host, self, self.hostList)

    def addItem(self, hostname='', user='', username = '', typeAuth='psw', password=''):
        h1 = Host()
        self.index = self.index + 1
        h1._it = self.index
        h1._user = user
        h1._username = username
        h1._hostname = hostname
        h1._typeAuth = typeAuth
        h1._password = password

        self.hostList.append(h1)
        self.hostsChanged.emit()

    def updateModel(self, _hostList):
        del self.hostList

        self.hostList = _hostList

        self.hostsChanged.emit()

    def deleteItem(self, id):

        for host in self.hostList:
            if str(host._it) == str(id):
                self.hostList.remove(host)
                break

        self.hostsChanged.emit()

    def clearList(self):
        del self.hostList
        self.index = -1
