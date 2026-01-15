class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_ayzf]:
        var_hqta = var_rgwu()
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            var_wrnh = ((var_wrnh << 1) + var_osiz) % 5
            var_hqta.append(var_wrnh == 0)
        return var_hqta
