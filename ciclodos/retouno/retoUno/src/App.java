public class App {
    public static void main(String[] args) throws Exception {

        NuevoProyecto np = new NuevoProyecto(12, 10000000, 0.9);
        System.out.println("\n");
        System.out.println(np.calcularInteresSimple());
        System.out.println(np.calcularInteresCompuesto());
        System.out.println(np.compararInversion());
        
        System.out.println("\n");
    }
}
