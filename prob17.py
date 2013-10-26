ones1 = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
ones = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tens = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
teens = { 10:'ten', 11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

def num_2_words(n):
  a = str(n)
  num_len = len(a)
  head = a[0]
  a = a[1:]
  if num_len == 4:
    return  ones[int(head)] + 'thousand' + num_2_words(int(a))
  if num_len == 3:
    if int(a) == 0:
      return  ones[int(head)] + 'hundred' + num_2_words(int(a))
    else:
      return  ones[int(head)] + 'hundred' + 'and' + num_2_words(int(a)) 
  if num_len == 2:
    if int(head) > 1:
      return tens[int(head)] + num_2_words(int(a))
    else:
      return teens[int(str(head) + a)]
  if num_len == 1:
    return ones[int(head)]



def sum_words(n):
  sum = 0
  for x in range(1, n+1):
    print num_2_words(x)
    sum += len(num_2_words(x))
  return sum
print sum_words(1000)
