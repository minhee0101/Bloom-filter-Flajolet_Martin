import mmh3
import math
import random
import  matplotlib.pyplot as plt
from tqdm import tqdm

class FM:
    def __init__(self,domain_size):
        self.bitarray = 0
        self.domain_size = domain_size
        self.n_bits = math.ceil(math.log2(domain_size)) #몇개의 bit를 쓸건지?
        self.mask = (1 << self.n_bits) -1 #11111111
        self.seed = random.randint(0,999999)

    def put(self,item): #item들어오면 hash하고 위치찾고 bitarray에서 해당위치 1인애 설정하면 됑
        h = mmh3.hash(item,self.seed) & self.mask #hash 하는 부분??
        #hash하면 000101010010101001010011 이렇게 나오는데
        #n_bits만큼만 봐야하니까 잘라야함 &1111111요론식으로 해서 안볼애들은 다 0으로
        r = 0
        if h == 0 : return
        while (h & (1 << r)) == 0 : r += 1 #1위치 찾기
        self.bitarray |= (1 << r) #bitarray에 r번 위치에다가 1을 셋팅하는ㄴ겨

    def size(self): #2**R
        R = self.n_bits-1
        while self.bitarray & (1 << R) == 0: R -= 1  # bitarray에서 쩰 큰 1이 나오는 곳 찾는거 ,,
        #print(self.bitarray)
        return 2 ** R

fm = FM(1000000)
tset = set() #True set

x = []
y = []


for i in tqdm(range(10000)):
    item = str(random.randint(0, 100000))
    fm.put(item)
    tset.add(item)

    x.append(len(tset))
    y.append(fm.size())

plt.scatter(x,y)
plt.plot(x,x,color='r')
plt.show()
    #print(f"true: {len(tset)}, estimated: {fm.size()}")
