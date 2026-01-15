class Solution:

    def func_udax(arg_ihhe, arg_xdvx: 'str', arg_rcsn: 'int') ->'List[str]':
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = []

        def func_wrnh(arg_osiz, arg_ayzf, arg_wnki, arg_egyk, arg_dcmd):
            if arg_osiz == var_bacg:
                if arg_egyk == arg_rcsn and arg_wnki == 0:
                    var_rgwu.append(''.join(arg_dcmd[1:]))
                return
            arg_wnki = arg_wnki * 10 + var_llti(arg_xdvx[arg_osiz])
            var_zbxo = var_rdmc(arg_wnki)
            if arg_wnki > 0:
                func_wrnh(arg_osiz + 1, arg_ayzf, arg_wnki, arg_egyk, arg_dcmd)
            arg_dcmd.append('+')
            arg_dcmd.append(var_zbxo)
            func_wrnh(arg_osiz + 1, arg_wnki, 0, arg_egyk + arg_wnki, arg_dcmd)
            arg_dcmd.pop()
            arg_dcmd.pop()
            if arg_dcmd:
                arg_dcmd.append('-')
                arg_dcmd.append(var_zbxo)
                func_wrnh(arg_osiz + 1, -arg_wnki, 0, arg_egyk - arg_wnki,
                    arg_dcmd)
                arg_dcmd.pop()
                arg_dcmd.pop()
                arg_dcmd.append('*')
                arg_dcmd.append(var_zbxo)
                func_wrnh(arg_osiz + 1, arg_wnki * arg_ayzf, 0, arg_egyk -
                    arg_ayzf + arg_wnki * arg_ayzf, arg_dcmd)
                arg_dcmd.pop()
                arg_dcmd.pop()
        func_wrnh(0, 0, 0, 0, [])
        return var_rgwu
