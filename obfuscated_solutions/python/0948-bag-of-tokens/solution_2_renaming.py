class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn: var_hqta[var_rgwu], arg_bacg: var_rgwu
        ) ->var_rgwu:
        var_wrnh = 0
        arg_rcsn.sort()
        var_osiz = var_ayzf.deque(arg_rcsn)
        while var_osiz:
            if arg_bacg >= var_osiz[0]:
                arg_bacg -= var_osiz.popleft()
                var_wrnh += 1
            elif var_wnki(var_osiz) > 2 and var_wrnh > 0:
                arg_bacg += var_osiz.pop()
                var_wrnh -= 1
            else:
                return var_wrnh
        return var_wrnh
