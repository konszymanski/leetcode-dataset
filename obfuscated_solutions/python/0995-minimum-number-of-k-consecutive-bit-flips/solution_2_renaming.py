class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf.deque()
        var_wnki = 0
        var_egyk = 0
        for var_dcmd, var_llti in var_zbxo(arg_xdvx):
            if var_dcmd >= arg_rcsn:
                var_wnki ^= var_osiz[0]
            if var_wnki == arg_xdvx[var_dcmd]:
                if var_dcmd + arg_rcsn > var_rgwu:
                    return -1
                var_osiz.append(1)
                var_wnki ^= 1
                var_egyk += 1
            else:
                var_osiz.append(0)
            if var_wrnh(var_osiz) > arg_rcsn:
                var_osiz.popleft()
        return var_egyk
