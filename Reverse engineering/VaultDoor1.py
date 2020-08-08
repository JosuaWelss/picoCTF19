
s = "password.charAt(00)  == 'd' &&password.charAt(29)  == '7' &&password.charAt(04)  == 'r' &&password.charAt(02)  == '5' &&password.charAt(23)  == 'r'\
               &&password.charAt(03)  == 'c' &&password.charAt(17)  == '4' &&password.charAt(01)  == '3' &&password.charAt(07)  == 'b' &&password.charAt(10)  == '_' \
               &&password.charAt(05)  == '4' &&password.charAt(09)  == '3' &&password.charAt(11)  == 't' &&password.charAt(15)  == 'c' &&password.charAt(08)  == 'l' \
               &&password.charAt(12)  == 'H' &&password.charAt(20)  == 'c' &&password.charAt(14)  == '_' &&password.charAt(06)  == 'm' &&password.charAt(24)  == '5' \
               &&password.charAt(18)  == 'r' &&password.charAt(13)  == '3' &&password.charAt(19)  == '4' &&password.charAt(21)  == 'T' &&password.charAt(16)  == 'H' \
               &&password.charAt(27)  == '1' &&password.charAt(30)  == 'f' &&password.charAt(25)  == '_' &&password.charAt(22)  == '3' &&password.charAt(28)  == 'e' \
               &&password.charAt(26)  == '5' &&password.charAt(31)  == 'd'"



def takeFirst(elem):
    return elem[0]

x = s.split("&&")


sub_list = []
for i in range(0, len(x)):

    sub_tuple = (x[i][16] + x[i][17], x[i][25])
    sub_list.append(sub_tuple)

sub_list = sorted(sub_list)

flag = ''
for i in range(len(sub_list)):
    flag += str(sub_list[i][1])

print(flag)

"""To crack Vault Door 1 you can also just read the solution from the screen, but I thought it is more fun to let a program do the sorting. 
I made some changes to the string (adding spaces and 0s) to make it more pleasing to look at. After splitting the string at the && we can easily create tuples from it wich in a result we append to a list.
After sorting the list, it is a peace of cake to read it out with a simple loop and string concatenation


Challenge java code for reference:

import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
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

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '7' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '1' &&
               password.charAt(30) == 'f' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == 'e' &&
               password.charAt(26) == '5' &&
               password.charAt(31) == 'd';
    }
}

"""

