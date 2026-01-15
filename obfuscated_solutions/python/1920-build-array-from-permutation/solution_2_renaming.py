class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        for var_wrnh in var_osiz(var_hqta):
            arg_xdvx[var_wrnh] += 1000 * (arg_xdvx[arg_xdvx[var_wrnh]] % 1000)
        for var_wrnh in var_osiz(var_hqta):
            arg_xdvx[var_wrnh] //= 1000
        return arg_xdvx
