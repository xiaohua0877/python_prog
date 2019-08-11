
'''python之os.environ模块学习
2018年07月05日 10:16:26 专丶注 阅读数 7355
我们想要用python获得一些有关系统的各种信息的时候就不得不想到os的environ，那这里面都具体包含了那些内容呢？



一、简介

对于官方的解释，environ是一个字符串所对应环境的映像对象。这是什么意思呢？举个例子来说，environ[‘HOME’]就代表了当前这个用户的主目录。

下图是windows和ubuntu下的environ的key列表：

windows：



linux：



虽然基本的字段对差不多，但是不同的系统有些字段还有有一些小小的差异。



二、举例

比如刚刚举例的os.environ[HOME]在linux中适用而在windows下面是没有这个key的，在windows下是HOMEPATH,又比如linux下的USER在windows下面对应的就是USERNAME:

windows：



linux：





总结这些差异来说，他们都是各自系统的本身特性造成的，比如你用的是gnome版的ubuntu，那么key里面就会多出一条[‘GNOME_DESKTOP_SESSION_ID’].





三、key字段详解

作为一个渗透测试学习者来说，对系统的足够了解是基本的要求，下面就通过对os.environ中的key解读的角度来认识系统。

windows：


· os.environ[‘HOMEPATH’]:当前用户主目录。

os.environ[‘TEMP‘]:临时目录路径。

os.environ[PATHEXT’]:可执行文件。

os.environ[‘SYSTEMROOT‘]:系统主目录。

os.environ[‘LOGONSERVER’]:机器名。

os.environ[‘PROMPT’]:设置提示符。

linux：


os.environ[‘USER‘]:当前使用用户。

os.environ[‘LC_COLLATE’]:路径扩展的结果排序时的字母顺序。

os.environ[‘SHELL’]:使用shell的类型。

os.environ[‘LAN’]:使用的语言。

os.environ[‘SSH_AUTH_SOCK‘]:ssh的执行路径。
'''