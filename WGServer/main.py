#!/usr/bin/python3
# -*- coding: utf-8 -*-

import flask
import threading
import time
import copy

import wg.GlobalParams as GP
import wg.PostGet as PostGet
import wg.Basic as basic
import wg.GITandSVN as GandS

lock = threading.Lock()

app = flask.Flask(__name__)

# =====================================================================
# Главный список!!! вокруг него все крутиться
listHost = []


# =====================================================================
# Возврат ошибок
#
@app.route('/')
def hello_world():
    return basic.resp(400, {})


@app.errorhandler(400)
def page_not_found(e):
    return basic.resp(400, {})


@app.errorhandler(404)
def page_not_found(e):
    return basic.resp(400, {})


@app.errorhandler(405)
def page_not_found(e):
    return basic.resp(405, {})


@app.route('/warapig/0.1/ping&key=' + GP.key,  methods=['GET'])
def ping():
    return basic.resp(200, {})


# =====================================================================
# Обмен

# Добавить
@app.route('/warapig/0.1/addhosts&key=' + GP.key,  methods=['POST'])
def add_hosts():
    lock.acquire()
    result = PostGet.addHosts(listHost)
    lock.release()
    return result


@app.route('/warapig/0.1/addhost&key=' + GP.key,  methods=['POST'])
def add_host():
    lock.acquire()
    result = PostGet.addHost(listHost)
    lock.release()
    return result


# Получить
@app.route('/warapig/0.1/hosts&key=' + GP.key,  methods=['GET'])
def get_hosts():
    tmp_hosts = copy.deepcopy(listHost)
    return PostGet.getHosts(tmp_hosts)


@app.route('/warapig/0.1/host/<host>&key=' + GP.key,  methods=['GET'])
def get_host(host):
    tmp_hosts = copy.deepcopy(listHost)
    return PostGet.getHost(tmp_hosts, str(host))


# Очистка
@app.route('/warapig/0.1/clear&key=' + GP.key,  methods=['GET'])
def clear():
    lock.acquire()
    listHost.clear()
    lock.release()
    return basic.resp(200, {})


# =====================================================================
# Старт
def runFlask():
    app.debug = True
    app.run(host=GP.hostFlask, port=GP.portFlask)


def searchGitAndSVN():
    while True:
        lock.acquire()
        GandS.update(listHost)
        lock.release()
        time.sleep(GP.timeSleepUpdate)

if __name__ == "__main__":
    runUpdate = threading.Thread(target=searchGitAndSVN)

    runUpdate.setDaemon(True)

    runUpdate.start()
    runFlask()

    runUpdate.join()


