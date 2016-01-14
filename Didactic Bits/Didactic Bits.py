text = "abbbabaaabbabaaaabbaababaabaaaaaabbaaaababbabbbaabbbaabbabbbabbbabbaabababbbaabaaabaaaaaabbabaababbbaabbaabaaaaaabbaaaababbaabaaabbbabababbabbababbaaabaabbbaabaabbaaaababbbabaaabbaabab"

print "text len = ", len(text)

dic = {}
for c in text:
    if c not in dic:
        dic[c] = 1
    else:
        dic[c] += 1

for c in dic:
    print "%s = %d" % (c, dic[c])
