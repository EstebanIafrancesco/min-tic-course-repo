public class NuevoProyecto {
    // -----------------------------------------------------------------
    // Atributos
    // -----------------------------------------------------------------
    private double monto;
    private double interes;
    private int periodo;
    // -----------------------------------------------------------------
    // Métodos
    // -----------------------------------------------------------------

    // Constructores
    public NuevoProyecto(){

        this.monto = 0.0;
        this.interes = 0.0;
        this.periodo = 0;
    }
    public NuevoProyecto(int pPeriodo, double pMonto, double pInteres){
        this.monto = pMonto;
        this.interes = pInteres;
        this.periodo = pPeriodo;

    } 

    public double calcularInteresSimple(){
        double interesSimple = this.monto*this.interes*this.periodo/100;
        return  Math.round(interesSimple);
    }
    public double calcularInteresCompuesto(){
        double interesCompuesto = this.monto*((Math.pow((1+(this.interes/100)), this.periodo))-1);
        return  Math.round(interesCompuesto);
    }

    public double compararInversion ( int pPeriodo, double pMonto, double  pInteres){

        this.periodo = pPeriodo;
        this.monto = pMonto;
        this.interes = pInteres;

        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        return diferencia;
        
    }
    public double compararInversion(){
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        return diferencia;
    }

}
