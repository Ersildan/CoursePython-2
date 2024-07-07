s = input()
print(['NO', 'YES'][all([any(map(lambda x: x in 'QWERTYUIOPASDFGHJKLZXCVBNM', s)),
                         any(map(lambda x: x in 'qwertyuiopasdfghjklzxcvbnm', s)),
                         any(map(lambda x: x.isdigit(), s)), len(s) >= 7])]
      )
