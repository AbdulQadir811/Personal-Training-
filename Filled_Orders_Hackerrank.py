def filledOrders(order, k):
    # Write your code here
    order.sort()
    print(order)
    
    s = 0 
    o = 0
    for i in range(0,len(order)):
        s = s + order[i]
        if s <= k :
            o +=1
        else:
            return o
                  
    
    return (len(o))        
              

if __name__ == '__main__':
    print(filledOrders([50,30,40], 2))
