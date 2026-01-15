class DSU:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.N = arg_xdvx
        arg_ihhe.size = [1] * arg_xdvx
        arg_ihhe.representative = var_rcsn(var_bacg(arg_xdvx))

    def func_hqta(arg_ihhe, arg_rgwu):
        if arg_ihhe.representative[arg_rgwu] == arg_rgwu:
            return arg_rgwu
        arg_ihhe.representative[arg_rgwu] = arg_ihhe._find(arg_ihhe.
            representative[arg_rgwu])
        return arg_ihhe.representative[arg_rgwu]

    def func_wrnh(arg_ihhe, arg_osiz, arg_ayzf):
        arg_osiz = arg_ihhe._find(arg_osiz)
        arg_ayzf = arg_ihhe._find(arg_ayzf)
        if arg_osiz == arg_ayzf:
            return False
        else:
            if arg_ihhe.size[arg_osiz] > arg_ihhe.size[arg_ayzf]:
                arg_ihhe.representative[arg_ayzf] = arg_osiz
                arg_ihhe.size[arg_osiz] += arg_ihhe.size[arg_ayzf]
            else:
                arg_ihhe.representative[arg_osiz] = arg_ayzf
                arg_ihhe.size[arg_ayzf] += arg_ihhe.size[arg_osiz]
            return True


class Solution:

    def func_wnki(arg_ihhe, arg_egyk):
        arg_xdvx = var_dcmd(arg_egyk)
        var_llti = var_zbxo(arg_xdvx)
        for var_rdmc in arg_egyk:
            if not var_llti._do_union(var_rdmc[0] - 1, var_rdmc[1] - 1):
                return var_rdmc
        return []
