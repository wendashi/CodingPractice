class Solutioin():
    def repeat(self, s: str):
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0 and s[:i] * (n//i) == s[:] :
                return True
        
        return False

sol = Solutioin()
res = sol.repeat(s = "abab")
print(res)