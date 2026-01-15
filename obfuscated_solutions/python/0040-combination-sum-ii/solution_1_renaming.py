class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_bacg[var_hqta]]:

        def func_rgwu(arg_wrnh, arg_osiz, arg_xdvx, arg_ayzf, arg_wnki):
            if arg_ayzf < 0:
                return
            elif arg_ayzf == 0:
                arg_wrnh.append(arg_osiz.copy())
            else:
                for var_egyk in var_dcmd(arg_wnki, var_llti(arg_xdvx)):
                    if var_egyk > arg_wnki and arg_xdvx[var_egyk] == arg_xdvx[
                        var_egyk - 1]:
                        continue
                    if arg_ayzf < arg_xdvx[var_egyk]:
                        break
                    arg_osiz.append(arg_xdvx[var_egyk])
                    func_rgwu(arg_wrnh, arg_osiz, arg_xdvx, arg_ayzf -
                        arg_xdvx[var_egyk], var_egyk + 1)
                    arg_osiz.pop()
        var_zbxo = []
        arg_xdvx.sort()
        func_rgwu(var_zbxo, [], arg_xdvx, arg_rcsn, 0)
        return var_zbxo
