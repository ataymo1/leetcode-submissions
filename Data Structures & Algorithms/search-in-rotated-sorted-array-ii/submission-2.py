class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L + R) // 2
            l_e, r_e, m_e = nums[L], nums[R], nums[M]
            print(nums[L:R+1])
            if m_e == target:
                return True
            elif l_e <= m_e:
                if l_e == target:
                    return True
                elif l_e == m_e:
                    L += 1
                elif l_e < target < m_e:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if r_e == target:
                    return True
                elif r_e == target:
                    R -= 1
                elif m_e < target < r_e:
                    L = M + 1
                else:
                    R = M - 1
        
        return False
