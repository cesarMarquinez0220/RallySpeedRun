package com.speedrun.rally.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.speedrun.rally.model.Producto;
import com.speedrun.rally.service.ProductoService;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;


@RestController
@RequestMapping("api/productos")
public class ProductoController {
    
    private final ProductoService productoService;

    public ProductoController(ProductoService productoService){
        this.productoService = productoService;
    }

    @GetMapping("/bajo-stock")
    public List<Producto> productosBajoStock(){
        return productoService.ObtenerProductosBajoStock();
    }
    
}
