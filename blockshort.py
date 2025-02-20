import hashlib, time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index, self.transactions, self.previous_hash = index, transactions, previous_hash
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.hash = self.compute_hash()

    def compute_hash(self):
        return hashlib.sha256(f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}".encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [Block(0, "Genesis Block", "0")]

    def add_block(self, transactions):
        last_block = self.chain[-1]
        self.chain.append(Block(len(self.chain), transactions, last_block.hash))

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            block, prev_block = self.chain[i], self.chain[i - 1]
            if block.hash != block.compute_hash() or block.previous_hash != prev_block.hash:
                print(f"[WARNING] Block {block.index} is invalid!")
                return False
        print("[SUCCESS] Blockchain is valid.")
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}\nTimestamp: {block.timestamp}\nTransactions: {block.transactions}\nPrev Hash: {block.previous_hash}\nHash: {block.hash}\n" + "-"*40)

if __name__ == "__main__":
    bc = Blockchain()
    for t in ["A pays 5 BTC to B", "B pays 2 BTC to C", "C pays 1 BTC to D"]:
        bc.add_block(t)

    bc.display_chain()
    print("\nChecking blockchain integrity..."); bc.is_chain_valid()

    print("\n[INFO] Tampering with block 1...")
    bc.chain[1].transactions = "Alice pays 100 BTC to Bob"

    print("\nChecking blockchain integrity after tampering...")
    bc.is_chain_valid()
