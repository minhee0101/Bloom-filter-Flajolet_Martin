import math
import mmh3
import random


class BloomFilter:
    def __init__(self,capacity,fp_prob): #capacity = m,fp_brob = false positive 비율
        self.capacity = capacity #언제쓸지 모르니까 인스턴스에 멤버변수로 넣어주기
        self.fp_prob = fp_prob
        self.bitarray = 0
        self.n_bits = math.ceil(-math.log(fp_prob,math.e)*capacity/(math.log(2,math.e)**2)) #bitarray 크기인듯?
        self.n_hashs = int(self.n_bits / capacity* math.log(2,math.e)) #hash 개수
        #print(self.n_bits)
        #print(self.n_hashs)
        self.seeds = [random.randint(0,999999) for i in range(self.n_hashs)]

    def put(self,item):
        for i in range(self.n_hashs): #hash 개수 만큼 해시를 돌림
            pos = mmh3.hash(item,self.seeds[i]) % self.n_bits
            self.bitarray |= (1<<pos) #bitarray에다가 set , 1에서 pos만큼 shift시켜서 #그럼 해당위치에 set됩니당.

    def test(self,item): #item이 들어왔을때 그 item을 hash를 해서 pos를 구하고 해당 pos가 전부 다 1이면 있을수도 있다~
        for i in range(self.n_hashs): 
            pos = mmh3.hash(item,self.seeds[i]) % self.n_bits
            
            if self.bitarray & (1<<pos) == 0: #이게 true면 0, false면 1
                return False
        return True

bloom = BloomFilter(10, 0.1)

bloom.put('a')
bloom.put('b')
bloom.put('c')
bloom.put('d')
bloom.put('e')

print('a',bloom.test('a'))
print('b',bloom.test('b'))
print('c',bloom.test('c'))
print('d',bloom.test('d'))
print('e',bloom.test('e'))
print('f',bloom.test('f'))
print('g',bloom.test('g'))
print('h',bloom.test('h'))
print('i',bloom.test('i'))
print('j',bloom.test('j'))
print('k',bloom.test('k'))
print('l',bloom.test('l'))
print('m',bloom.test('m'))
print('n',bloom.test('n'))







