func = lambda x : True if ((x[0] == 'a' and x[-1] == 'a') or (x[0] == 'A' and x[-1] == 'A') or
                           (x[0] == 'a' and x[-1] == 'A') or (x[0] == 'A' and x[-1] == 'a')) \
    else False
