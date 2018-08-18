/*
 * gcc ch21.c -lcrypt -o ch21
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <crypt.h>
#include <sys/types.h>
#include <unistd.h>

int main (int argc, char *argv[]) {
    char pid[16];
    char *args[] = { "/bin/bash", "-p", 0 };
    char ch[33]; 
    scanf("%s",ch);
    //printf("%s\n",ch);

    //snprintf(pid,sizeof(pid), "%i",5108);
    //printf("%s\n",crypt(pid,"$1$awesome"));
    
    
    for(int i=100;i<100000;i++){
    
    	snprintf(pid, sizeof(pid), "%i", i);
    	if (strcmp(ch, crypt(pid, "$1$awesome")) == 0) {
		//printf("this is :%d\n",i);
    		snprintf(pid,sizeof(pid), "%i",i+2);
    		printf("%s\n",crypt(pid,"$1$awesome"));
		break;
	}
    }

    return 0;
}
