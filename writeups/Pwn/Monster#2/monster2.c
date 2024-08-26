#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

void ignore_me_init_buffering() {
        setvbuf(stdout, NULL, _IONBF, 0);
        setvbuf(stdin, NULL, _IONBF, 0);
        setvbuf(stderr, NULL, _IONBF, 0);
    }   
void kill_on_timeout(int sig) {
    if (sig == SIGALRM) {
        printf("[!] Anti DoS Signal. Patch me out for testing.");
        exit(0);
    }
}
void ignore_me_init_signal() {
    signal(SIGALRM, kill_on_timeout);
    alarm(60);
}

void print_monster() {
    printf("⠀⠀⠀⠀⢶⡆⠀⠀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n");
    printf("⠀⠀⠀⢠⣾⣿⣦⣤⣭⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n");
    printf("⠀⠀⣰⠏⠀⢹⣻⣭⣭⡧⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n");
    printf("⠀⢠⠏⠀⠴⠚⣷⣿⣿⠀⠀⢀⡤⠖⠛⠹⠶⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n");
    printf("⠀⡏⠀⠀⠀⡼⠉⠉⠁⢀⡴⠋⠀⠀⠤⢄⡀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n");
    printf("⠀⡇⠀⠀⠀⢧⡀⠀⢠⠎⠀⢠⣤⡞⠒⠲⡌⠃⠀⠀⠀⠱⢤⡀⠀⢀⣀⣀⣀⠀⠀\n");
    printf("⠀⣧⠀⠀⠀⠀⠙⠲⠏⠀⢀⡀⠙⣇⠀⠀⢘⡶⠆⣤⠤⠔⢲⣯⡖⠉⠀⠀⠈⢧⠀\n");
    printf("⠀⢺⣦⡀⠀⠂⠀⠀⠀⠀⠀⢠⣄⠼⣗⠒⠋⠀⠀⠹⣄⣠⣿⡋⡀⢠⣤⡆⠀⢸⠀\n");
    printf("⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⠦⣠⠴⣄⢀⣠⣄⣸⠇⠀⣳⣿⣧⠈⢹⠁\n");
    printf("⠀⠀⠀⠘⠶⡆⠀⠆⢶⣴⠀⢾⠀⠀⠀⠀⠀⠀⠈⠉⡼⡭⣭⡴⠖⠼⠛⣿⣿⠏⠀\n");
    printf("⠀⠀⠀⠀⠀⢻⠀⠀⠀⠁⠀⠘⡄⠀⣠⢤⣀⡤⡄⢸⣿⣿⠋⠀⠀⠀⠀⠙⠁⠀⠀\n");
    printf("⠀⠀⠀⠀⠀⣏⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠘⠛⢱⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀\n");
    printf("A bigger scarier monster blocks your path!\n\n");
}

int main() {
    char buffer[16];
    int magicWord = 0x0;

    ignore_me_init_buffering();
    ignore_me_init_signal();

    print_monster();
    printf("You have a wand in your hand. What spell do you want to cast? Remember to include a strong magic word!\n");
    fgets(buffer, 40, stdin);

    //String conversion - Ignore
    char magicWord_str[5];
    magicWord_str[0] = (magicWord >> 24) & 0xFF;
    magicWord_str[1] = (magicWord >> 16) & 0xFF;
    magicWord_str[2] = (magicWord >> 8) & 0xFF;
    magicWord_str[3] = magicWord & 0xFF;
    magicWord_str[4] = '\0'; 

    if (magicWord == 0x41425241)
	{
        printf("You crit the monster with your magic spellword %x ('%s' as ASCII values). You found the monster's weakness! Here comes the shell\n", magicWord, magicWord_str);
        system("/bin/sh");	
	}

	else if (magicWord == 0x41524241)
	{
		printf("You yell the correct magicWord, but for some reason it hits the monster in reverse: %x ('%s' as ASCII values), the monster laughs and slays you while gargling something about Endianness.", magicWord, magicWord_str);
	}
    
	else
	{
        printf("You yelled the wrong spell. ('magicWord' is %x ('%s' as ASCII values)). The monster slays you.", magicWord, magicWord_str);
	}

return 0;
}
