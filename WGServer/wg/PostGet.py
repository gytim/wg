# Функции flask

from wg.Host import Host
import flask
import json

import wg.Basic as basic

def hostValidate():
    errors = []
    json = flask.request.get_json()

    if json is None:
        errors.append(
            "No JSON sent. Did you forget to set Content-Type header" +
            " to application/json?")
        return (None, errors)

    return (json, errors)


def findParams(item):
    if not 'hostname' in item \
        or not 'user' in item:
        return False

    return True


def addHosts(listHost):
    (json, errors) = hostValidate()

    if errors:
        return basic.resp(400, {"errors": errors})

    if not 'hosts' in json:
        return basic.resp(400, {"errors": "uncorrected"})

    json_hosts = json['hosts']

    for json_host in json_hosts:
        try:
            if not findParams(json_host):
                return basic.resp(400, {"errors": "uncorrected"})

            if not 'username' in json_host:
                username = str(json_host['user'])
            else:
                username = str(json_host['username'])

            newHost = Host(username, str(json_host['hostname']), str(json_host['user']))

            if 'auth_type' in json_host:
                if json_host['auth_type'] == 'psw' and 'password' in json_host:
                    newHost.setPassword(json_host['password'])
                if json_host['auth_type'] == 'key' and 'key' in json_host:
                    newHost.setKey(json_host['key'])

        except:
            continue

        listHost.append(newHost)

    return basic.resp(200, {})


def addHost(listHost):
    (json, errors) = hostValidate()

    if errors:
        return basic.resp(400, {"errors": errors})

    try:
        if not findParams(json):
            return basic.resp(400, {"errors": "uncorrected"})

        if not 'username' in json:
            username = str(json['user'])
        else:
            username = str(json['username'])

        newHost = Host(username, str(json['hostname']), str(json['user']))

        if 'auth_type' in json:
            if json['auth_type'] == 'psw' and 'password' in json:
                newHost.setPassword(json['password'])
            if json['auth_type'] == 'key' and 'key' in json:
                newHost.setKey(json['key'])
    except:
        return basic.resp(400, {"errors": "uncorrected"})

    listHost.append(newHost)

    return basic.resp(200, {})


def getHost(tmp_hosts, tmp_host):
    try:
        answer = []
        for host in tmp_hosts:
            if host.hostname == tmp_host:
                answer_item = {"username": host.user, "user": host.hostuser, "auth_type": host.typeAuth, "hostname": host.hostname}

                if not host.activeHost:
                    answer_item.update({"active": bool(False)})
                    break

                answer_item["active"] = bool(True)

                if not host.branchGit == '':
                    answer_item["git"] = {"branch": host.branchGit, "revision": host.revisionGit}

                if not host.branchSVN == '':
                    answer_item["svn"] = {"branch": host.branchSVN, "revision": host.revisionSVN}

            answer.append(answer_item)
            break
    except:
        return basic.resp(400, {"errors": "Did not form response"})

    return basic.resp(200, {"hosts": answer})


def getHosts(tmp_hosts):
    try:
        answer = []
        for host in tmp_hosts:
            answer_item = {"username": host.user, "user": host.hostuser, "auth_type": host.typeAuth, "hostname": host.hostname}

            if not host.activeHost:
                answer_item["active"] = bool(False)
                answer.append(answer_item)
                continue

            answer_item["active"] = bool(True)

            if not host.branchGit == '':
                answer_item["git"] = {"branch": host.branchGit, "revision": host.revisionGit}

            if not host.branchSVN == '':
                answer_item["svn"] = {"branch": host.branchSVN, "revision": host.revisionSVN}

            answer.append(answer_item)
    except:
        return basic.resp(400, {"errors": "Did not form response"})

    return basic.resp(200, {"hosts": answer})
