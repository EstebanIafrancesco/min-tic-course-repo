package com.esteban.recuperacion;

public class CafeExportacion extends Cafe {
    private Integer CIF_BASE = 20;
    private Integer cif; 
    private boolean VERDE = false;
    private boolean verde;
    
    public CafeExportacion(){
        this.peso = this.PESO_BASE;
        this.precioBase = this.PRECIO_BASE; 
        this.calidadC = this.CALIDAD_C_BASE;
        this.cif = this.CIF_BASE;
        this.verde = this.VERDE;
        this.tipo = " ";
    }

    public CafeExportacion(Double precioBase, Integer peso){
        this.peso = peso;
        this.precioBase = precioBase;
        this.calidadC = this.CALIDAD_C_BASE;
        this.cif = this.CIF_BASE;
        this.verde = this.VERDE;
        this.tipo = "exportacion";

    }

    public CafeExportacion(Double precioBase, Integer peso, char calidadC, Integer cif, boolean verde){
        this.peso = peso;
        this.precioBase = precioBase;
        this.calidadC = calidadC;
        this.cif = cif;
        this.verde = verde;
    }

    public Double calcularPrecio(){
        Double adicion = 0.0;
        adicion = super.calcularPrecio();
        if (this.verde == true) {
            adicion += 50;
        }
        if (this.cif > 40) {
            adicion += this.precioBase * 0.3;
        }
        return adicion;
    }
}
