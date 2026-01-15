class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_rcsn)

        def func_osiz(arg_ayzf):
            if var_hqta % arg_ayzf or var_rgwu % arg_ayzf:
                return False
            var_wnki, var_egyk = var_hqta // arg_ayzf, var_rgwu // arg_ayzf
            var_dcmd = arg_xdvx[:arg_ayzf]
            return (arg_xdvx == var_wnki * var_dcmd and arg_rcsn == 
                var_egyk * var_dcmd)
        for var_llti in var_zbxo(var_rdmc(var_hqta, var_rgwu), 0, -1):
            if func_osiz(var_llti):
                return arg_xdvx[:var_llti]
        return ''
