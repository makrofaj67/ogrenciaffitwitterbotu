import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QTimer, QTime, QElapsedTimer
import tweepy
import time
import threading
import random
import tweetolusturma
import siraylatweetolusturma

app = QApplication(sys.argv)

class TweetsWindow(QWidget):
  def __init__(self):
    super().__init__()
    uic.loadUi('tweetler.ui', self)

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.setWindowIcon(icon)    

    self.show()
    self.pushButton.clicked.connect(self.funcmentionlarekle)
    self.pushButton_3.clicked.connect(self.funcmentionlarsil)
    self.load_mentionlar()

  def funcmentionlarekle(self):
    mention = self.lineEdit.text()
    if mention:
      self.listWidget.addItem(mention)
      self.lineEdit.clear()
      self.save_mentionlar()

  def funcmentionlarsil(self):
    for item in self.listWidget.selectedItems():
        self.listWidget.takeItem(self.listWidget.row(item))
    self.save_mentionlar()

  def load_mentionlar(self):
    try:
      with open("tweetler.txt", "r") as f:
        for line in f:
          mention = line.strip()
          if mention:
            self.listWidget.addItem(mention)
    except FileNotFoundError:
            pass

  def save_mentionlar(self):
    with open("tweetler.txt", "w") as f:
      for row in range(self.listWidget.count()):
        f.write(self.listWidget.item(row).text() + "\n")       
        
class MentionsWindow(QWidget):
  def __init__(self):
    super().__init__()
    uic.loadUi('mentionlar.ui', self)

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.setWindowIcon(icon)

    self.show()
    self.pushButton.clicked.connect(self.funcmentionlarekle)
    self.pushButton_3.clicked.connect(self.funcmentionlarsil)
    self.load_mentionlar()

  def funcmentionlarekle(self):
    mention = self.lineEdit.text()
    if mention:
      self.listWidget.addItem(mention)
      self.lineEdit.clear()
      self.save_mentionlar()

  def funcmentionlarsil(self):
    for item in self.listWidget.selectedItems():
        self.listWidget.takeItem(self.listWidget.row(item))
    self.save_mentionlar()

  def load_mentionlar(self):
    try:
      with open("mentionlar.txt", "r") as f:
        for line in f:
          mention = line.strip()
          if mention:
            self.listWidget.addItem(mention)
    except FileNotFoundError:
            pass

  def save_mentionlar(self):
    with open("mentionlar.txt", "w") as f:
      for row in range(self.listWidget.count()):
        f.write(self.listWidget.item(row).text() + "\n")

class Hashtaglar(QWidget):
  def __init__(self):
    super().__init__()
    uic.loadUi('hashtaglar.ui', self)

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.setWindowIcon(icon)

    self.show()
    self.pushButton.clicked.connect(self.funcmentionlarekle)
    self.pushButton_3.clicked.connect(self.funcmentionlarsil)
    self.load_mentionlar()

  def funcmentionlarekle(self):
    mention = self.lineEdit.text()
    if mention:
      self.listWidget.addItem(mention)
      self.lineEdit.clear()
      self.save_mentionlar()

  def funcmentionlarsil(self):
    for item in self.listWidget.selectedItems():
        self.listWidget.takeItem(self.listWidget.row(item))
    self.save_mentionlar()

  def load_mentionlar(self):
    try:
      with open("hashtaglar.txt", "r") as f:
        for line in f:
          mention = line.strip()
          if mention:
            self.listWidget.addItem(mention)
    except FileNotFoundError:
            pass

  def save_mentionlar(self):
    with open("hashtaglar.txt", "w") as f:
      for row in range(self.listWidget.count()):
        f.write(self.listWidget.item(row).text() + "\n")

class Anahtarlar(QWidget):
 def __init__(self):
  super(Anahtarlar, self).__init__()
  uic.loadUi('anahtarlar.ui', self)

  icon = QtGui.QIcon()
  icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
  self.setWindowIcon(icon)

  self.anahtarlarikaydet.clicked.connect(self.funcanahtarlarikaydet)

  with open("anahtarlar.txt", "r") as file:
    api_key = file.readline().strip()
    api_key_secret = file.readline().strip()
    bearer_token = file.readline().strip()
    acess_token = file.readline().strip()
    acess_token_secret = file.readline().strip()
  self.apikeyline.setText(api_key)
  self.apikeysecretline.setText(api_key_secret)
  self.bearertokenline.setText(bearer_token)
  self.accesstokenline.setText(acess_token)
  self.accesstokensecretline.setText(acess_token_secret)
    
 def funcanahtarlarikaydet(self):
  self.api_key = self.apikeyline.text().strip()
  self.api_key_secret = self.apikeysecretline.text().strip()
  self.bearer_token = self.bearertokenline.text().strip()
  self.access_token = self.accesstokenline.text().strip()
  self.access_token_secret = self.accesstokensecretline.text().strip()
    
  with open("anahtarlar.txt", "w") as file:
   
   file.write(self.bearer_token + "\n")
   file.write(self.api_key + "\n")
   file.write(self.api_key_secret + "\n")   
   file.write(self.access_token + "\n")
   file.write(self.access_token_secret + "\n")

  message_box = QMessageBox()
  message_box.setText("Anahtarlar kaydedildi!")
  message_box.setWindowTitle("Bilgi")
  message_box.exec_()



