class Solution:
    var_udax = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine']
    var_ihhe = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
        'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    var_xdvx = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
        'Seventy', 'Eighty', 'Ninety']

    def func_rcsn(arg_bacg, arg_hqta: var_rgwu) ->var_wrnh:
        if arg_hqta == 0:
            return 'Zero'
        return arg_bacg._convert_to_words(arg_hqta)

    def func_osiz(arg_bacg, arg_hqta: var_rgwu) ->var_wrnh:
        if arg_hqta < 10:
            return arg_bacg.below_ten[arg_hqta]
        if arg_hqta < 20:
            return arg_bacg.below_twenty[arg_hqta - 10]
        if arg_hqta < 100:
            return arg_bacg.below_hundred[arg_hqta // 10] + (' ' + arg_bacg
                ._convert_to_words(arg_hqta % 10) if arg_hqta % 10 != 0 else ''
                )
        if arg_hqta < 1000:
            return arg_bacg._convert_to_words(arg_hqta // 100) + ' Hundred' + (
                ' ' + arg_bacg._convert_to_words(arg_hqta % 100) if 
                arg_hqta % 100 != 0 else '')
        if arg_hqta < 1000000:
            return arg_bacg._convert_to_words(arg_hqta // 1000
                ) + ' Thousand' + (' ' + arg_bacg._convert_to_words(
                arg_hqta % 1000) if arg_hqta % 1000 != 0 else '')
        if arg_hqta < 1000000000:
            return arg_bacg._convert_to_words(arg_hqta // 1000000
                ) + ' Million' + (' ' + arg_bacg._convert_to_words(arg_hqta %
                1000000) if arg_hqta % 1000000 != 0 else '')
        return arg_bacg._convert_to_words(arg_hqta // 1000000000
            ) + ' Billion' + (' ' + arg_bacg._convert_to_words(arg_hqta % 
            1000000000) if arg_hqta % 1000000000 != 0 else '')
