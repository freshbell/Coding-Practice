def solution(cacheSize, cities):
    answer = 0
    cache = []

    for i in range(len(cities)):
        city = cities[i].lower()
        if city not in cache:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
        #print(cache)

    return answer

cacheSize = 2
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize,cities))