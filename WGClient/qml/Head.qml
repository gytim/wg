import QtQuick 2.12
import QtQuick.Controls 2.12

ToolBar {
    property alias mainLabel: mainLabel


    Label {
        id: mainLabel
        text: qsTr("WGClient")

        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }

    //Область шапки
    MouseArea{
        anchors.fill: parent
        onDoubleClicked: window.visibility === Qt.MaximumSize ? window.showMaximized(): window.showNormal()

        onPressed: {
            previousX = mouseX
            previousY = mouseY
        }

        onMouseXChanged: {
            var dx = mouseX - previousX
            window.setX(window.x + dx)
        }

        onMouseYChanged: {
            var dy = mouseY - previousY
            window.setY(window.y + dy)
        }
    }

    //Закрыть окно
    ToolButton  {
        id: closeButton
        text: "\u26CC"

        anchors.right: parent.right
        anchors.top: parent.top
        width: 40

        onClicked: close()
    }
    //Развернуть окно
    ToolButton  {
        id: sizeButton
        text: "\u2610"

        anchors.right: closeButton.left
        width: 40

        onClicked: window.visibility === Qt.MaximumSize ? window.showMaximized(): window.showNormal()
    }
    //Свернуть окно
    ToolButton  {
        id: hideButton
        text: "\u268A"

        anchors.right: sizeButton.left
        width: 40

        onClicked: window.showMinimized()
    }

}
