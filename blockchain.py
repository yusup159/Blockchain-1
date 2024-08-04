import sys
import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask
from flask.globals import request
from flask.json import jsonify
import requests
from urllib.parse import urlparse


class Blockchain(object):
    tingkat_kesulitan = "0000"

    def hashblock(self, block):
        block_encode= json.dumps(block, short_keys=True).encode()
        return hashlib.sha256(block_encode).hexdigest()
    
    def __init__(self):
        self.chain =[]
        self.current_tran=[]

        genesis_hash =self.hashblock("hash block pertama")

        self.append_block(
            hash_of_previous_block = genesis_hash,
            nounce = self.proof_of_work(0, genesis_hash, [])
        )

    def proof_of_work(self, index, hash_of_previous_block, tran, nounce):
        nounce = 0

        while self.valid_proof( index, hash_of_previous_block, tran, nounce) is False:
            nounce += 1
            return nounce
        
    def valid_proof(self, index, hash_of_previous_block, tran, nounce):
        content = f'{index}{hash_of_previous_block}{tran}{nounce}'.encode()
        
        content_hash = hashlib.sha256(content).hexdigest()
        
        return content_hash[:len(self.tingkat_kesulitan)] == self.tingkat_kesulitan