def CountDD(n):
    count=0
    while n!=0:
        n//=10
        count+=1
    return count
def Amstrong(n):
    tem=n
    sum=0
    power=CountDD(n)
    while n!=0:
        rem=n%10
        sum=(sum+rem**power)
        n//=10
    if tem==sum:
        return True
    else:
        return False
n=int(input('enter  a number'))            
float=Amstrong(n)
if float==True:
    print('amstumg')
else:
    print('not a amstrong number')    