class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = {var_rgwu.id: var_rgwu for var_rgwu in arg_rcsn}

        def func_wrnh(arg_osiz):
            var_ayzf = var_hqta[arg_osiz]
            return var_ayzf.importance + var_wnki(func_wrnh(arg_osiz) for
                arg_osiz in var_ayzf.subordinates)
        return func_wrnh(arg_bacg)
