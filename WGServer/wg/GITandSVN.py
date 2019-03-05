# Проверка наличия веток и ревизий

import base64
import paramiko

import wg.GlobalParams as GP


def initConnect(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if host.typeAuth == 'key':
        try:
            key = paramiko.RSAKey(data=base64.b64decode(bytes(host.key, encoding='utf-8')))
            ssh.connect(hostname=host.hostname, username=host.hostuser, pkey=host.key())
        except:
            host.setPassword(host.key)

    if host.typeAuth == 'psw':
        try:
            ssh.connect(hostname=host.hostname, username=host.hostuser, password=host.password())
        except:
            host.setPassword(host.hostuser)
            try:
                ssh.connect(hostname=host.hostname, username=host.hostuser, password=host.password())
            except:
                host.activeHost = False
                return host

    searchGit(ssh, host)
    searchSVN(ssh, host)

    ssh.close()

    host.activeHost = True
    return host


def searchGit(ssh, host):
    branch = ''
    revision = ''

    try:
        stdin, stdout, stderr = ssh.exec_command('cd ~/'+GP.projectName+'/ '
                                                 '&& git rev-parse --abbrev-ref HEAD')
        branch = stdout.readlines()[0].rstrip()

        stdin, stdout, stderr = ssh.exec_command('cd ~/'+GP.projectName+'/ '
                                                 '&& git rev-list --count HEAD')
        revision = stdout.readlines()[0].rstrip()
    except:
        host.activeHost = False
        return

    host.branchGit = branch
    host.revisionGit = revision

    return


def searchSVN(ssh, host):
    branch = ''
    revision = ''

    try:
        stdin, stdout, stderr = ssh.exec_command('cd ~/'+GP.projectName+'/ '
                                                 '&& svn info --show-item url')
        branch = stdout.readlines()[0].rstrip()

        stdin, stdout, stderr = ssh.exec_command('cd ~/'+GP.projectName+'/ '
                                                 '&& svn info --show-item revision')
        revision = stdout.readlines()[0].rstrip()
    except:
        host.activeHost = False
        return

    host.branchGit = branch
    host.revisionGit = revision

    return


def update(hosts):
    for host in hosts:
        initConnect(host)
