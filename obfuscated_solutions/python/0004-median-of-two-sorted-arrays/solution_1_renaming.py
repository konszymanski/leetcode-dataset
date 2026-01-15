class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_rdmc:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_rcsn)
        var_ayzf, var_wnki = 0, 0

        def func_egyk():
            nonlocal p1, p2
            if var_ayzf < var_rgwu and var_wnki < var_wrnh:
                if arg_xdvx[var_ayzf] < arg_rcsn[var_wnki]:
                    var_dcmd = arg_xdvx[var_ayzf]
                    var_ayzf += 1
                else:
                    var_dcmd = arg_rcsn[var_wnki]
                    var_wnki += 1
            elif var_wnki == var_wrnh:
                var_dcmd = arg_xdvx[var_ayzf]
                var_ayzf += 1
            else:
                var_dcmd = arg_rcsn[var_wnki]
                var_wnki += 1
            return var_dcmd
        if (var_rgwu + var_wrnh) % 2 == 0:
            for var_llti in var_zbxo((var_rgwu + var_wrnh) // 2 - 1):
                var_llti = func_egyk()
            return (func_egyk() + func_egyk()) / 2
        else:
            for var_llti in var_zbxo((var_rgwu + var_wrnh) // 2):
                var_llti = func_egyk()
            return func_egyk()
