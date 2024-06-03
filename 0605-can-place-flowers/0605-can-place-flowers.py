class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n ==0: return True
        cnt = 0
        flowerbed = [0, *flowerbed, 0]
        size = len(flowerbed)
        
        for i in range(1, size - 1):
            right, left = i + 1, i - 1
            if flowerbed[i] == 1:
                continue
            elif flowerbed[right] == 0 and flowerbed[left] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        
        return False