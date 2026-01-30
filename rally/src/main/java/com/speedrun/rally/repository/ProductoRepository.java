package com.speedrun.rally.repository;

import java.math.BigDecimal;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.speedrun.rally.model.Producto;

public interface ProductoRepository extends JpaRepository<Producto, String>{
    List<Producto> findByStockLessThan(BigDecimal stock);
}
