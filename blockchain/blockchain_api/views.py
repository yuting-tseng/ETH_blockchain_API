from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("home page!")

def node_info(request):
    return HttpResponse("Node Info!")

def block_info(request, block_num):
    return HttpResponse("Block Info! Block number = {}".format(block_num))

def transaction_info(request, transaction_hash):
    return HttpResponse("Transaction Info! Transaction hash = {}".format(transaction_hash))

