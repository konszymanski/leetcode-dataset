class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wnki:
        var_hqta = 1
        var_rgwu = 0
        var_wrnh = var_osiz(arg_xdvx)
        while var_rgwu < var_wrnh:
            while var_rgwu < var_wrnh and arg_xdvx[var_rgwu] == ' ':
                var_rgwu += 1
                var_hqta += 1
            var_ayzf = 0
            while var_rgwu < var_wrnh and var_ayzf < var_osiz(arg_rcsn
                ) and arg_xdvx[var_rgwu] == arg_rcsn[var_ayzf]:
                var_rgwu += 1
                var_ayzf += 1
            if var_ayzf == var_osiz(arg_rcsn):
                return var_hqta
            while var_rgwu < var_wrnh and arg_xdvx[var_rgwu] != ' ':
                var_rgwu += 1
        return -1
