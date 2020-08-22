def recur_fibo(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  return(recur_fibo(num-1) + recur_fibo(num-2))

def recur_lucas(n):
  if (n==0):
    return 2
  if (n==1):
    return 1
  return recur_lucas(n-1) + recur_lucas(n-2)

def sum_series(num,n1=0,n2=1):
    if (n1 == 0) and (n2 ==1):
        return recur_fibo(num)
    elif (n1 == 2) and (n2 ==1):
        return recur_lucas(num)
    else:
        return recur_fibo(num) + recur_lucas(n1)