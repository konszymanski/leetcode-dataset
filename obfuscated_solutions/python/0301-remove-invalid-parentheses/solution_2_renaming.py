class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        """
        :type s: str
        :rtype: List[str]
        """
        var_rcsn = 0
        var_bacg = 0
        for var_hqta in arg_xdvx:
            if var_hqta == '(':
                var_rcsn += 1
            elif var_hqta == ')':
                var_bacg = var_bacg + 1 if var_rcsn == 0 else var_bacg
                var_rcsn = var_rcsn - 1 if var_rcsn > 0 else var_rcsn
        var_rgwu = {}

        def func_wrnh(arg_xdvx, arg_osiz, arg_ayzf, arg_wnki, arg_egyk,
            arg_dcmd, arg_llti):
            if arg_osiz == var_zbxo(arg_xdvx):
                if arg_egyk == 0 and arg_dcmd == 0:
                    var_rdmc = ''.join(arg_llti)
                    var_rgwu[var_rdmc] = 1
            else:
                if arg_xdvx[arg_osiz] == '(' and arg_egyk > 0 or arg_xdvx[
                    arg_osiz] == ')' and arg_dcmd > 0:
                    func_wrnh(arg_xdvx, arg_osiz + 1, arg_ayzf, arg_wnki, 
                        arg_egyk - (arg_xdvx[arg_osiz] == '('), arg_dcmd -
                        (arg_xdvx[arg_osiz] == ')'), arg_llti)
                arg_llti.append(arg_xdvx[arg_osiz])
                if arg_xdvx[arg_osiz] != '(' and arg_xdvx[arg_osiz] != ')':
                    func_wrnh(arg_xdvx, arg_osiz + 1, arg_ayzf, arg_wnki,
                        arg_egyk, arg_dcmd, arg_llti)
                elif arg_xdvx[arg_osiz] == '(':
                    func_wrnh(arg_xdvx, arg_osiz + 1, arg_ayzf + 1,
                        arg_wnki, arg_egyk, arg_dcmd, arg_llti)
                elif arg_xdvx[arg_osiz] == ')' and arg_ayzf > arg_wnki:
                    func_wrnh(arg_xdvx, arg_osiz + 1, arg_ayzf, arg_wnki + 
                        1, arg_egyk, arg_dcmd, arg_llti)
                arg_llti.pop()
        func_wrnh(arg_xdvx, 0, 0, 0, var_rcsn, var_bacg, [])
        return var_rjut(var_rgwu.keys())
