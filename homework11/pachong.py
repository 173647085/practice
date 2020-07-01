import requests,re,json,threading,time
from requests.exceptions import RequestException
from multiprocessing.pool import ThreadPool
from queue import Queue
import pymysql
from DBUtils.PooledDB import PooledDB


total_num=0
total_max=0
total_min=0
class ThreadInsert(object):
    "多线程并发MySQL插入数据"
    def __init__(self):
        start_time = time.time()
        self.pool = self.mysql_connection()
        self.data = self.getData()
        self.mysql_delete()
        self.task()
        print("========= 数据插入,共耗时:{}'s =========".format(round(time.time() - start_time, 3)))

    def mysql_connection(self):
        maxconnections = 15  # 最大连接数
        pool = PooledDB(
            pymysql,
            maxconnections,
            host='localhost',
            user='root',
            port=3306,
            passwd='zxl.2000',
            db='test',
            charset='utf8',
            use_unicode=True)
        return pool

    def getData(self):
        st = time.time()
        with open("data.txt", "rb") as f:
            data = []
            for line in f:
                line = re.sub("\s", "", str(line, encoding="utf-8"))
                line = tuple(line.split("||"))
                data.append(line)
        n = 100    # 按每100行数据为最小单位拆分成嵌套列表
        result = [data[i:i + n] for i in range(0, len(data), n)]
        print("共获取{}组数据,每组{}个元素.==>> 耗时:{}'s".format(len(result), n, round(time.time() - st, 3)))
        return result

    def mysql_delete(self):
        st = time.time()
        con = self.pool.connection()
        cur = con.cursor()
        sql = "TRUNCATE TABLE test"
        cur.execute(sql)
        con.commit()
        cur.close()
        con.close()
        print("清空原数据.==>> 耗时:{}'s".format(round(time.time() - st, 3)))

    def mysql_insert(self, *args):
        con = self.pool.connection()
        cur = con.cursor()
        sql = "INSERT INTO 51job(职位名,公司名,工作地点,薪资,发布时间)VALUE(%s,%s,%s,%s,%s)"
        try:
            cur.executemany(sql, *args)
            con.commit()
        except Exception as e:
            con.rollback()  # 事务回滚
            print(*args)
            print('SQL执行有误,原因:', e)
            exit
        finally:
            cur.close()
            con.close()

    def task(self):
        q = Queue(maxsize=10)  # 设定最大队列数和线程数
        st = time.time()
        while self.data:
            content = self.data.pop()
            t = threading.Thread(target=self.mysql_insert, args=(content,))
            q.put(t)
            if (q.full() == True) or (len(self.data)) == 0:
                thread_list = []
                while q.empty() == False:
                    t = q.get()
                    thread_list.append(t)
                    t.start()
                for t in thread_list:
                    t.join()
        print("数据插入完成.==>> 耗时:{}'s".format(round(time.time() - st, 3)))


def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


def get_one_page(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3706.400 SLBrowser/10.0.4040.400'}
    try:
        res=requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.content.decode('gb18030')
        return None
    except RequestException:
        return None


def parse_one_page(html):
    list1=[]
    list3=[]
    reg = re.compile('<div class="el">.*?<a target="_blank" title="(.*?)".*?<a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    data = re.findall(reg,html)
    for item in data:
        list2=[]
        dict1={
            '职位名': item[0],
            '公司名': item[1],
            '工作地点':  item[2],
            '薪资': item[3],
            '发布时间': item[4]
        }
        salary = str(dict1['薪资'])
        salary = salary[0:-3]
        b = salary.find('-')
        min_salary = salary[:b]
        max_salary = salary[b+1:]
        if(is_num(min_salary) and is_num(max_salary)):
            list1.append(dict1)
            for i in range(5):
                list2.append(item[i])
                if i != 4:
                    list2.append('||')
            list3.append(list2)
    return(list1,list3)


def sum(data1):
    min_salary=0
    max_salary=0
    global total_num,total_max,total_min
    for item in data1:
        total_num+=1
        salary = str(item['薪资'])
        if(salary[-3:] == '千/月'):
            scale = 0.1
        elif(salary[-3:] == '万/年'):
            scale = 1/12
        elif(salary[-3:] == '元/天'):
            scale = 3/1000
        else:
            scale = 1
        salary = salary[0:-3]
        b = salary.find('-')
        min_salary = salary[:b]
        max_salary = salary[b+1:]
        if(is_num(min_salary) and is_num(max_salary)):
            a = (float(min_salary)*scale)
            c = (float(max_salary)*scale)
            total_min +=a
            total_max +=c
        else:
            total_num-=1


def write(data1,data2):
    with open('result.txt','a',encoding='utf-8') as f:
        for item in data1:
            f.writelines(json.dumps(item,ensure_ascii=False)+'\n')
    with open('data.txt','a',encoding='utf-8') as f:
        for item in data2:
            str_1="\n"
            f.writelines(item) #将歌词写入文件
            f.write(str_1)
    

def main(index):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%'\
          '25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&postchannel=0000&workyear=99&cotyp'\
          'e=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(index)
    html=get_one_page(url)
    data1,data2=parse_one_page(html)
    write(data1,data2)
    if index<4:
        url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%'\
              '25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype='\
              '99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(index)
        html=get_one_page(url)
        data1,data2=parse_one_page(html)
        sum(data1)
    else:
        pass


if __name__ == "__main__":
    p = ThreadPool(10)
    for i in range(1,39):
        p.apply_async(main,(i,))
    p.close()
    p.join()
    print('北京Python工程师职位总数为{}'.format(total_num))
    Min = total_min/total_num
    Max = total_max/total_num
    print("北京Python工程师职位平均薪资为:"+str('%.2f'%Min ) + "-" +str('%.2f'%Max)+"万/月")
    ThreadInsert()