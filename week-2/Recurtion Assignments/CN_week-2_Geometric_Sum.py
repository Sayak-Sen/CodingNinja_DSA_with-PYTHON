def geometric_sum(k):
    if k==0:
        return 1
    else:
        return (1/2)**k+geometric_sum(k-1)
n=int((input("enter a number : ")))
print("%.5f"%(geometric_sum(n)))    