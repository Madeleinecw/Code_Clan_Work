public class Runner {

    public static void main(String[] args) {
        Planet planet = new Planet();
        planet.setName("Mars");
        planet.setSize(908973);
        System.out.println(planet.getName());
        System.out.println(planet.explode());
        System.out.println(planet.getName() + " is " + planet.getSize() + "cm");
    }

}
