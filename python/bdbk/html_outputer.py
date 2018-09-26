# coding:utf-8

print("HTML 输出页面")


class HtmlOutput(object):

    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 展示数据
    def output_html(self):

        fout = open('output.html', 'w',encoding="utf-8")
        file = open('file.txt','w')

        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta http-equiv="Content-Type" content="text/html;charset=utf-8">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table border="1">')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td><a href = "%s">%s</a></td>' % (data['url'], data['title']))
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()


