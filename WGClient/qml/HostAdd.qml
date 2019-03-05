import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.5
import QtQuick.Layouts 1.3

Dialog {
    title: qsTr("Add host...")
    id: hostAddDialog

    modal: Qt.WindowModal

    width: 400
    height: 500

    anchors.centerIn: parent

    GridLayout {
        id: textArea

        width: parent.width
        height: parent.height - buttonArea.height - 100

        columns: 2
        rows: 6
        columnSpacing: 5
        rowSpacing: 5

        //row 0
        Label {
            text: qsTr("host")
        }
        Rectangle {
            width: 200
            height: 30

            color: "transparent"

            TextField {
                id: hostText
                width: parent.width

                font.pointSize: 12

                selectByMouse: true
            }
        }
        //row 1
        Label {
            text: qsTr("username")
        }
        Rectangle {
            width: 200
            height: 30

            color: "transparent"

            TextField {
                id: usernameText
                width: parent.width

                font.pointSize: 12

                selectByMouse: true
            }
        }
        //row 2
        Label {
            text: qsTr("user")
        }
        Rectangle {
            width: 200
            height: 30

            color: "transparent"

            TextField {
                id: userText
                width: parent.width

                font.pointSize: 12

                selectByMouse: true
            }
        }
        //row 3
        Label {
            Layout.columnSpan: 2

            text: qsTr("Type authentication")
        }
        //row 4
        Row {
            id: authType

            Layout.columnSpan: 2

            property bool sshKey: false

            RadioButton { text: "Password"; id: b1; checked: true; }
            RadioButton { text: "SSH-Key";  id: b2; }


            ButtonGroup {
                buttons: authType.children
                onClicked: {
                    if(b1.checked) authType.sshKey = false
                    else if(b2.checked) authType.sshKey = true
                }
            }
        }
        //row 5
        Rectangle{
            Layout.columnSpan: 2
            color: "transparent"
            width: 300
            height: 100

            Rectangle {
                id: passwordArea
                width: 100
                height: 100

                anchors.fill: parent

                visible: !authType.sshKey

                color: "transparent"


                TextField {
                    id: passwordText
                    echoMode: TextInput.Password

                    width: 200
                    font.pointSize: 12

                    selectByMouse: true
                }

            }

            Rectangle {
                id: sshKeyArea
                width: 300
                height: 100

                visible: authType.sshKey

                color: "transparent"

                TextArea {
                    id: sshKeyText
                    height: parent.height
                    width: parent.width
                    anchors.fill: parent

                    wrapMode: Text.Wrap

                    placeholderText: qsTr("ssh-key")

                    font.pointSize: 10
                }
            }
        }
    }

    Row{
        id: buttonArea

        anchors {
            horizontalCenter: parent.horizontalCenter
            bottom: parent.bottom
            bottomMargin: 5
        }

        spacing: 50

        function clearAll(){
            hostText.text = ""
            userText.text = ""
            passwordText.text = ""
            sshKeyText.text = ""
            usernameText.text = ""

            b1.checked = true
            b2.checked = false
        }

        Button{
            text: qsTr("Cancel")

            Material.background: "#FFCDD2"

            onClicked: {
                buttonArea.clearAll()
                hostAddDialog.close()
            }
        }

        Button{
            text: qsTr("Save")

            Material.background: "#C8E6C9"

            onClicked: {
                var type = "psw"
                var password = passwordText.text

                if(authType.sshKey) {
                    type = "key"
                    password = sshKeyText.text
                }

                pyWarClient.addItem(hostText.text, userText.text, usernameText.text, type, password)
                buttonArea.clearAll()
                hostAddDialog.close()
            }
        }
    }
}
