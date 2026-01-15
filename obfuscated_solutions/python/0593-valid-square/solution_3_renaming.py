class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        return (arg_rcsn[1] - arg_xdvx[1]) * (arg_rcsn[1] - arg_xdvx[1]) + (
            arg_rcsn[0] - arg_xdvx[0]) * (arg_rcsn[0] - arg_xdvx[0])

    def func_bacg(arg_ihhe, arg_xdvx, arg_rcsn, arg_hqta, arg_rgwu):
        return arg_ihhe.dist(arg_xdvx, arg_rcsn) > 0 and arg_ihhe.dist(arg_xdvx
            , arg_hqta) > 0 and arg_ihhe.dist(arg_xdvx, arg_rcsn
            ) == arg_ihhe.dist(arg_rcsn, arg_hqta) and arg_ihhe.dist(arg_rcsn,
            arg_hqta) == arg_ihhe.dist(arg_hqta, arg_rgwu) and arg_ihhe.dist(
            arg_hqta, arg_rgwu) == arg_ihhe.dist(arg_rgwu, arg_xdvx
            ) and arg_ihhe.dist(arg_xdvx, arg_hqta) == arg_ihhe.dist(arg_rcsn,
            arg_rgwu)

    def func_wrnh(arg_ihhe, arg_xdvx, arg_rcsn, arg_hqta, arg_rgwu):
        return arg_ihhe.check(arg_xdvx, arg_rcsn, arg_hqta, arg_rgwu
            ) or arg_ihhe.check(arg_xdvx, arg_hqta, arg_rcsn, arg_rgwu
            ) or arg_ihhe.check(arg_xdvx, arg_rcsn, arg_rgwu, arg_hqta)
