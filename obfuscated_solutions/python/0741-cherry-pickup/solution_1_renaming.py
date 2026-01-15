class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):

        def func_bacg(arg_rcsn):
            var_hqta = var_rgwu(arg_rcsn)
            var_wrnh = var_osiz('-inf')
            var_ayzf = [([var_wrnh] * var_hqta) for var_wnki in var_egyk(
                var_hqta)]
            var_ayzf[-1][-1] = arg_rcsn[-1][-1]
            for var_dcmd in var_egyk(var_hqta - 1, -1, -1):
                for var_llti in var_egyk(var_hqta - 1, -1, -1):
                    if arg_rcsn[var_dcmd][var_llti] >= 0 and (var_dcmd != 
                        var_hqta - 1 or var_llti != var_hqta - 1):
                        var_ayzf[var_dcmd][var_llti] = var_zbxo(var_ayzf[
                            var_dcmd + 1][var_llti] if var_dcmd + 1 <
                            var_hqta else var_wrnh, var_ayzf[var_dcmd][
                            var_llti + 1] if var_llti + 1 < var_hqta else
                            var_wrnh)
                        var_ayzf[var_dcmd][var_llti] += arg_rcsn[var_dcmd][
                            var_llti]
            if var_ayzf[0][0] < 0:
                return None
            var_rdmc = [(0, 0)]
            var_dcmd = var_llti = 0
            while var_dcmd != var_hqta - 1 or var_llti != var_hqta - 1:
                if (var_llti + 1 == var_hqta or var_dcmd + 1 < var_hqta and
                    var_ayzf[var_dcmd + 1][var_llti] >= var_ayzf[var_dcmd][
                    var_llti + 1]):
                    var_dcmd += 1
                else:
                    var_llti += 1
                var_rdmc.append((var_dcmd, var_llti))
            return var_rdmc
        var_rdmc = 0
        var_rjut = func_bacg(arg_rcsn)
        if var_rjut is None:
            return 0
        for var_dcmd, var_llti in var_rjut:
            var_rdmc += arg_rcsn[var_dcmd][var_llti]
            arg_rcsn[var_dcmd][var_llti] = 0
        for var_dcmd, var_llti in func_bacg(arg_rcsn):
            var_rdmc += arg_rcsn[var_dcmd][var_llti]
        return var_rdmc
