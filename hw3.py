import os
import codecs

cmd=""                                                   #無功能,建立cmd變數給while使用
while True:                                              #令while cmd!=0 可使回圏重覆執行 或令while=ture
    os.system("cls")                                     #os.system("cls") 每次執行功能後 清空上一次資料(畫面乾淨)
    if cmd=="0":
         os._exit(0)                                     #輸入0 結束程式
    elif cmd=="1":
         ret=os.listdir("./")                            #建立變數ret取得資料夾中檔案列表(list)
         count=0                                         #count為後面檔案建立顯示的編號
         for file in ret:                                #在ret檔案列表中建立file(變數)迴圈 (使列表呈現由上至下)
             if os.path.isfile(file):                    #判斷是否為檔案
                print(count,file)                        #顯示資料夾中的檔案和編號count
                count+=1                                 #編號從0~最後
    elif cmd=="2":
         ret=os.listdir("./")
         count=0
         for folder in ret:
             if os.path.isdir(folder):                   #判斷是否為資料夾
                print(count,folder)
                count+=1
    elif cmd=="3":
         ret=os.listdir("./")
         count=0
         filenum=[]                                      #建立一個list
         for files in ret:
             if os.path.isfile(files):                   
                 print(count, files)
                 count+=1
                 filenum+=[files]                        #判斷是檔案後 令files成為一個list資料組 同時並編號(0~最後)
         x=int(input("請輸入欲顯示檔案索引:"))                  #輸入想要的編號索引
         os.system("cls")                                
         with codecs.open(filenum[x], "r", "utf-8") as filee:   #使用顯示檔案內容與法  輸入想要開啟的編號檔案 
             print("=========檔案開始=========")
             print(filee.read())
             print("=========檔案結束=========")
    elif cmd=="4":
         ret=os.listdir("./")
         count=0
         filenum=[]
         for delfile in ret:
             if os.path.isfile(delfile):
                 print(count, delfile)
                 count+=1
                 filenum+=[delfile]       
         x=int(input("請輸入欲刪除檔案索引:"))   
         os.system("cls")
         os.remove(filenum[x])            #刪除語法
    elif cmd=="5":
         ret=os.listdir("./")
         count=0
         filenum=[]
         for exefile in ret:
             if os.path.isfile(exefile):
                print(count,exefile)
                count+=1
                filenum+=[exefile]
         x=int(input("請輸入欲執行檔案索引:"))
         os.system("cls")
         os.startfile(filenum[x])         #執行語法
    elif cmd=="6":
         ret=os.listdir("./")
         count=0
         foldernum=[]
         for enterfolder in ret:
             if os.path.isdir(enterfolder):
                print(count,enterfolder)
                count+=1
                foldernum+=[enterfolder]  
         x=int(input("請輸入欲進入資料夾索引:"))
         os.system("cls")
         os.chdir(foldernum[x])          #改變工作路徑語法
         print(os.getcwd())
    elif cmd=="7":
         ret=os.listdir("./")
         count=0
         foldernum=[]
         for delfolder in ret:
             if os.path.isdir(delfolder):
                print(count,delfolder)
                count+=1
                foldernum+=[delfolder]
         x=int(input("請輸入欲刪除資料夾索引:"))
         os.system("cls")
         os.rmdir(foldernum[x])
    elif cmd=="8":
         backfolder=os.path.dirname(os.getcwd())    #建立變數backfolder=取檔名中路徑部分(取得當前工作路徑(os.getcwd))
         os.chdir(backfolder)
         print(os.getcwd())
    else:
          pass


    print("工作路徑:",os.getcwd())
    print("""            (0) 離開程式
            (1) 列出檔案
            (2) 列出資料夾
            (3) 顯示檔案內容
            (4) 刪除檔案
            (5) 執行檔案
            (6) 進入資料夾
            (7) 刪除資料夾
            (8) 回上層資料夾""")
    cmd=input("操作:")