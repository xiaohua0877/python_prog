import argparse
parser = argparse.ArgumentParser()
parser.add_argument('echo')     # add_argument()指定程序可以接受的命令行选项
args = parser.parse_args()      # parse_args()从指定的选项中返回一些数据
print(args)
print(args.echo)


'''
python3中argparse模块
1、定义：argparse是python标准库里面用来处理命令行参数的库

2、命令行参数分为位置参数和选项参数：
位置参数就是程序根据该参数出现的位置来确定的
如：[root@openstack_1 /]# ls root/    #其中root/是位置参数
选项参数是应用程序已经提前定义好的参数，不是随意指定的
如：[root@openstack_1 /]# ls -l    # -l 就是ls命令里的一个选项参数
3、使用步骤：

（1）import argparse    首先导入模块
（2）parser = argparse.ArgumentParser（）    创建一个解析对象
（3）parser.add_argument()    向该对象中添加你要关注的命令行参数和选项
（4）parser.parse_args()    进行解析
4、argparse.ArgumentParser（）方法参数须知：一般我们只选择用description

prog=None     - 程序名

description=None,    - help时显示的开始文字
epilog=None,     - help时显示的结尾文字
parents=[],        -若与其他参数的一些内容一样，可以继承
formatter_class=argparse.HelpFormatter,     - 自定义帮助信息的格式
prefix_chars='-',    - 命令的前缀，默认是‘-’
fromfile_prefix_chars=None,     - 命令行参数从文件中读取
argument_default=None,    - 设置一个全局的选项缺省值，一般每个选项单独设置
conflict_handler='error',     - 定义两个add_argument中添加的选项名字发生冲突时怎么处理，默认处理是抛出异常
add_help=True    - 是否增加-h/--help选项，默认是True)
5、add_argument()方法参数须知：

name or flags...    - 必选，指定参数的形式，一般写两个，一个短参数，一个长参数

parser = argparse.ArgumentParser(description = 'this is a description')
parser.add_argument('--ver', '-v', action = 'store_true', help = 'hahaha')
# 将变量以标签-值的字典形式存入args字典
args = parser.parse_args()
if args.ver:
    print("Ture")
else:
    print("False")
    
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('echo')     # add_argument()指定程序可以接受的命令行选项
args = parser.parse_args()      # parse_args()从指定的选项中返回一些数据
print(args)
print(args.echo)
    
'''