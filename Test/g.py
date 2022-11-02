from flask import Flask, render_template
import psycopg2  


app = Flask(__name__)


@app.route('/')


def chart ():
    connection = psycopg2.connect(user='webadmin',
                                    password='RTTooa27373',
                                    host='node36662-jakapat.proen.app.ruk-com.cloud',
                                    port='11243',
                                    database='login')
    cursor1_graph = connection.cursor()
    cursor2_graph = connection.cursor()

    select_gold_thai_1_graph = "select goldthaistick.sell , goldthaistick.buy from goldthaistick"
    select_gold_thai_2_graph = "select goldthairoopapan.buy_roop , goldthairoopapan.sell_roop from goldthairoopapan"

    cursor1_graph.execute(select_gold_thai_1_graph)
    cursor2_graph.execute(select_gold_thai_2_graph)

    Data_graph1 = cursor1_graph.fetchall()
    Data_graph2 = cursor2_graph.fetchall()


    s = []
    for i in Data_graph1: # แปลง list ซ้อน list
        for z in i:
            s.append(z)

    s2 = []
    for e in Data_graph2:
        for t in e:
            s2.append(t)

    l = [',']

    out_list = [ x.replace(y,'')  for x in s for y in l if y in x ] # convert ให้เป็น ['29030'] ให้ลบตัว , ออกเพเพื่อจะใส่กราฟ
    out_list2 = [ x.replace(y,'')  for x in s2 for y in l if y in x ]

    outlist = out_list + out_list2
    print(outlist)

    return render_template("chard.html", chart_data=outlist)


if __name__ == "__main__":
    app.run(debug=True)