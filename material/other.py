# coding: utf-8

# import re
import json
import requests

var = [1, 'str', {'key1': 'value1'}]
var_json = json.dumps(var)  # -> "[1, 'str', {'key1': 'value1'}]"
var_ = json.loads(var_json)  # -> [1, 'str', {'key1': 'value1'}]


# ---------------------------------------------------------------------------
# make first request
# http://developer.openstack.org/api-ref-identity-v2.html

auth_url = 'http://10.10.54.62:5000/v2.0'

response = requests.get(auth_url)
print response.status_code, response.text

# ---------------------------------------------------------------------------
# request token by user\pass
params = {
    "auth": {
            "tenantName": "demo",
            "passwordCredentials": {
                "username": "demo",
                "password": "devstack"
            }
        }
}
response = requests.post(auth_url+'/tokens',
                         data=json.dumps(params))
status_code, response_data = response.status_code, response.text
assert status_code == 200

# ---------------------------------------------------------------------------
# make request by token

data = json.loads(response_data)
token_id = data['access']['token']['id']

params = {
    "auth": {
        'token': {
            'id': token_id
        }
    }
}
response = requests.post(auth_url+'/tokens',
                         data=json.dumps(params))

assert response.status_code == 200

# ---------------------------------------------------------------------------
# request all tenants
response = requests.get(auth_url+'/tenants',
                        headers={'X-Auth-Token': token_id})

assert response.status_code == 200
data = json.loads(response.text)
tenants = data['tenants']
assert [t for t in tenants if t.get('name') == 'demo']

# ---------------------------------------------------------------------------
# get servers list
compute_url = 'http://10.10.54.62:8774/v2.1/ed707862390245b2bd9c9fb6d107183e/'

response = requests.get(compute_url+'servers',
                        headers={'X-Auth-Token': token_id})

assert response.status_code == 200

servers = json.loads(response.text).get('servers')
assert servers

server_name = servers[0].get('name')
print server_name

# ---------------------------------------------------------------------------
# get servers list. OpenStack intro

from keystoneclient.client import Client as KeystoneClient
from novaclient.client import Client as NovaClient

keystone_client = KeystoneClient(
    version='2.0',
    auth_url=auth_url,
    tenant_name='demo',
    username='demo',
    password='devstack',
)
assert keystone_client.authenticate()
assert keystone_client.auth_token

auth_token = keystone_client.auth_token

nova_client = NovaClient(
    '3',
    token=auth_token,
    auth_token=auth_token,
    bypass_url=compute_url)

servers = nova_client.servers.list()
servers = nova_client.hypervisors.list()
assert servers

server_name = servers[0].name
print server_name

'''
  284  su -c 'easy_install pip'
  287  pip install requests
  288  pip freeze
  289  pip list
  290  pip freeze
  291  ls ~/work/env/cc/lib/python2.7/site-packages/
  292  ls ~/work/env/cc/lib/python2.7/site-packages/tionix_cloud_control-0.3.2.dev32-py2.7.egg-info/
  293  ll ~/work/env/cc/lib/python2.7/site-packages/tionix_cloud_control-0.3.2.dev32-py2.7.egg-info/
  294  ls -la ~/work/env/cc/lib/python2.7/site-packages/tionix_cloud_control-0.3.2.dev32-py2.7.egg-info/
  295  less ~/work/env/cc/lib/python2.7/site-packages/tionix_cloud_control-0.3.2.dev32-py2.7.egg-info/requires.txt
  296  less ~/work/env/cc/lib/python2.7/site-packages/tionix_cloud_control-0.3.2.dev32-py2.7.egg-info/entry_points.txt
  297  ls -la ~/work/env/cc/lib/python2.7/site-packages/tionix_cloud_control/
  298  ipython
  299  pip install virtualenv
  создание окружения
  300  virtualenv test_env
  301  cd test_env/
  активируем
  303  source test_env/bin/activate
  установка пакета в окружение
  304  pip install requests
  установка удобной утилиты
  pip install virtualenvwrapper

  настройка virtualenvwrapper

  создание окружения
  305  mkvirtualenv test
  отключение окружения
  306  deactivate
  переключение между существующими
  307  workon liberty
'''