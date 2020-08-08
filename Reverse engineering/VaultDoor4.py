values_row1 = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98]
pw_row1 = ''.join([chr(c) for c in values_row1])

print(pw_row1)


values_row2 = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
pw_row2 = ''.join([chr(c) for c in values_row2])

print(pw_row2)


values_row3 = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o67 , 0o141]
pw_row3 = ''.join([chr(c) for c in values_row3])

print(pw_row3)


values_row4 = ['1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b']
pw_row4 = ''.join(c for c in values_row4)

print(pw_row4)


pw = pw_row1 + pw_row2 + pw_row3 + pw_row4

print(pw)

'''This one is solvable through manually looking through an ascii table like this one here:
http://www.asciitable.com/
I used te chr() function that converts any number to its ascii character pendant, to solve it. 

Java challenge code for reference:
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 067 , 0141,
            '1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

'''