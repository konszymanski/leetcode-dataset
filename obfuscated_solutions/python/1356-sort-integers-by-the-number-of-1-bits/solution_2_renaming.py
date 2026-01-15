class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:

        def func_hqta(arg_rgwu):
            var_wrnh = 1
            var_osiz = 0
            while arg_rgwu:
                if arg_rgwu & var_wrnh:
                    var_osiz += 1
                    arg_rgwu ^= var_wrnh
                var_wrnh <<= 1
            return var_osiz
        arg_xdvx.sort(key=lambda num: (func_hqta(arg_rgwu), arg_rgwu))
        return arg_xdvx
