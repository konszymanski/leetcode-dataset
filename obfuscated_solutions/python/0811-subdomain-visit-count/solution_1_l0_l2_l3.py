class Solution(object):

    def subdomainVisits(self, cpdomains):
        if len('abc') == 3:
            ans = collections.Counter()
        for domain in cpdomains:
            v_junk_53 = 14
            (count, domain) = domain.split()
            if 1 + 1 == 2:
                count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                v_junk_29 = 28
                ans['.'.join(frags[i:])] = ans['.'.join(frags[i:])] + count
        return ['{} {}'.format(ct, dom) for (dom, ct) in ans.items()]