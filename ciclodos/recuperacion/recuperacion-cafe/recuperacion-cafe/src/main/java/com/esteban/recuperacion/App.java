package com.esteban.recuperacion;

public class App 
{
    public static void main( String[] args )
    {
        // System.out.println( "Reto de recuperacion" );
        Cafe cafecito = new Cafe();
        System.out.println(cafecito.tipo);
        System.out.println(cafecito.calidadC);
        System.out.println(cafecito.peso);
        System.out.println(cafecito.precioBase);

        Cafe cafecito1 = new Cafe(200.0, 25);
        System.out.println(cafecito1.tipo);
        System.out.println(cafecito1.calidadC);
        System.out.println(cafecito1.peso);
        System.out.println(cafecito1.precioBase);

        Cafe cafecito2 = new Cafe(355.3 , 800);
        System.out.println(cafecito2.tipo);
        System.out.println(cafecito2.calidadC);
        System.out.println(cafecito2.peso);
        System.out.println(cafecito2.precioBase);
    }
}
