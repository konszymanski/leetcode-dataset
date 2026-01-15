class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(arg_xdvx)
        for var_ayzf in var_wnki(var_hqta):
            var_egyk = True
            for var_dcmd in var_wnki(var_hqta):
                if arg_xdvx[(var_ayzf + var_dcmd) % var_hqta] != var_wrnh[
                    var_dcmd]:
                    var_egyk = False
                    break
            if var_egyk:
                return True
        return False
