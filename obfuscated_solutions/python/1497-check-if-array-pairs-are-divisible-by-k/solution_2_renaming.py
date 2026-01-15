class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_egyk:
        arg_xdvx = var_rgwu(arg_xdvx, key=lambda x: (arg_rcsn + var_wrnh %
            arg_rcsn) % arg_rcsn)
        var_osiz = 0
        var_ayzf = var_wnki(arg_xdvx) - 1
        while var_osiz < var_ayzf:
            if arg_xdvx[var_osiz] % arg_rcsn != 0:
                break
            if arg_xdvx[var_osiz + 1] % arg_rcsn != 0:
                return False
            var_osiz = var_osiz + 2
        while var_osiz < var_ayzf:
            if (arg_xdvx[var_osiz] + arg_xdvx[var_ayzf]) % arg_rcsn != 0:
                return False
            var_osiz += 1
            var_ayzf -= 1
        return True
