package com.example.im2latexspring.dto;

import lombok.Data;
import org.springframework.web.multipart.MultipartFile;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@Data
public class LatexDto {
    private MultipartFile image;
    private String latexStr;

    public void removeEscaped() throws JsonProcessingException {
        ObjectMapper mapper = new ObjectMapper();
        this.latexStr = mapper.readValue(this.latexStr, String.class);;
    }
}