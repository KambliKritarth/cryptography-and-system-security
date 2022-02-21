import java.util.*;
public class PasswordBruteForce{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String password = sc.nextLine();
        String str = "";
        int count = 0;
        for(int i = 0; i<4;i++){
            for(char ch = 'a';ch<='z';ch++){
                count++;
                if(ch == password.charAt(i)){
                    str += ch;
                    System.out.println("Password"+(str.length()!=4?" segment":"") +" is " + str +", deciphered in "+count+" iterations");
                }   
            }
        }
        sc.close();
    }
}