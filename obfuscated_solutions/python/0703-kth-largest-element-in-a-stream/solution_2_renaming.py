class KthLargest:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]):
        arg_ihhe.min_heap = []
        arg_ihhe.k = arg_xdvx
        for var_rgwu in arg_rcsn:
            arg_ihhe.add(var_rgwu)

    def func_wrnh(arg_ihhe, arg_osiz: var_bacg) ->var_bacg:
        if var_ayzf(arg_ihhe.min_heap) < arg_ihhe.k or arg_ihhe.min_heap[0
            ] < arg_osiz:
            var_wnki.heappush(arg_ihhe.min_heap, arg_osiz)
            if var_ayzf(arg_ihhe.min_heap) > arg_ihhe.k:
                var_wnki.heappop(arg_ihhe.min_heap)
        return arg_ihhe.min_heap[0]
