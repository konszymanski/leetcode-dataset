class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        n = len(dist)                                                       #    Ex: dist = [1,5,4,4,3]
                                                                            #       speed = [1,2,1,1,1]
        time = sorted(map(lambda x: int(ceil(x[0]/x[1])),zip(dist,speed)))  #
                                                                            #  time: sorted([1,3,4,4,3])        
        for i in range(n):                                                  #             = [1,3,3,4,4]    
            if i >= time[i]: return i                                       #            i:  0 1 2 3 4
                                                                            #                        |   
        return n                                                            #                    return 4