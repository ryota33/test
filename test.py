with open('input.txt', mode='rt', encoding='utf-8') as f:
  read_data = list(f)
num = int(read_data[53])
read_data.pop()
sep = ":"
ans = ""
for i in read_data:
  i = i[:-1]
  i = i.split(sep)
  i[0] = int(i[0])
  if num%i[0]==0:
    ans += i[1]
print(ans)