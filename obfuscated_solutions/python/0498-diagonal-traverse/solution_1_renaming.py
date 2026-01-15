class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        if not arg_xdvx or not arg_xdvx[0]:
            return []
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz, var_ayzf = [], []
        for var_wnki in var_egyk(var_hqta + var_rgwu - 1):
            var_ayzf.clear()
            var_dcmd, var_llti = (0 if var_wnki < var_rgwu else var_wnki -
                var_rgwu + 1, var_wnki if var_wnki < var_rgwu else var_rgwu - 1
                )
            while var_dcmd < var_hqta and var_llti > -1:
                var_ayzf.append(arg_xdvx[var_dcmd][var_llti])
                var_dcmd += 1
                var_llti -= 1
            if var_wnki % 2 == 0:
                var_osiz.extend(var_ayzf[::-1])
            else:
                var_osiz.extend(var_ayzf)
        return var_osiz
