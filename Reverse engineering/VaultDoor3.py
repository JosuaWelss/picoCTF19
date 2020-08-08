s = 'jU5t_a_sna_3lpm17ga45_u_4_mbrf4c'


part1 = s[0:8]
part2 = s[15:7:-1]
part3 = s[30:14:-2]
part4 = s[31:16:-2]

finalpart = part1 + part2
counter1 = 0
counter2 = 0
for i in range(16):
    if i % 2 == 0:
        finalpart+=part3[counter1]
        counter1 +=1
    else:
        finalpart += part4[len(part4)-counter2-1]
        counter2 += 1

print(part1)
print(part2)
print(part3)
print(part4)

print(finalpart)


exil = bool(input())



'''You can also do this challenge manually through creating tables and sorting for inputs.
I decided to revert the password into 4 parts(one for every loop) with slices.
After this I use a loop with 2 different counters to sort  for the right input


Challenge java code for reference:

import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        System.out.println(password.length());
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
            System.out.println(buffer[i]);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
            System.out.println(buffer[i]);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
            System.out.println(buffer[i]);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
            System.out.println(buffer[i]);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm17ga45_u_4_mbrf4c");
    }
    
    
}
'''