package com.example.im2latexspring.web.dto;

import lombok.Data;
import org.springframework.web.multipart.MultipartFile;

@Data
public class LatexDto {
    private MultipartFile image;
    private String latexStr;
}
