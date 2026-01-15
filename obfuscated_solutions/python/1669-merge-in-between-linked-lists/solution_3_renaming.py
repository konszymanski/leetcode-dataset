class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh,
        arg_bacg: var_wrnh, arg_hqta: var_rgwu) ->var_rgwu:

        def func_osiz(arg_ayzf: var_rgwu) ->var_rgwu:
            if arg_ayzf.next is None:
                return arg_ayzf
            return func_osiz(arg_ayzf.next)

        def func_wnki(arg_egyk, arg_dcmd, arg_llti):
            if arg_egyk == arg_rcsn - 1:
                arg_dcmd = arg_llti
            if arg_egyk == arg_bacg:
                arg_dcmd.next = arg_hqta
                var_zbxo = func_osiz(arg_hqta)
                var_zbxo.next = arg_llti.next
                arg_llti.next = None
                return arg_xdvx
            return func_wnki(arg_egyk + 1, arg_dcmd, arg_llti.next)
        return func_wnki(0, None, arg_xdvx)
