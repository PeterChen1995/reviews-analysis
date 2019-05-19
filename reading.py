data = [] #建立一個空清單
count = 0 #計數器

with open('reviews.txt', 'r') as f:
	for line in f: #一行一行讀取
		data.append(line)
		count += 1  #count = count + 1 每讀一筆就加一
		if count % 1000 == 0: #每一千筆就印出來, %是求餘數的,count和1000的餘數是0就印出來
			print(len(data)) #資料的總筆數 = data的長度

print('檔案讀取完了, 總共有', len(data), '筆資料!')

sum_len = 0  #總長度從0開始
for d in data: #每一筆稱呼為d, data是清單裝著一百萬筆字串,每一個d就是一個字串,每一個字串可以用len求長度
	sum_len = sum_len + len(d) #sum_len += len(d), 每一筆留言(字串)加上上一筆的長度總和存回目前的總筆數

print('留言的平常度為', sum_len / len(data))

#要知道總長度可以用 print(sum_len)

new = []  #設一個新的空清單
for d in data: #取用之前的data清單,每筆留言叫d
	if len(d) < 100: #d的長度如果小於100
		new.append(d) #一個一個裝入new清單裡
print('一共有', len(new), '筆留言長度小於100!') #留言是英文,ex:help = 4個字

