class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_hqta:
        return arg_ihhe.delete_similar_ends(arg_xdvx, 0, var_bacg(arg_xdvx) - 1
            )

    def func_rgwu(arg_ihhe, arg_xdvx: var_rcsn, arg_wrnh: var_hqta,
        arg_osiz: var_hqta) ->var_hqta:
        if arg_wrnh >= arg_osiz or arg_xdvx[arg_wrnh] != arg_xdvx[arg_osiz]:
            return arg_osiz - arg_wrnh + 1
        else:
            var_ayzf = arg_xdvx[arg_wrnh]
            while arg_wrnh <= arg_osiz and arg_xdvx[arg_wrnh] == var_ayzf:
                arg_wrnh += 1
            while arg_osiz > arg_wrnh and arg_xdvx[arg_osiz] == var_ayzf:
                arg_osiz -= 1
            return arg_ihhe.delete_similar_ends(arg_xdvx, arg_wrnh, arg_osiz)
