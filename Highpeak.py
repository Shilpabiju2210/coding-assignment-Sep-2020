#open input file to read input
in_file =open("sample_input.txt","r")
#open output file to write output
out_file = open("sample_output.txt","w+")
goodies={}
out_list=[]

#reading input file 
for f in in_file:
    toRead_index_price=f.index(":")
    print(f[toRead_index_price+1:].strip())
    print(f[:toRead_index_price])
    goodies[f[:toRead_index_price]]=f[toRead_index_price+1:].strip()
print(goodies) 
prices_goodie=list(goodies.values())
prices_goodie=[int(i)for i in prices_goodie]

#sorted list in decsending order to get prices to be distributed in order
prices_goodie.sort(reverse=True)
print(prices_goodie)
#taking inputs
num_of_employees=int(input("Enter number of employees: "))
len_considered=(len(prices_goodie)-num_of_employees)
print(len_considered)


#finding minimum difference between highest and lowest
for i in range(len_considered):
    max_price=prices_goodie[i]
    min_price=prices_goodie[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        index_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        index_choosen=i

choosen_prices=prices_goodie[index_choosen:num_of_employees+index_choosen]
#differnce between high price and low price
diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

cnt=0
for key,value in goodies.items():
    prices_goodie[cnt]
    print(value)
    if int(value)in choosen_prices and cnt<num_of_employees:
        str1=key+" : "+value
        #preparing  list for output
        out_list.append(str1)
        cnt+=1
        print(str1)
#writing to output file
out_file.write("The goodies selected for distribution are: \n")
out_file.write("\n")
for i in out_list:
    out_file.write(i)
    out_file.write("\n")
out_file.write("\n And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))
in_file.close()
out_file.close()
