package com.example.chatbox.Controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import java.util.Map;

@RestController
@RequestMapping("/chat")
public class ChatController {
    private final String FLASK_URL = "http://localhost:5001/chat"; // flask api adresi

    @PostMapping
    public ResponseEntity<Map> chat(@RequestBody Map<String, String> request) {
        RestTemplate restTemplate = new RestTemplate();
        // Diğer API'lere HTTP isteği göndermek için kullanılan Spring sınıfı
        ResponseEntity<Map> response = restTemplate.postForEntity(FLASK_URL, request, Map.class);
        // http yanıtlarını yönetmek için ResponseEntity kullanıldı
        // json formatındaki request/response verilerini kullanabilmek için Map<String, String> oluşturuldu
        return ResponseEntity.ok(response.getBody());
    }
}
