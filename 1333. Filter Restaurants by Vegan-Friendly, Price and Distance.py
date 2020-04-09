class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        for i in range(len(restaurants)):
            
            if restaurants[i][2] >= veganFriendly:
                if restaurants[i][3] <= maxPrice:
                    if restaurants[i][4] <= maxDistance:
                        ans.append([restaurants[i][0], restaurants[i][1]])
        ans.sort(key = lambda x:(x[1], x[0]), reverse = True)
        ans = [x[0] for x in ans]
        return ans
