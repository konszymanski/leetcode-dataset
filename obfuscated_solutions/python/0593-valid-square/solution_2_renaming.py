class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        return (arg_rcsn[1] - arg_xdvx[1]) * (arg_rcsn[1] - arg_xdvx[1]) + (
            arg_rcsn[0] - arg_xdvx[0]) * (arg_rcsn[0] - arg_xdvx[0])

    def func_bacg(arg_ihhe, arg_xdvx, arg_rcsn, arg_hqta, arg_rgwu):
        var_wrnh = [arg_xdvx, arg_rcsn, arg_hqta, arg_rgwu]
        var_wrnh.sort(key=lambda l: (var_osiz[0], var_osiz[1]))
        return arg_ihhe.dist(var_wrnh[0], var_wrnh[1]) != 0 and arg_ihhe.dist(
            var_wrnh[0], var_wrnh[1]) == arg_ihhe.dist(var_wrnh[1], var_wrnh[3]
            ) and arg_ihhe.dist(var_wrnh[1], var_wrnh[3]) == arg_ihhe.dist(
            var_wrnh[3], var_wrnh[2]) and arg_ihhe.dist(var_wrnh[3],
            var_wrnh[2]) == arg_ihhe.dist(var_wrnh[2], var_wrnh[0]
            ) and arg_ihhe.dist(var_wrnh[0], var_wrnh[3]) == arg_ihhe.dist(
            var_wrnh[1], var_wrnh[2])
