package com.example.im2latexspring.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.example.im2latexspring.dto.LatexDto;
import lombok.RequiredArgsConstructor;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
@Service
@RequiredArgsConstructor
public class FlaskService {
    private final String FLASK_URL = "http://127.0.0.1:8080/model";

    public LatexDto sendToFlask(MultipartFile image) throws IOException, JsonProcessingException {
        RestTemplate restTemplate = new RestTemplate();

        // Prepare the file as ByteArrayResource
        ByteArrayResource imageResource = new ByteArrayResource(image.getBytes()) {
            @Override
            public String getFilename() {
                return image.getOriginalFilename();
            }
        };

        // Prepare the request body with the image
        MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
        body.add("image", imageResource);

        // Set the headers
        HttpHeaders headers = new HttpHeaders();
        headers.set("Content-Type", "multipart/form-data");

        // Create the HttpEntity with body and headers
        HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(body, headers);

        // Send the request to Flask server
        ResponseEntity<String> response = restTemplate.exchange(FLASK_URL, HttpMethod.POST, requestEntity, String.class);

        // Create the DTO with the image and response
        LatexDto dto = new LatexDto();
        dto.setLatexStr(response.getBody());
        dto.removeEscaped();

        return dto;
    }
}
