package com.esteban.recuperacion;

public class CafeNacional extends Cafe {

    private boolean TOSTADO = false;
    private boolean tostado;

    public  CafeNacional() {
        this.peso = PESO_BASE;
        this.calidadC = this.CALIDAD_C_BASE;
        this.precioBase = this.PRECIO_BASE;
        this.tostado = this.TOSTADO;
        this.tipo = "nacional";
    }

    public  CafeNacional(Double precioBase, Integer peso) {
        this.peso = peso;
        this.precioBase = precioBase;
        this.tostado = this.TOSTADO;
        this.tipo = "nacional";
    }

    public  CafeNacional(Double precioBase, Integer peso, char calidadC, boolean tostado) {
        this.peso = peso;
        this.precioBase = precioBase;
        this.calidadC = calidadC;
        this.tostado = tostado;
        this.tipo = "nacional";
    }

    public Double calcularPrecio(){
        Double adicion = 0.0;
        adicion = super.calcularPrecio();
        if (this.tostado == true) {
            adicion += 50;
        }
        return adicion;


    }
}
