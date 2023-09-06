from pathlib import Path

class BloomFilter:
    '''
    The BloomFilter classes encompasses a standard 100 bucket bloom filter
    with 3 hashing functions.
    '''
    def __init__(self) -> None:
        self.globalBloomFilter = [0]*100
        self.sum = 0
    
    def getSum(self, file: str) -> None:
        for letter in file:
            self.sum += ord(letter)

    def mod83(self) -> int:
        return self.sum&83
        
    def mod89(self) -> int:
        return self.sum%89

    def mod97(self) -> int:
        return self.sum%97

    def insertBloomFilter(self):
        self.globalBloomFilter[self.mod83()] = self.globalBloomFilter[self.mod89()] = \
          self.globalBloomFilter[self.mod97()] = 1
        
        # print(f"Toggling positions {self.mod83()}, {self.mod89()} and {self.mod97()}")
        self.sum = 0

    def searchBloomFilter(self, file: str) -> int:
        self.getSum(file)
        hash83 = self.mod83()
        hash89 = self.mod89()
        hash97 = self.mod97()
        self.sum = 0

        if self.globalBloomFilter[hash83] and self.globalBloomFilter[hash89] \
          and self.globalBloomFilter[hash97]:
            
            return 2 # Definitely present 
        
        elif self.globalBloomFilter[hash83] + self.globalBloomFilter[hash89] + self.globalBloomFilter[hash97] == 2:
            return 1 # Probabilistic - may or may not be present: chance of FALSE POSITIVES!

        else:
            return 0 # Definitely not present 


