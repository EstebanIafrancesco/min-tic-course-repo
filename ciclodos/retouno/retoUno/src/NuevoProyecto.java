public class NuevoProyecto {
    // -----------------------------------------------------------------
    // Atributos
    double pMonto;
    double pInteres;
    int pPeriodo;
    double diferencia;
    double interesSimple;
    double interesCompuesto;
    // -----------------------------------------------------------------
    // -----------------------------------------------------------------
    // Métodos
    // -----------------------------------------------------------------
    public NuevoProyecto( int pPeriodo, double pMonto, double pInteres){
        pMonto = this.pMonto;
        pInteres = this.pInteres;
        pPeriodo = this.pPeriodo;

    }
    public double calcularInteresSimple(){
        return  Math.round(pMonto*pInteres+pPeriodo);
    }
    // calacularInteresCompuesto(){
    //     interesCompuesto = Math.round(pMonto*((Math.pow((1+pInteres), pPeriodo))-1));
    // }
    
    /**
    * Método para comparar la diferencia en el total de intereses generados para
    el proyecto.
    * @return Respuesta al Reto.
    */
    public String compararInversion ( int pPeriodo, double pMonto, double  pInteres ){
        
        return "hola";
        
    }
    // public double compararInversion (){
    //     //codigo
    // }
        public static void main(String[] args){
        //Instanciación de clase y uso de métodos
            NuevoProyecto np = new NuevoProyecto(5, 12.5 ,33.6 );
            System.out.println(np.calcularInteresSimple());

        }
    }

    