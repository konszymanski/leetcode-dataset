class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_bacg:
        arg_rcsn.sort()
        var_rgwu = var_wrnh(arg_rcsn[:-arg_xdvx])
        var_osiz = arg_rcsn[-arg_xdvx:]
        for var_ayzf in var_wnki(arg_xdvx - 1):
            if var_rgwu // (var_ayzf + 1) < var_osiz[var_ayzf + 1] - var_osiz[
                var_ayzf]:
                return var_osiz[var_ayzf] + var_rgwu // (var_ayzf + 1)
            var_rgwu -= (var_ayzf + 1) * (var_osiz[var_ayzf + 1] - var_osiz
                [var_ayzf])
        return var_osiz[-1] + var_rgwu // arg_xdvx
