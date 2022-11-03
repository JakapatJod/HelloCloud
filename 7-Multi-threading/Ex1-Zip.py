import threading # Multi-threading สั่งทำโดยไม่ต้อง รอ การทำงาน
import zipfile 
# การทำ responsive ทำงานได้เร็วขึ้น
# ต้องรู้จักรการทำ CPU , OS , Process(Flask) , Thread(แบ่งการทำงานย่อย และรวมกัน) Blocking = ถ้าการทำ User จะทำการ Blocking ตัว User ให้รอ
class AsyncZip(threading.Thread):
    def __init__(self, infile , outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    
    def run(self):
        f = zipfile.ZipFile(self.outfile,'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of: ',self.infile)

background = AsyncZip('7-Multi-threading/mydata.txt',   # ต้องสร้างไฟล์ txt ขึ้นมาก่อน ถึงจะสั่ง run ได้
                        '7-Multi-threading/myarchive.zip') # เก็บ txt ลงในไฟล์ zip
background.start()
print('The main program continues to run in foreground. ')

background.join()
# Wait for the background task to finish print('Main program waited until background was done.)