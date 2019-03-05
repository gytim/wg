import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.2
import QtQuick.Controls.Material 2.5
import QtQuick.Layouts 1.3
import QtGraphicalEffects 1.12

import "."

Page {
    HostAdd{
        id: hostAdd
    }

    header: Label {
        text: qsTr("")
        font.pixelSize: Qt.application.font.pixelSize * 2
        padding: 10
    }

    RowLayout{
        anchors{
            left: pane.left
            bottom: pane.top
            bottomMargin: 10
        }

        Label {
            text: qsTr("Host(server) ")
        }
        Rectangle {
            width: 200
            height: 30

            color: "transparent"

            TextField {
                id: hostServerText
                width: parent.width

                font.pointSize: 12

                selectByMouse: true
                text: "localhost:8880"
            }
        }
        Label {
            text: qsTr("key ")
        }
        Rectangle {
            width: 200
            height: 30

            color: "transparent"

            TextField {
                id: keyServerText
                width: parent.width

                font.pointSize: 12

                selectByMouse: true
                text: "Art0fWar"
            }
        }
    }

    RowLayout{
        anchors.right: pane.right
        anchors.bottom: pane.top

        ToolButton  {
            width: 60
            height: 60

            icon {
                source:  "qrc:/img/baseline-add_circle-24px.svg"
                color: startStopButton.statusStart ? "#AAAAAA" : "#1976D2"
                width: 40
                height:40
            }

            enabled: !startStopButton.statusStart

            onClicked: {
                hostAdd.open()
            }
        }
        ToolButton  {
            width: 60
            height: 60

            icon {
                source:  "qrc:/img/baseline-cancel-24px.svg"
                color: startStopButton.statusStart ? "#AAAAAA" : "#1976D2"
                width: 40
                height:40
            }

            enabled: !startStopButton.statusStart

            onClicked: {
                pyWarClient.deleteItem(clientList.currentItem)
            }
        }
    }

    Pane{
        id: pane

        width: parent.width * 0.85

        anchors {
            margins: 10
            top: parent.top
            topMargin: 10
            bottom: startStopButton.top
            bottomMargin: 10

            horizontalCenter: parent.horizontalCenter
        }

        Material.elevation: 10
    }

    ToolButton  {
        id: startStopButton
        property bool statusStart: false

        anchors {
            bottom: parent.bottom
            horizontalCenter: parent.horizontalCenter
        }

        width: 100
        height: 100

        icon {
            source: statusStart ? "qrc:/img/baseline-stop-24px.svg" : "qrc:/img/baseline-play_arrow-24px.svg"

            width: 100
            height:100

            color: statusStart ? "#D50000" : "#00C853"
        }

        onClicked: {
            statusStart = !statusStart

            pyWarClient.updateServer(hostServerText.text, keyServerText.text)

            if(statusStart)
                timer.start()
            else
                timer.stop()
        }
    }

    ListView {
        id: clientList

        property string currentItem: "-1"

        anchors {
            left: pane.left
            top: pane.top
            bottom: pane.bottom
            right: pane.right
        }

        currentIndex: 0

        headerPositioning: ListView.OverlayHeader
        header: HostListHeader{}

        highlight: Rectangle { color: "lightsteelblue"; opacity: 0.3}

        focus: true

        model: pyWarHostModel.hosts
        delegate: HostListComponent{}
    }

    Timer{
        id: timer
        interval: 20000
        repeat: true

        onTriggered: {
            pyWarClient.updateModel()
        }
    }
}
