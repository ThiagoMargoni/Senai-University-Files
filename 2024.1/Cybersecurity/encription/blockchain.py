import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Cria o bloco de gênese
        self.new_block(previous_hash='1', proof=100)


    def new_block(self, proof, previous_hash=None):
        """
        Cria um novo bloco na blockchain

        :param proof: Prova fornecida pelo algoritmo de Prova de Trabalho (Proof of Work)
        :param previous_hash: Hash do bloco anterior
        :return: Novo bloco
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
    def new_block(self, proof, previous_hash=None):
        """
        Cria um novo bloco na blockchain

        :param proof: Prova fornecida pelo algoritmo de Prova de Trabalho (Proof of Work)
        :param previous_hash: Hash do bloco anterior
        :return: Novo bloco
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

    # Reinicia a lista de transações atuais
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adiciona uma nova transação à lista de transações

        :param sender: Endereço do remetente
        :param recipient: Endereço do destinatário
        :param amount: Quantidade enviada
        :return: Índice do bloco que irá armazenar esta transação, geralmente o próximo bloco a ser minerado
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1
    @staticmethod
    def hash(block):
        """
        Gera um hash SHA-256 de um bloco

        :param block: Bloco
        :return: String contendo o hash
        """

        # Certifica-se de que o dicionário está ordenado para garantir a consistência do hash
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
# Exemplo de uso
blockchain = Blockchain()

# Adiciona uma nova transação
blockchain.new_transaction('Alice', 'Bob', 5)

# Minerar um novo bloco
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = 12345  # A prova seria normalmente derivada através de um processo de mineração
previous_hash = blockchain.hash(last_block)
blockchain.new_block(proof, previous_hash)

# Adicionar mais uma transação
blockchain.new_transaction('Bob', 'Charlie', 3)

# Minerar um outro bloco
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = 67890  # Outra prova fictícia para demonstração
previous_hash = blockchain.hash(last_block)
blockchain.new_block(proof, previous_hash)

# Exibir a blockchain
print(json.dumps(blockchain.chain, indent=2))