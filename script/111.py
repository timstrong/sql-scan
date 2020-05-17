#coding=utf-8

#import libs
import 1_cmd
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
ElementBGArray={}
ElementBGArray_Resize={}
ElementBGArray_IM={}

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  1:
    def __init__(self,root):
      global ElementBGArray
      global ElementBGArray_Resize
      global ElementBGArray_IM
      Fun.G_UIElementArray['UIClass']=self
      self.root = root
      root.title("Form1")
      root.geometry("500x400")
      Form_1= tkinter.Canvas(root,width = 10,height = 4)
      Form_1.place(x = 0,y = 0,width = 500,height = 400)
      Form_1.configure(bg = "#efefef")
      Fun.G_UIElementArray['root']=root
      Fun.G_UIElementArray['Form_1']=Form_1
      #Create the elements of root
      Fun.G_UIElementVariableArray['Entry_2']=tkinter.StringVar()
      Entry_2= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_2'])
      Entry_2.place(x = 80,y = 50,width = 301,height = 50)
      Entry_2.configure(relief = "sunken")
      Fun.G_UIElementArray['Entry_2']=Entry_2
      Button_3= tkinter.Button(root,text="开始检测",width = 10,height = 4)
      Button_3.place(x = 400,y = 50,width = 100,height = 28)
      Fun.G_UIElementArray['Button_3']=Button_3
      Button_4= tkinter.Button(root,text="结束检测",width = 10,height = 4)
      Button_4.place(x = 400,y = 100,width = 100,height = 28)
      Fun.G_UIElementArray['Button_4']=Button_4
      Button_5= tkinter.Button(root,text="版本信息",width = 10,height = 4)
      Button_5.place(x = 400,y = 150,width = 100,height = 28)
      Fun.G_UIElementArray['Button_5']=Button_5
      Label_6= tkinter.Label(root,text="web系统SQL注入漏洞检测系统",width = 10,height = 4)
      Label_6.place(x = 144,y = 19,width = 186,height = 20)
      Fun.G_UIElementArray['Label_6']=Label_6
      Label_7= tkinter.Label(root,text="输入网址",width = 10,height = 4)
      Label_7.place(x = -24,y = 64,width = 100,height = 20)
      Fun.G_UIElementArray['Label_7']=Label_7
      Label_8= tkinter.Label(root,text="状态",width = 10,height = 4)
      Label_8.place(x = -20,y = 310,width = 100,height = 20)
      Fun.G_UIElementArray['Label_8']=Label_8
      Fun.G_UIElementVariableArray['Entry_9']=tkinter.StringVar()
      Entry_9= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_9'])
      Entry_9.place(x = 50,y = 250,width = 400,height = 130)
      Entry_9.configure(relief = "sunken")
      Fun.G_UIElementArray['Entry_9']=Entry_9
      Label_10= tkinter.Label(root,text="输入线程数",width = 10,height = 4)
      Label_10.place(x = -18,y = 121,width = 100,height = 20)
      Fun.G_UIElementArray['Label_10']=Label_10
      Fun.G_UIElementVariableArray['Entry_11']=tkinter.StringVar()
      Entry_11= tkinter.Entry(root,textvariable=Fun.G_UIElementVariableArray['Entry_11'])
      Entry_11.place(x = 80,y = 120,width = 120,height = 20)
      Entry_11.configure(relief = "sunken")
      Fun.G_UIElementArray['Entry_11']=Entry_11
      Text_12= tkinter.Text(root)
      Text_12.place(x = 80,y = 156,width = 196,height = 86)
      Text_12.configure(relief = "sunken")
      Fun.G_UIElementArray['Text_12']=Text_12
      Button_13= tkinter.Button(root,text="联系作者",width = 10,height = 4)
      Button_13.place(x = 400,y = 197,width = 100,height = 28)
      Fun.G_UIElementArray['Button_13']=Button_13
      #Inital all element's Data
      Fun.InitElementData()
      #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = 1(root)
    root.mainloop()

