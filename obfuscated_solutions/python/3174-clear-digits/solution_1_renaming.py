class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        arg_xdvx = var_bacg(arg_xdvx)
        var_hqta = 0
        while var_hqta < var_rgwu(arg_xdvx):
            if arg_xdvx[var_hqta].isdigit():
                del arg_xdvx[var_hqta]
                del arg_xdvx[var_hqta - 1]
                var_hqta -= 1
            else:
                var_hqta += 1
        return ''.join(arg_xdvx)
