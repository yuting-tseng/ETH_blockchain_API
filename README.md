# Ethereum blockchain API
* * *

## About this project
To provide a set of RESTful API to query Ethereum blockchain information.

## API endpoints

* Node info
`http://127.0.0.1:8000/node`

* Block info
`http://127.0.0.1:8000/block/{block_number}`

* Transaction info
`http://127.0.0.1:8000/transaction/{transation_hash}`


## How to install

```
# download source code
git clone https://github.com/yuting-tseng/ETH_blockchain_API.git
cd ETH_blockchain_API
```

Then, It's recommanded to create a python virtual environment, which allows you to work on a specific project without worry of affecting other projects.
note that: python3 is required.
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

