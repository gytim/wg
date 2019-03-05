import QtQuick 2.12
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.5

ItemDelegate {
    height: 40

    MouseArea{
        anchors.fill: parent

        onClicked: {
            clientList.currentIndex = index
            clientList.currentItem = it
        }
    }

    anchors {
        left: parent.left
        right: parent.right
    }

    Rectangle{
        height: 10
        width: 10
        radius: 10

        color: activeHost ? "#00C853" : "#D50000"

        anchors {
            left: parent.left
            leftMargin: 5
            verticalCenter: parent.verticalCenter
        }
    }
    Text {
        id: hostLabel

        anchors.verticalCenter: parent.verticalCenter
        x: 15

        font.pointSize: 10

        text: hostname

    }
    Text {
        id: userLabel

        anchors.verticalCenter: parent.verticalCenter
        x: 5 + parent.width / 4

        font.pointSize: 14
        elide: Text.ElideRight

        text: username
    }

    Text {
        id: branchSVNLabel

        y: 5
        x: 10 + 2 * parent.width / 4

        font.pointSize: 10
        font.italic: true
        opacity: 0.6
        elide: Text.ElideRight        

        text: branchSVN
    }
    Text {
        id: revisionSVNLabel

        y: parent.height / 2
        x: 10 + 2 * parent.width / 4

        font.pointSize: 10
        font.italic: true
        opacity: 0.6
        elide: Text.ElideRight

        text: revisionSVN
    }

    Text {
        id: branchGitLabel

        y: 5
        x: 5 + 3 * parent.width / 4

        font.pointSize: 10
        font.italic: true
        opacity: 0.6
        elide: Text.ElideRight

        text: branchGit
    }
        Text {
        id: revisionGitLabel

        y: parent.height / 2
        x: 5 + 3 * parent.width / 4

        font.pointSize: 10
        font.italic: true
        opacity: 0.6
        elide: Text.ElideRight

        text: revisionGit
    }
}
