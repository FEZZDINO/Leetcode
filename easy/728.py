        def dimo(num1):
            num = num1
            out = []
            while num != 0:
                num, mo = divmod(num,10)
                out.append(mo)
                if mo ==0:
                    return False
            #print(num1, out)
            for i in out:
                
                if num1 %i ==0:
                    continue

                return False
            return True
            
        output = []
        for i in range(left,right+1):
            if dimo(i):
                output.append(i)
        return output