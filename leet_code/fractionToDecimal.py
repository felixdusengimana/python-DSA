class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        res = ""
        mp = {}

        rem = numerator % denominator

        while (rem != 0) and (rem not in mp):
            # Store this remainder
            mp[rem] = len(res)

            # Multiply remainder with 10
            rem = rem * 10

            # Append rem / denr to result
            res_part = rem // denominator
            res += str(res_part)

            # Update remainder
            rem = rem % denominator

        if rem == 0:
            div = str(numerator / denominator)
            if div.split(".")[1] == "0":
                div = div.split(".")[0]
                if div== "-0":
                    div = div.replace("-", "")
            return div
        else:
            _add = ""
            index = str([numerator / denominator]).replace("-","").split(".")[1].index(res[mp[rem]:])
            for i in range(0, index):
                _add += str([numerator / denominator]).split(".")[1][i]
            return str(numerator / denominator).split(".")[0] + f".{_add}({res[mp[rem]:]})"


sol = Solution()
print(sol.fractionToDecimal(7, -12))
