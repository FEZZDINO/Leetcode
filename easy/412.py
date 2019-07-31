class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = ["1"]
        for i in range(2,n+1):
            
            if i %15 == 0:
                output.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                output.append("Fizz")
                continue
            elif i % 5 == 0:
                output.append("Buzz")
                continue
            output.append("%d" % i)
        return output