class Anasayfa(QMainWindow):
 def __init__(self):
  super(Anasayfa, self).__init__()
  uic.loadUi('mainwindow.ui', self)
  
  icon = QtGui.QIcon()
  icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
  self.setWindowIcon(icon)

  self.tweeteranahtarlarinigir.triggered.connect(self.anahtarlar)
  self.actionMention.triggered.connect(self.mention)
  self.actionTweet.triggered.connect(self.tweet)
  self.actionHashtag.triggered.connect(self.hashtag)
  self.tweetlebutton.clicked.connect(lambda: threading.Thread(target=self.tweetle_thread).start())
  self.tweetlebutton.clicked.connect(lambda: threading.Thread(target=self.timer_thread).start())
  self.timer = QTimer()
  self.start_time = None
  
  self.secimlerikaydetbutton.clicked.connect(self.secimlerikaydet)
  with open("ayarlar.txt", "r") as file:
   self.kactivitline.setText(file.readline().strip())
   self.kacdakikaline.setText(file.readline().strip())
   self.rastgelecheckbox.setChecked(file.readline() == "True")
      
 def secimlerikaydet(self):
  kactivittext = self.kactivitline.text().strip()
  kacdakikatext = self.kacdakikaline.text().strip()
  rastgele_mi = self.rastgelecheckbox.isChecked()
  with open("ayarlar.txt", "w") as file:
   file.write(f"{kactivittext}\n{kacdakikatext}\n{rastgele_mi}")
  message_box = QMessageBox()
  message_box.setText("Seçimler kaydedildi!")
  message_box.setWindowTitle("Bilgi")
  message_box.exec_()
  
 def anahtarlar(self):
  self.anahtarpenceresi=Anahtarlar()
  self.anahtarpenceresi.show()
 
 def mention(self):
  self.mentionlar = MentionsWindow()
  self.mentionlar.show()
  
 def tweet(self):
  self.tweetler = TweetsWindow()
  self.tweetler.show()
  
 def hashtag(self):
  self.hashtaglar = Hashtaglar()
  self.hashtaglar.show() 
 
 def timer_thread(self):
  self.timer.start(10)
  self.start_time = QTime.currentTime()

  while True:
    elapsed_time = self.start_time.msecsTo(QTime.currentTime()) / 1000.0
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time // 60) % 60)
    seconds = int(elapsed_time % 60)
    time_strhours = "{:02d}".format(hours)
    time_str = "{:02d}:{:02d}".format(minutes, seconds)
    self.gecensurelcdsaat.display(time_strhours)
    self.gecensurelcd.display(time_str)
    threading.Event().wait(0.01)   
 
 def tweetle_thread(self):
  self.tweetle()
  
 def tweetle(self):  
  
  with open("hashtaglar.txt", "r") as file:
    hashtags = file.readlines()
  with open("tweetler.txt", "r") as file:
    tweets = file.readlines()
  with open("mentionlar.txt", "r") as file:
    mentions = file.readlines()

  with open("anahtarlar.txt", "r") as file:
    bearertoken = file.readline().strip()
    consumer_api_key = file.readline().strip()
    consumer_api_key_secret = file.readline().strip()   
    accesstoken = file.readline().strip()
    accesstoken_secret = file.readline().strip()

  try:
    tweetci = tweepy.Client(bearer_token=bearertoken, consumer_key=consumer_api_key, consumer_secret=consumer_api_key_secret, access_token=accesstoken, access_token_secret=accesstoken_secret)
  except Exception as e:
    print("Error creating Tweepy client:", e)
  
  with open("ayarlar.txt", "r") as file:
    ayar = file.readlines()

  kactivit = int(ayar[0])
  kacdakikadabir = int(ayar[1])
  rastgele = ayar[2]

  if rastgele == "False":
    for k in range(kactivit):
      siraylastringolusturucu = siraylatweetolusturma.RastgeleTweetSec()
      new_tweet = siraylastringolusturucu.rastgele_tweet_sec(k)
      try:
        tweetci.create_tweet(text=new_tweet)
      except Exception as e:
        print("Error creating tweet:", e)
      else:  
        self.atilanensontweet.addItem(new_tweet)
        self.atilantweetlcd.display(k + 1)
      finally:
        time.sleep(kacdakikadabir * 60)
  else:
    for i in range(kactivit):
      stringolusturucu = tweetolusturma.RastgeleTweetSec()
      new_tweet = stringolusturucu.rastgele_tweet_sec()
      try:
        tweetci.create_tweet(text=new_tweet)
      except Exception as e:
        print("Error creating tweet:", e)
      else:  
        self.atilanensontweet.addItem(new_tweet)
        self.atilantweetlcd.display(i + 1)
      finally:
        time.sleep(kacdakikadabir * 60)    

window = Anasayfa()
window.show()

sys.exit(app.exec_())

        
                   
    
