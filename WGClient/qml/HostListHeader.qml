import QtQuick 2.0

Rectangle {
    id: headerItem
    width: parent.width
    height: 30
    z: 2

    color: "#eaeaea"

    Text {
        anchors.verticalCenter: parent.verticalCenter
        x: 5

        text: "Host"
        color: "gray"
    }
    Text {
        anchors.verticalCenter: parent.verticalCenter
        x: 5 + parent.width / 4

        text: "Username"
        color: "gray"
    }
    Text {
        anchors.verticalCenter: parent.verticalCenter
        x: 5 + 2 * parent.width / 4

        text: "SVN"
        color: "gray"
    }
    Text {
        anchors.verticalCenter: parent.verticalCenter
        x: 5 + 3 * parent.width / 4

        text: "GIT"
        color: "gray"
    }    
}
