# Break statement-Exits an entire loop

num= 20
while num <= 25:
   print(num)
   if num== 23:
    break
   num += 1

   #Continue statement- Skips elements in a loop
   devices=["Laptop","Phone", "Tablet"]
   for dev in devices:
       if dev=="Phone":
           continue
       print(dev)
