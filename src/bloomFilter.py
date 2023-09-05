from pathlib import Path

class BloomFilter:
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
        
        print(f"Togging positions {self.mod83()}, {self.mod89()} and {self.mod97()}")
        self.sum = 0

    def searchBloomFilter(self, file: str) -> bool:
        self.getSum(file)
        hash83 = self.mod83()
        hash89 = self.mod89()
        hash97 = self.mod97()

        if self.globalBloomFilter[hash83] and self.globalBloomFilter[hash89] \
          and self.globalBloomFilter[hash97]:
            
            return True
        

            
    
bloomFilter = BloomFilter()
bloomFilter.getSum("dinesh.jpg")
bloomFilter.insertBloomFilter()