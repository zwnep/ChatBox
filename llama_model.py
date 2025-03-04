# pip install flask transformers torch
# Daha öncesinde hugging face'den gidip izin alındı ve geçerli bir token oluşturuldu modeli indirebilmek için 


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from flask import Flask, request, jsonify


app = Flask(__name__)

model_name = "meta-llama/Llama-3.1-8B"  # en küçük versiyon

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

print("Model başarılı ir şekilde indirildi!")


# modelin testi - doğru çalışıp çalışmadığını test etmek için

# prompt = "Hi, how are you today?"
# inputs = tokenizer(prompt, return_tensors="pt")
# outputs = model.generate(**inputs, max_length=100)
# response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print("LLaMA Yanıtı:", response)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        # modelin anlayabileceği formata çevir, 
        # tokenizer, kullanıcının metnini modelin anlayabileceği bir formata (genellikle token ID'leri) dönüştürür.
        inputs = tokenizer(user_input, return_tensors="pt")

        # modelin çalıştırır.
        # torch.no_grad() ile modelin eğitim modunda olmadığını ve gradyan hesaplaması yapılmayacağını belirtildi performans açısından kazanç sağlamak için
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=100)

        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True) # modelin ürettiği token ID'leri (outputs[0]), tokenizer.decode() ile okunabilir bir metne dönüştürüldü (yani bizim, insanların)

        return jsonify({"response": response_text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)