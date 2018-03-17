# Ethereum blockchain API
* * *

## About this project
To provide a set of RESTful API to query Ethereum blockchain information. 
<br /> <br />

## API endpoints

* Node info: `curl -X GET http://127.0.0.1:8000/node/` 
* Block info: `curl -X GET http://127.0.0.1:8000/block/{block_number}` 
* Transaction info: `curl -X GET http://127.0.0.1:8000/transaction/{transation_hash}` 
* Turn on miner: `curl -X PUT http://127.0.0.1:8000/` 
* Turn off miner: `curl -X DELETE http://127.0.0.1:8000/` 
* Send Ethereum transaction: `curl -H "Content-Type: application/json" -X POST -d '{transaction message}' http://127.0.0.1:8000/`
    * transaction message key: `to`, `value`, `gas`

<br /> <br />

## How to install

First, download source code
```
git clone https://github.com/yuting-tseng/ETH_blockchain_API.git
cd ETH_blockchain_API
```

Then, It's recommanded to create a python virtual environment, which allows you to work on a specific project without worry of affecting other projects. <br />
```
virtualenv blockchain_env
source blockchain_env/bin/activate
pip install -r requirement.txt
```

Start the Django server
```
python blockchain/manage.py runserver 0.0.0.0:8000
```

Then, install go-ethereum and start a node on your local machine
> reference: [building ethereum](https://github.com/ethereum/go-ethereum/wiki/Building-Ethereum)

<br />
note that: python3 is required.

