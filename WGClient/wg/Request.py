import requests
import json

import wg.GlobalParams as GB
from wg.Host import Host

def statusCode(status):
    if status == requests.codes.ok:
        return True
    else:
        return False

def clearServer():
    try:
        r = requests.get('http://' + str(GB.host) + '/warapig/0.1/clear&key=' + GB.key)
        if not statusCode(r.status_code):
            print("error")
            return
    except:
        print("error")

def updateModel():
    hosts = []

    try:
        r = requests.get('http://' + str(GB.host) + '/warapig/0.1/hosts&key=' + GB.key)
        if not statusCode(r.status_code):
            return hosts
    except:
        print("erorr")

    answer = r.json()

    array = answer['hosts']
    for data in array:
        host = Host()

        host._hostname = str(data['hostname'])
        host._user = str(data['user'])
        host._activeHost = bool(data['active'])

        if 'username' in data:
            host._username = data['username']

        if not bool(data['active']):
            host._activeHost = False
            hosts.append(host)
            continue

        host._typeAuth = str(data['auth_type'])

        if 'git' in data:
            host._branchGit = str(data['git']['branch'])
            host._revisionGit = str(data['git']['revision'])

        if 'svn' in data:
            host._branchSVN = str(data['svn']['branch'])
            host._revisionSVN = str(data['svn']['revision'])

        hosts.append(host)

    return hosts


def updateServer(hostlist):
    hostList4JSON = []

    for host in hostlist:
        host4JSON = (
            {"user": str(host.user),
             "hostname": str(host.hostname),
             "username": str(host.username)}
        )
        if host.typeAuth == 'psw':
            host4JSON["auth_type"] = "psw"
            host4JSON["password"] = host.password
        elif host.typeAuth == 'key':
            host4JSON["auth_type"] = "key"
            host4JSON["key"] = host.password

        hostList4JSON.append(host4JSON)

    headers = {'Content-type': 'application/json'}

    try:
        r = requests.post('http://' + str(GB.host) + '/warapig/0.1/addhosts&key=' + str(GB.key),
                            data=json.dumps({"hosts": hostList4JSON}),
                            headers=headers
                     )
    except:
        print("error")

def ping():
    try:
        r = requests.get('http://' + str(GB.host) + '/warapig/0.1/ping&key=' + GB.key)
        if not statusCode(r.status_code):
                    print("error")
                    return
    except:
        print("error")
