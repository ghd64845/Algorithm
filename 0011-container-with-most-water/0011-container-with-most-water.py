class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        길이 n의 정수 배열 높이가 제공됩니다. i번째 선의 두 끝점이 (i, 0)과 (i, height[i])가 되도록 n개의 수직선이 그려집니다.
        x축과 함께 용기를 형성하는 두 개의 선을 찾아 용기에 가장 많은 물이 포함되도록 하세요.
        컨테이너가 저장할 수 있는 최대 물의 양을 반환합니다.
        용기를 기울일 수는 없습니다.
        '''
        
        l = 0
        r = len(height) -1
        area = 0

        while l < r:
            # Calculating the max area
            area = max(area, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area