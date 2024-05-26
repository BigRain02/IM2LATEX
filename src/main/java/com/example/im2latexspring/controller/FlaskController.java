package com.example.im2latexspring.controller;

import com.example.im2latexspring.dto.LatexDto;
import com.example.im2latexspring.service.FlaskService;
import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequiredArgsConstructor
public class FlaskController {
    private final FlaskService service;

    @PostMapping("/flask")
    public LatexDto sendToFlask(@RequestParam("image")MultipartFile image) throws Exception {
        return service.sendToFlask(image);
    }

}
