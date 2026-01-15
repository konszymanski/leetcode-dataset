class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:

        def func_bacg(arg_hqta, arg_rgwu):
            var_wrnh = arg_hqta
            var_osiz = arg_rgwu - 1
            while var_wrnh < var_osiz:
                if arg_xdvx[var_wrnh] != arg_xdvx[var_osiz]:
                    return False
                var_wrnh += 1
                var_osiz -= 1
            return True
        for var_ayzf in var_wnki(var_egyk(arg_xdvx), 0, -1):
            for var_dcmd in var_wnki(var_egyk(arg_xdvx) - var_ayzf + 1):
                if func_bacg(var_dcmd, var_dcmd + var_ayzf):
                    return arg_xdvx[var_dcmd:var_dcmd + var_ayzf]
        return ''
