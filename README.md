
# Token'dan Çizime: ANTLR ve PLY ile Turtle İle Çizim

## Proje Açıklaması

Bu proje, Python kullanarak bir metin dosyasındaki komutları okuyup analiz eden ve bu komutlara göre çizim yapan bir uygulama geliştirmeyi amaçlar. Proje, ANTLR ve PLY kütüphanelerini kullanarak bir parse tree oluşturur ve ardından Turtle grafik kütüphanesi ile bu parse tree'yi çizim haline getirir. Ayrıca, Tkinter kütüphanesi kullanılarak kullanıcı dostu bir arayüz tasarlanmıştır.

## Teknolojiler ve Kütüphaneler

- **Python**: Projeyi geliştirmek için ana programlama dili.
- **ANTLR**: Parse tree oluşturmak için kullanılır.
- **PLY**: Token ayrıştırma ve parser gerçekleme işlemleri için kullanılır.
- **Turtle**: Grafik çizimi için kullanılır.
- **Tkinter**: Grafiksel kullanıcı arayüzü (GUI) oluşturmak için kullanılır.

## İşlem Adımları

1. **Projede Kullanılacak Teknolojilerin ve Kütüphanelerin Tespiti**
   - Python ve ilgili kütüphaneler seçilmiştir.

2. **Okunan Programın Token’lara Ayrılması**
   - Python'ın PLY kütüphanesi kullanılarak token'lar ayrıştırılır.

3. **ANTLR Kullanılarak Parse Tree Oluşturulması**
   - Parse ağacının görsel olarak incelenmesi ve CFG (Context-Free Grammar) paternlerinin kurallara uygun oluşturulması için ANTLR kullanılır.

4. **PLY’de Parser’ın Gerçeklenmesi**
   - ANTLR ile oluşturulan CFG grammeri PLY'nin desteklediği BNF (Backus-Naur Form) grammer’e dönüştürülür ve koda entegre edilir.

5. **Parser Kurallarına Uygun Bir Şekilde Turtle Kullanılarak Çizimin Yapılması**
   - Parser'dan çıkan sonuçlara göre Turtle ile çizim gerçekleştirilir.

6. **Arayüz Tasarımı**
   - Tkinter kullanılarak kullanıcı dostu bir arayüz tasarlanır.

7. **Turtle’ın GUI’a Entegre Edilmesi**
   - Çizen robot uygulaması, görsel arayüze entegre edilir.

## Kullanım

1. **Gerekli Kütüphanelerin Kurulumu**

   Python ve gerekli kütüphaneleri kurun:
   ```bash
   pip install antlr4-python3-runtime ply turtle
   ```

2. **Proje Dosyalarını İndirme**

   Proje dosyalarını indirin ve proje dizinine gidin.

3. **Uygulamayı Çalıştırma**

   Uygulamayı çalıştırmak için:
   ```bash
   python main.py
   ```

4. **Arayüz Kullanımı**

   - Sol tarafta bulunan "Open Text File" butonuna tıklayarak bir `.txt` dosyası seçin.
   - Açılan Turtle penceresinde komutların uygulanması ve çizimlerin görünmesi sağlanır.
