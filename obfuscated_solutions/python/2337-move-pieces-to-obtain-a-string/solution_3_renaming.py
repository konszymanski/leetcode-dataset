class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_ayzf:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh, var_osiz = 0, 0
        while var_wrnh < var_hqta or var_osiz < var_hqta:
            while var_wrnh < var_hqta and arg_xdvx[var_wrnh] == '_':
                var_wrnh += 1
            while var_osiz < var_hqta and arg_rcsn[var_osiz] == '_':
                var_osiz += 1
            if var_wrnh == var_hqta or var_osiz == var_hqta:
                return var_wrnh == var_hqta and var_osiz == var_hqta
            if arg_xdvx[var_wrnh] != arg_rcsn[var_osiz] or arg_xdvx[var_wrnh
                ] == 'L' and var_wrnh < var_osiz or arg_xdvx[var_wrnh
                ] == 'R' and var_wrnh > var_osiz:
                return False
            var_wrnh += 1
            var_osiz += 1
        return True
