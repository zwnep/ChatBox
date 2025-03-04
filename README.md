# ChatBox

Yapılan bu projede, Postman aracılığıyla mesaj gönderildiğinde, mesajın LLaMA 3.1 modeline iletilmesini ve yanıtın geri dönmesini sağlayan bir API servis geliştirildi.

- Spring Boot: API istemcisi ile model arasındaki köprü görevini üstlenir.
- Flask: LLaMA 3.1 modelini çalıştıran arayüzdür.
- LLaMA 3.1: Meta AI tarafından geliştirilen transformer tabanlı büyük dil modeli (LLM).
<br>
<br>
🔎 Proje Mimarisi  

<br>Postman → Spring Boot API → Flask API → LLaMA 3.1

Projede işleyiş:
<br>  
1️⃣ Kullanıcı, Postman üzerinden Spring Boot API’ye /chat endpoint’ine POST isteği ile bir mesaj gönderir.  
2️⃣ Spring Boot, mesajı alır ve Flask API’ye iletir.  
3️⃣ Flask, mesajı LLaMA 3.1 modeline gönderir ve yanıtı alır.  
4️⃣ Spring Boot, Flask'tan dönen yanıtı Postman’a geri iletir.  


<br>  

| Postman (Client) | → | Spring Boot (Backend) | → | Flask API (Python + AI) |
|------------------|----|----------------------|----|-------------------------|


<br><br>  

❓Peki neden Flask kullanıldı bu projede? Neden Bu Mimari Tercih Edildi?

Bu projede Spring Boot + Flask + LLaMA 3.1 mimarisi seçildi çünkü:

- Python, makine öğrenimi ve derin öğrenme modelleri için en yaygın kullanılan dildir.  
- LLaMA 3.1 modeli de python ile kolay entegre edilebilir.
<br>

LLaMA 3.1 modeli, Meta AI tarafından geliştirilen Hugging Face Transformers ve PyTorch ile çalışır.
<br>
Flask, Python tabanlı bir mikroframework olduğu için LLaMA modeliyle sorunsuz çalışır.
<br>  Eğer doğrudan Java ile model çalıştırılsaydı:
- Java'da PyTorch desteği olmadığından, ek kütüphanelerle karmaşık bir entegrasyon yapılması gerekirdi.

<br>Bu yüzden Flask, modeli çalıştıran bir ara katman olarak kullanıldı.
<br>  
Aynı zamanda, <br>  

- Python tarafında modeli güncellemek istediğimizde sadece Flask servisini değiştirmek yeterlidir.  
- Python tarafında sadece Flask API çalıştığı için, Java tarafında ek kütüphanelere gerek kalmaz.

<br>
<br>

⚙️ Gerekli Araçlar:

- Java Development Kit (JDK 17+)
- Maven veya Gradle (Spring Boot projelerini yönetmek için, bu proje için Maven yüklendi.)
- Spring Boot (Rest Api geliştirmek için.)
- Python (3.8 veya üstü gerekli, kullanılan güncel Python sürümü: "Python 3.11.8")
- Flask (Python tabanlı API servisi için)
- PyTorch ve Transformers (LLaMA 3.1 modelini çalıştırmak için)
- Postman (API'yi test etmek için)

<br><br>

📪 Postman'de API’yi test ederken, <br>

- Endpoint: "http://localhost:8080/chat"
- Method: POST
- Body (JSON, raw format):
    + {
         "message": "Hi, how are you?"
      }

şeklinde ayarlandı. 
<br>
- Beklenen yanıt ise,
    + {
        "response": "(İnglizce bir cevap.)"
      }
şeklindedir.
<br>
<br>

❓ İngilizce istekte bulunmamızın sebebi, 
- Llama 3.1'in desteklediği dillerin English , Almanca, Fransızca, İtalyanca, Portekizce, Hintçe, İspanyolca ve Tayca gibi dilllerin olmasıdır.

<br>
<br>
✅ Postman'de test edilmesi sonucu:
<br>
<br>

<img width="1440" alt="Ekran Resmi 2025-03-03 22 58 41" src="https://github.com/user-attachments/assets/3f41f5bc-c87f-4682-bfad-f31847564c67" />


<br>




