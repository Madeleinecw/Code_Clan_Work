public class Runner {
    public static void main(String[] args) {
        Bear bear = new Bear("Balu");
        System.out.println(bear.getName());
        bear.setName("Baloo");
        System.out.println(bear.getName());
    }
}

