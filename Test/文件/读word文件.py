import win32com
import win32com.client
###于是在cmd中使用python -m pip install pypiwin32进行安装，成功解决。
def readWordFile(path):
    # 调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    doc.Close()
    mw.Quit()

b = os.path.exists("E:\\testFile\\py17")
if b:
    print("File Exist!")
else:
    os.mkdir("E:\\testFile\\py17")
    print('file create os mkdir ')

###path = r"E:\\Python\\py17\\Keyboardtext\\001.docx"
path = r"E:\\testFile\\17\\001.docx"
readWordFile(path)

