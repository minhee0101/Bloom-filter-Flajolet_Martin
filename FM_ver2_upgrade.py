import mmh3
import math
import random
import  matplotlib.pyplot as plt
from tqdm import tqdm

class FM:
    def __init__(self,domain_size,n_groups):
        self.domain_size = domain_size
        self.n_groups = n_groups
        self.n_bits = math.ceil(math.log2(domain_size)) #몇개의 bit를 쓸건지?
        self.mask = (1 << self.n_bits) -1 #11111111
        self.seed = 10 #해시함수 개수입미당
        self.seeds = [random.randint(0,999999) for i in range(self.seed)]
        self.bitarray = [0 for i in range(self.seed)]

    def put(self,item): #item들어오면 hash하고 위치찾고 bitarray에서 해당위치 1인애 설정하면 됑
        for i in range(self.seed):
            h = (mmh3.hash(item,self.seeds[i]) & self.mask) #hash 하는 부분??
            #hash하면 000101010010101001010011 이렇게 나오는데
            #n_bits만큼만 봐야하니까 잘라야함 &1111111요론식으로 해서 안볼애들은 다 0으로
            r = 0
            if h == 0 : return
            while (h & (1 << r)) == 0 : r += 1
            self.bitarray[i] |= (1 << r) #bitarray에 r번 위치에다가 1을 셋팅하는ㄴ겨

    def size(self): #2**R/Φ
        group = [[] for i in range(self.n_groups)]
        R = 0
        for i in range(self.seed):
            while self.bitarray[i] & (1 << R) != 0: R += 1 #bitarray에서 처음 0이 나오는 곳 찾는거 ,, 그
            group[i%self.n_groups].append(2 ** R / 0.77351)
        jungahng = 0
        for i in group:
            i.sort()
            jungahng += i[len(i)//2]

        return jungahng/self.n_groups

fm = FM(100000,5)
tset = set() #True set

x = []
y = []


for i in tqdm(range(100000)):
    item = str(random.randint(0, 100000))
    fm.put(item)
    tset.add(item)


    x.append(len(tset))
    y.append(fm.size())

plt.scatter(x,y)
plt.plot(x,x,color='r')
plt.show()
    #print(f"true: {len(tset)}, estimated: {fm.size()}")
