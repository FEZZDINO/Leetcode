class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        end, odd = divmod(m+n, 2)
        i, j = 0, 0
        counter = 0
        tmp = []
        while i<m and j <n:
            if A[i]<= B[j]:
                tmp.append(A[i])
                i += 1
                
            else:
                tmp.append(B[j])
                j += 1
                
            #print(tmp)
            
            if counter== end and odd:
                return tmp[-1]
            elif counter == end and not odd:
                return sum(tmp[-2:])/2
            counter += 1
        #print(tmp)
        if i ==m:
            while j< n:
                tmp.append(B[j])
                j+=1
                #print(1 )
                if counter== end and odd:
                    return tmp[-1]
                elif counter == end and not odd:
                    #print(tmp,sum(tmp[-2:])//2)
                    #print(counter, end)
                    return sum(tmp[-2:])/2
                counter += 1
            
        elif j == n:
            while i<m:
                tmp.append(A[i])
                i+=1
                if counter== end and odd:
                    return tmp[-1]
                elif counter == end and not odd:
                    return sum(tmp[-2:])/2
                counter += 1   