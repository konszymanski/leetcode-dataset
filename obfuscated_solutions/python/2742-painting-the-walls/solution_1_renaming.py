class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:

        @var_zbxo
        def func_rgwu(arg_wrnh, arg_osiz):
            if arg_osiz <= 0:
                return 0
            if arg_wrnh == var_ayzf:
                return var_wnki
            var_egyk = arg_xdvx[arg_wrnh] + func_rgwu(arg_wrnh + 1, 
                arg_osiz - 1 - arg_rcsn[arg_wrnh])
            var_dcmd = func_rgwu(arg_wrnh + 1, arg_osiz)
            return var_llti(var_egyk, var_dcmd)
        var_ayzf = var_rdmc(arg_xdvx)
        return func_rgwu(0, var_ayzf)
