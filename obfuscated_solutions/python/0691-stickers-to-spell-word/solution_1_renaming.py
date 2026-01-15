class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu.Counter(arg_bacg)
        var_wrnh = [(var_rgwu.Counter(var_osiz) & var_hqta) for var_osiz in
            arg_rcsn]
        for var_ayzf in var_wnki(var_egyk(var_wrnh) - 1, -1, -1):
            if var_dcmd(var_wrnh[var_ayzf] == var_wrnh[var_ayzf] & var_wrnh
                [var_llti] for var_llti in var_wnki(var_egyk(var_wrnh)) if 
                var_ayzf != var_llti):
                var_wrnh.pop(var_ayzf)
        arg_xdvx.best = var_egyk(arg_bacg) + 1

        def func_zbxo(arg_rdmc=0):
            if arg_rdmc >= arg_xdvx.best:
                return
            if not var_wrnh:
                if var_rjut(var_hqta[var_lsgw] <= 0 for var_lsgw in var_hqta):
                    arg_xdvx.best = arg_rdmc
                return
            var_osiz = var_wrnh.pop()
            var_cbvh = var_yjch((var_hqta[var_lsgw] - 1) // var_osiz[
                var_lsgw] + 1 for var_lsgw in var_osiz)
            var_cbvh = var_yjch(var_cbvh, 0)
            for var_dmio in var_osiz:
                var_hqta[var_dmio] -= var_cbvh * var_osiz[var_dmio]
            func_zbxo(arg_rdmc + var_cbvh)
            for var_ayzf in var_wnki(var_cbvh - 1, -1, -1):
                for var_lsgw in var_osiz:
                    var_hqta[var_lsgw] += var_osiz[var_lsgw]
                func_zbxo(arg_rdmc + var_ayzf)
            var_wrnh.append(var_osiz)
        func_zbxo()
        return arg_xdvx.best if arg_xdvx.best <= var_egyk(arg_bacg) else -1
