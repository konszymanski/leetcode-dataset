class LFUCache:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.cap = arg_xdvx
        arg_ihhe.key2val = {}
        arg_ihhe.key2freq = {}
        arg_ihhe.freq2key = var_bacg.defaultdict(var_bacg.OrderedDict)
        arg_ihhe.minf = 0

    def func_hqta(arg_ihhe, arg_rgwu: var_rcsn) ->var_rcsn:
        if arg_rgwu not in arg_ihhe.key2val:
            return -1
        var_wrnh = arg_ihhe.key2freq[arg_rgwu]
        arg_ihhe.key2freq[arg_rgwu] = var_wrnh + 1
        arg_ihhe.freq2key[var_wrnh].pop(arg_rgwu)
        if not arg_ihhe.freq2key[var_wrnh]:
            del arg_ihhe.freq2key[var_wrnh]
        arg_ihhe.freq2key[var_wrnh + 1][arg_rgwu] = 1
        if arg_ihhe.minf not in arg_ihhe.freq2key:
            arg_ihhe.minf += 1
        return arg_ihhe.key2val[arg_rgwu]

    def func_osiz(arg_ihhe, arg_rgwu: var_rcsn, arg_ayzf: var_rcsn) ->None:
        if arg_ihhe.cap <= 0:
            return
        if arg_rgwu in arg_ihhe.key2val:
            arg_ihhe.get(arg_rgwu)
            arg_ihhe.key2val[arg_rgwu] = arg_ayzf
            return
        if var_wnki(arg_ihhe.key2val) == arg_ihhe.cap:
            var_egyk, var_dcmd = arg_ihhe.freq2key[arg_ihhe.minf].popitem(last
                =False)
            del arg_ihhe.key2val[var_egyk]
            del arg_ihhe.key2freq[var_egyk]
        arg_ihhe.key2val[arg_rgwu] = arg_ayzf
        arg_ihhe.key2freq[arg_rgwu] = 1
        arg_ihhe.freq2key[1][arg_rgwu] = 1
        arg_ihhe.minf = 1
