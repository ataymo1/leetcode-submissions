class Solution:
        # Find Peak
            # if in between r and l
            #   set that side to max
            #   search whatever side is greater
            #   

            # if greater than both
            #   quickly check which side it heads to
        # Check both sorted sides
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        mlength = mountainArr.length()
        L, R = 0, mlength - 1

        peak = (0,0)
        while L <= R:
            M = (L + R) // 2
            l_e, r_e, m_e = mountainArr.get(L), mountainArr.get(R), mountainArr.get(M)
            p_i, p = peak
            if m_e > p:
                peak = (M, m_e)
            if l_e < m_e < r_e:
                L = M + 1
            elif l_e > m_e > r_e:
                R = M - 1
            else:
                if 1 + M < mlength and mountainArr.get(M + 1) > m_e:
                    L = M + 1
                elif M - 1 >= 0 and mountainArr.get(M - 1) > m_e:
                    R = M - 1
                else:
                    break
        print(peak)
        
        L, R = 0, peak[0]

        while L <= R:
            M = (L + R) // 2
            m_e = mountainArr.get(M)

            if m_e == target:
                return M
            elif m_e > target:
                R = M - 1
            else:
                L = M + 1
        L, R = peak[0] + 1, mlength 

        while L <= R:
            
            M = (L + R) // 2
            m_e = mountainArr.get(M)
            if m_e == target:
                return M
            elif m_e > target:
                L = M + 1
            else:
                R = M - 1


        return -1

        