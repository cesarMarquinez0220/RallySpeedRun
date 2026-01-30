package com.speedrun.rally.service;

import java.math.BigDecimal;
import java.util.List;

import org.springframework.stereotype.Service;

import com.speedrun.rally.model.Producto;
import com.speedrun.rally.repository.ProductoRepository;

@Service
public class ProductoService {
    private final ProductoRepository productoRepository;

    public ProductoService(ProductoRepository productoRepository){
        this.productoRepository = productoRepository;

    }

    public List<Producto> ObtenerProductosBajoStock(){
        return productoRepository.findByStockLessThan(new BigDecimal("5"));
    }
}
