new=list()
def flatten(n):
    for i in n:
        if isinstance(i,list):
            flatten(n)
        else:
            new.append(i)
            