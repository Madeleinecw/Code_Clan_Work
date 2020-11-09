public class Planet {

    private String name;
    private int size;

    public void setName(String newName){
        this.name = newName;
    }

    public void setSize(int newSize){
        this.size = newSize;
    }

    public String getName(){
        return this.name;
    }

    public int getSize(){
        return this.size;
    }

    public String explode(){
        return "Boom!" + this.name + " has exploded!";
    }
}
