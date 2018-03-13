from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from web3 import Web3, HTTPProvider, IPCProvider 
import json


## helper function
def get_json(target):
    return json.dumps(target, indent=4, sort_keys=True)

web3 = Web3(HTTPProvider('http://localhost:8545'))


## main views

def home(request):
    return HttpResponse("home page!")

def node_info(request):
    # get node info from blockchain
    node = web3.admin.nodeInfo
    # take keys in need
    key_list = ['enode', 'name']
    result = dict((k, node[k]) for k in key_list)
    
    return HttpResponse(get_json(result), content_type="application/json")

def block_info(request, block_num):
    block_num = int(block_num)

    # get block info from blockchain
    block = web3.eth.getBlock(block_num)
    # take keys in need
    key_list = ['difficulty', 'gasLimit', 'gasUsed', 'hash', 'miner', 'parentHash', 'totalDifficulty']
    result = dict((k, block[k]) for k in key_list)

    return HttpResponse(get_json(result), content_type="application/json")

def transaction_info(request, transaction_hash):

    # get transaction info from blockchain
    tx = web3.eth.getTransaction(transaction_hash)
    # take keys in need
    key_list = ['blockHash', 'blockNumber', 'from', 'gas', 'gasPrice', 'hash', 'nonce', 'to', 'value']
    result = dict((k, tx[k]) for k in key_list)

    return HttpResponse(get_json(result), content_type="application/json")


## Error handling
def page_not_found(request):    # http return 404 
    result = {'Error': 'The requested URL was not found on this server.'}
    return HttpResponse(get_json(result), content_type="application/json", status=404)

def server_error(request):      # http return 500
    result = {'Error': 'Internal Server Error.'}
    return HttpResponse(get_json(result), content_type="application/json", status=500)

def forbidden(request):         # http return 403
    result = {'Error': 'Forbidden.'}
    return HttpResponse(get_json(result), content_type="application/json", status=403)

def bad_request(request):       # http return 400
    result = {'Error': 'Bad Request.'}
    return HttpResponse(get_json(result), content_type="application/json", status=400)
