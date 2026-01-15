class Bank:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]):
        arg_ihhe.balance = arg_xdvx

    def func_hqta(arg_ihhe, arg_rgwu: var_bacg, arg_wrnh: var_bacg,
        arg_osiz: var_bacg) ->var_wnki:
        if arg_rgwu > var_ayzf(arg_ihhe.balance) or arg_wrnh > var_ayzf(
            arg_ihhe.balance) or arg_ihhe.balance[arg_rgwu - 1] < arg_osiz:
            return False
        arg_ihhe.balance[arg_rgwu - 1] -= arg_osiz
        arg_ihhe.balance[arg_wrnh - 1] += arg_osiz
        return True

    def func_egyk(arg_ihhe, arg_dcmd: var_bacg, arg_osiz: var_bacg) ->var_wnki:
        if arg_dcmd > var_ayzf(arg_ihhe.balance):
            return False
        arg_ihhe.balance[arg_dcmd - 1] += arg_osiz
        return True

    def func_llti(arg_ihhe, arg_dcmd: var_bacg, arg_osiz: var_bacg) ->var_wnki:
        if arg_dcmd > var_ayzf(arg_ihhe.balance) or arg_ihhe.balance[
            arg_dcmd - 1] < arg_osiz:
            return False
        arg_ihhe.balance[arg_dcmd - 1] -= arg_osiz
        return True
