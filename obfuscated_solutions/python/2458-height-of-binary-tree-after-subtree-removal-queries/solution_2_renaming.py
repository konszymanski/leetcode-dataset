class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_rgwu[var_wrnh]) ->var_rgwu[var_wrnh]:
        var_osiz = {}
        var_ayzf = {}

        def func_wnki(arg_egyk):
            if not arg_egyk:
                return -1
            if arg_egyk in var_ayzf:
                return var_ayzf[arg_egyk]
            var_dcmd = 1 + var_llti(func_wnki(arg_egyk.left), func_wnki(
                arg_egyk.right))
            var_ayzf[arg_egyk] = var_dcmd
            return var_dcmd

        def func_zbxo(arg_egyk, arg_rdmc, arg_rjut):
            if not arg_egyk:
                return
            var_osiz[arg_egyk.val] = arg_rjut
            func_zbxo(arg_egyk.left, arg_rdmc + 1, var_llti(arg_rjut, 
                arg_rdmc + 1 + func_wnki(arg_egyk.right)))
            func_zbxo(arg_egyk.right, arg_rdmc + 1, var_llti(arg_rjut, 
                arg_rdmc + 1 + func_wnki(arg_egyk.left)))
        func_zbxo(arg_xdvx, 0, 0)
        return [var_osiz[var_lsgw] for var_lsgw in arg_rcsn]
