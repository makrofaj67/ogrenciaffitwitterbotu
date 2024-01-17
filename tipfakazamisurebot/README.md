# tipfakazamisurebot

//https://youtu.be/6lNBurHzm-w  bu videoda aşağıdaki adımları göstermeye çalıştım bakabilirsiniz.

1) Microsoft Store'dan python 3.11'i indirin.
2) Masaüstünde başlat menüsüne tıklayın ve komut istemini çalıştırın.
3) Komut istemine aşağıdaki satırı girin ve enter'a basın.

pip install tweepy PyQt5

4) Yukarıda sağ üst köşede Go to file, Add file, ve code butonları var. Yeşil olan code'a tıklayın. En altta download as zip çıkacak, ona tıklayın ve zip olarak indirin.
5) İndirdiğiniz zip dosyasının içerisindeki klasörü masaüstüne çıkarın.
6) Klasörü açın, klasörün içerisindeyken shift'e basılı tutup fare ile sağ tıklayın. Powershell ya da komut istemini burada açın diye bir seçenek çıkacak, ona tıklayın.
7) Açılan powershell ya da komut istemi penceresinde aşağıdaki satırları girin ve enter'a basın.

python main.py

7) Twitter'da bir developer account açın.

https://developer.twitter.com/

ve aşağıdaki adımları izleyin bu keyleri programa girmemiz gerekecek. benim hesabımda zaten açılmış olduğu için buraları videoya alamadım çok fazla.

https://www.youtube.com/watch?v=qVe7PeC0sUQ&t=215s

8) Programda tivitleri mentionları hashtaglari kendiniz değiştirebilirsiniz. Programa girmek yerine txt dosyalarını da düzenleyebilirsiniz. Tweetleri rastgele sırayla atabilirsiniz. Tweeterdan aldığınız keyleri girdikten sonra tamam'a tıklayın yoksa kaydetmez. Aynı şekilde seçimleri kaydet butonuna da tıklamanız gerekli.

Şimdilik bi kaç problem var 
  * Eğer kaç dakikada bir atılsın sorusuna 0 deyip seçimi kaydederseniz bütün tweetleri aynı anda atar. 
  * Şimdilik tweet kac tivit atılacağa 70'den fazla girerseniz bazen sorun olabiliyor. 
  * Mention ve hashtag boş kalırsa tweet sonunda # @ eklenir. //hallettim
  * İlerideki günlerde geçen süreye saat de ekleyeceğim. Bir saat süreyi geçerse ne oluyor bilmiyorum. Şimdilik bu kadar. //hallettim
  * Bazı tweetler çok uzun olmuş, onları atmaya çalıştığı zaman tweeter izin vermiyor. Ondan dolayı program çalışmayı durduruyor. Uzun tweetleri silerek çözebilirsiniz bi kaç güne tweetleri düzenleyeceğim. //hallettim
