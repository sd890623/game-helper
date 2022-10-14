def funcA():
    varA=1
    def funcB():
        # varA+=1
        print(varA)

    funcB()

funcA()
