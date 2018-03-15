from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from ratelimit.decorators import ratelimit


from web3 import Web3, HTTPProvider, IPCProvider 
import json


web3 = Web3(HTTPProvider('http://localhost:8545'))


## main views class

class MainView(View):
    """
        default API
    """
    def __init__(self):
        self.page = ''
        self.keylist = [] # JSON keys that would be return

    @ratelimit(key='ip', method='GET')
    def get(self, request, *args, **kwargs):
        return JsonResponse({'Default': '{} GET.'.format(self.page)})

    @ratelimit(key='ip', method='POST')
    def post(self, request, *args, **kwargs):
        """ send ethereum transaction to blockchain.
            Reference JSON RPC API: Eth.sendTransaction(transaction).
        """

        tx_args= json.loads(request.body.decode("utf-8"))
        gas = (tx_args['gas'] or 90000)
        res = {'to': tx_args['to'], 'from': web3.eth.coinbase, 'value': tx_args['value'], 'gas': gas}

        try:
            web3.eth.sendTransaction(res)
        except:
            raise Exception()

        return JsonResponse(res)

    @ratelimit(key='ip', method='PUT')
    def put(self, request, *args, **kwargs):
        """ turn on miner.
            Reference JSON RPC API: miner.start(1).
        """
        web3.miner.start(1) # start CPU mining
        result = {'Mining': "Start CPU mining proccess using 1 thread."}
        return JsonResponse(result)

    @ratelimit(key='ip', method='DELETE')
    def delete(self, request, *args, **kwargs):
        """ turn off miner.
            Reference JSON RPC API: miner.stop().
        """
        web3.miner.stop() # stop CPU mining
        result = {'Mining': "Stop CPU mining proccess"}
        return JsonResponse(result)

## views subclass

class HomeView(MainView):
    """ Home Page
    """
    def __init__(self):
        self.page = 'Home'

class NodeInfo(MainView):
    """ get node information
        Reference JSON RPC API: admin.nodeInfo()

        input:
            None
        return:
            result(JSON)
    """
    def __init__(self):
        self.page = 'NodeInfo'
        self.keylist = ['enode', 'name']
    
    @ratelimit(key='ip', method='GET')
    def get(self, request):
        node = web3.admin.nodeInfo  # get node info from blockchain
        result = dict((k, node[k]) for k in self.keylist)
        return JsonResponse(result)

class BlockInfo(MainView):
    """ get node information
        Reference JSON RPC API: eth.getBlock(block_num)

        input:
            block_num(str)
        return:
            result(JSON)
    """
    def __init__(self):
        self.page = 'BlockInfo' 
        self.keylist = ['difficulty', 'gasLimit', 'gasUsed', 'hash', 'miner', 'parentHash', 'totalDifficulty']

    @ratelimit(key='ip', method='GET')
    def get(self, request, block_num):
        block_num = int(block_num)  # str to int
        block = web3.eth.getBlock(block_num) # get block info from blockchain
        result = dict((k, block[k]) for k in self.keylist)
        return JsonResponse(result)

class TxInfo(MainView):
    """ get transaction information
        Reference JSON RPC API: eth.getTransaction(transaction_hash)

        input:
            transaction_hash(str)
        return:
            result(JSON)
    """
    def __init__(self):
        self.page = 'BlockInfo' 
        self.keylist = ['blockHash', 'blockNumber', 'from', 'gas', 'gasPrice', 'hash', 'nonce', 'to', 'value']
         
    @ratelimit(key='ip', method='GET')
    def get(self, request, transaction_hash):
        # get transaction info from blockchain
        tx = web3.eth.getTransaction(transaction_hash) 
        result = dict((k, tx[k]) for k in self.keylist)
        return JsonResponse(result)


## Error handling

def page_not_found(request):    # http status 404 handler 
    result = {'Error': 'The requested URL was not found on this server.'}
    return JsonResponse(result)

def server_error(request):      # http status 500 handler
    result = {'Error': 'Internal Server Error.'}
    return JsonResponse(result)

def forbidden(request):         # http status 403 handler
    result = {'Error': 'Forbidden.'}
    return JsonResponse(result)

def bad_request(request):       # http status 400 handler
    result = {'Error': 'Bad Request.'}
    return JsonResponse(result)
