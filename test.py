import psycopg2
connection = psycopg2.connect(user='webadmin',
                                    password='RTTooa27373',
                                    host='node36662-jakapat.proen.app.ruk-com.cloud',
                                    port='11243',
                                    database='login')
cursor = connection.cursor()
cursor2 = connection.cursor()

select_gold_thai_1 = "select goldthaistick.sell , goldthaistick.buy from goldthaistick"
select_gold_thai_2 = "select goldthairoopapan.buy_roop , goldthairoopapan.sell_roop from goldthairoopapan"

cursor.execute(select_gold_thai_1)
cursor2.execute(select_gold_thai_2)

Data1 = cursor.fetchall()
Data2 = cursor2.fetchall()


s = []
for i in Data1:
    for z in i:
        s.append(z)

s2 = []
for e in Data2:
    for t in e:
        s2.append(t)

l = [',']

out_list = [ x.replace(y,'')  for x in s for y in l if y in x ]
out_list2 = [ x.replace(y,'')  for x in s2 for y in l if y in x ]

outlist = out_list + out_list2
print(outlist)



