class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if left is sorted
        #   if target is in there, search in there
        #   else search right
        # else
        #   if target is in the right half, search in there


        L, R = 0, len(nums) - 1


        while L <= R:
            M = (L + R) // 2
            m_e, l_e, r_e = nums[M], nums[L], nums[R]

            if target == m_e:
                return M
            elif l_e < m_e: # if left half is sorted
                if l_e == target:
                    return L
                elif l_e < target < m_e:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if r_e == target:
                    return R
                elif m_e < target < r_e:
                    L = M + 1
                else:
                    R = M - 1
        return -1
                    

                    








        