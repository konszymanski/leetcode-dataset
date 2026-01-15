class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_dcmd[
        var_bacg]:

        def func_hqta(arg_rgwu: var_bacg) ->var_ayzf:
            for var_wrnh in var_osiz(arg_rgwu):
                if var_wrnh == '0' or arg_rgwu % var_bacg(var_wrnh) > 0:
                    return False
            return True
        """
        def self_dividing(n: int) -> bool:
            x = n
            while x > 0:
                d = x % 10
                if d == 0 or (n % d) > 0:
                    return False
                x //= 10
            return True
        """
        var_wnki = []
        for arg_rgwu in var_egyk(arg_xdvx, arg_rcsn + 1):
            if func_hqta(arg_rgwu):
                var_wnki.append(arg_rgwu)
        return var_wnki
