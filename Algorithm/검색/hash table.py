hash_table = [ 0 for _ in range(10)]

# 해쉬 함수 -> 가장 기본적인 Division 법(나누기를 통한 나머지 값을 사용하는 기법)
def hash_func(key):
    return key%5

# 데이타
data1 = 'Andy'
data2 = "Dave"
data3 = "Trump"

# ord() : 문자의 ASCII코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]),hash_func(ord(data1[0])))

# 해쉬 테이블에 저장
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy','0105553333')
storage_data('Dave','0105554444')
storage_data('Trump','01022223333')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))


##################################################################################
hash_table = [ 0 for _ in range(10)]
hash_address = hash('Dave') % 8
hash_table[hash_address] = '01044797388'
print(hash_table)

###################################################################################
# 충돌 해결 알고리즘

# 1. Chaining 기법 - Opening hashing - Linked List
hash_table = [ 0 for _ in range(10)]
def storage(data, value):
    index_key = hash(data)
    hash_address = index_key % 8
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key,value]]

def read(data):
    index_key = hash(data)
    hash_address = index_key % 8
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return "None"
    else:
        return "None"

print(hash('Dd')%8, hash('data')%8)

data = 'Dl'
value = '01044797399'
storage(data, value)
data = 'Data'
value = '01033333333'
storage(data,value)
print(hash_table)
print(read(data))