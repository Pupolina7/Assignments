#include <stdio.h>
#include <string.h>

//creating structure for collecting information about players
struct player{
    char name[800];
    int teamNumb;
    int power;
    unsigned short visibility;
};

int main() {
    //reading the input file
    FILE *fi = fopen("input.txt", "r");
    //creating the output file
    FILE *fo = fopen("output.txt", "w");
    int n=100;
    //scanning the number of teams
    fscanf (fi, "%d\n", &n);
    if(n==100){
        fprintf(fo, "Invalid inputs\n");
        fclose(fi);
        fclose(fo);
        return 0;
    }
    //checking if the number of teams satisfy the condition
    if(n < 1 || n > 10){
        fprintf(fo, "Invalid inputs\n");
        fclose(fi);
        fclose(fo);
        return 0;
    }
    //creating array for magicians names
    char mug_names[n][1000];//mug_names[number of the team][]
    //scanning magicians names
    for (int i = 0; i < n; i++) {
        strcpy(mug_names[i],"0");
        fscanf(fi,"%s\n",mug_names[i]);
        if(strcmp(mug_names[i],"0\0")==0){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //creating local variable for the length of the current name
        unsigned int length;
        length = strlen(mug_names[i]);
        //checking if name really exist
        if(length==0){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking if the length of the name satisfy the length condition
        if(length < 2 || length > 20){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking that all names start with capital letter
        if((int)mug_names[i][0] < 65 || (int)mug_names[i][0] > 90){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking if all other letters are english letters
        for(int j = 1; j < length; j++){
            if((int)mug_names[i][j] < 65 || ((int)mug_names[i][j] > 90 && (int)mug_names[i][j] < 97) ||(int)mug_names[i][j] > 122){
                fprintf(fo, "Invalid inputs\n");
                fclose(fi);
                fclose(fo);
                return 0;
            }
        }
    }
    //creating global variable for the number of players
    int m=200;
    //scanning the number of players
    fscanf(fi,"%d\n", &m);
    if(m==200){
        fprintf(fo, "Invalid inputs\n");
        fclose(fi);
        fclose(fo);
        return 0;
    }
    //checking if number of players satisfy the condition
    if(m < n || m > 100){
        fprintf(fo, "Invalid inputs\n");
        fclose(fi);
        fclose(fo);
        return 0;
    }
    //creating array of structures for collecting information about players
    struct player Player[m];
    //scanning information about players
    for(int i = 0; i < m; i++){
        //scanning players name
        strcpy(Player[i].name,"0");
        fscanf(fi, "%s\n", Player[i].name);
        if(strcmp(Player[i].name,"0\0")==0){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //creating local variable for the length of the current name
        unsigned int length;
        length = strlen(Player[i].name);
        //checking if name really exist
        if(length==0){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking if the length of the name satisfy the length condition
        if(length < 2 || length > 20){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking that name start with capital letter
        if((int)Player[i].name[0] < 65 || (int)Player[i].name[0] > 90){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking if all other letters are english letters
        for(int j = 1; j < length; j++){
            if((int)Player[i].name[j] < 65 || ((int)Player[i].name[j] > 90 && (int)Player[i].name[j] < 97) ||(int)Player[i].name[j] > 122){
                fprintf(fo, "Invalid inputs\n");
                fclose(fi);
                fclose(fo);
                return 0;
            }
        }
        //scanning players team number
        Player[i].teamNumb=20;
        fscanf(fi, "%d\n", &Player[i].teamNumb);
        if(Player[i].teamNumb==20){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking if team number satisfy the condition
        if(Player[i].teamNumb < 0 || Player[i].teamNumb >= n){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //scanning players power
        Player[i].power=-1;
        fscanf(fi, "%d\n", &Player[i].power);
        if(Player[i].power==-1){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking if players power satisfy the condition
        if(Player[i].power < 0 || Player[i].power > 1000){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //creating string for scanning visibility
        char bool[1000];
        strcpy(bool,"0");
        //scanning players visibility
        fscanf(fi, "%s\n", bool);
        if(strcmp(bool,"0\0")==0){
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //comparing visibility with true and false to use 0 and 1
        if(strcmp(bool,"True\0")==0){
            Player[i].visibility=1;
        }
        else if(strcmp(bool,"False\0")==0){
            Player[i].visibility=0;
        }
        else{
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
    }
    //creating arrays for actions:
    //action[][0]-attack
    //action[][1]-heal
    //action[][2]-super
    //action[][3]-flip_visibility
    char action1[10010][4][220]={0};//first player in the action
    char action2[10010][4][220]={0};//second player in the action
    //scanning actions
    int test1, test2;
    unsigned int l=0;
    char str[200]="hello";
    int count=0;
    //scanning and performing actions while it's not the end of the file
    while(fscanf(fi,"%s", str)!=EOF){
        //scanning attack action members
        if(strcmp(str,"attack\0")==0){
            fscanf(fi,"%s",action1[count][0]);
            fscanf(fi,"%s\n",action2[count][0]);
            if(strlen(action1[count][0])==0 || strlen(action2[count][0])==0){
                fclose(fo);
                fo=fopen("output.txt","w");
                fprintf(fo, "Invalid inputs\n");
                fclose(fi);
                fclose(fo);
                return 0;
            }
            //performing attack action
            else{
                test1=0,test2=0;
                for(int k = 0; k < m; k++){
                    //looking for the players in attack action
                    if(strcmp(action1[count][0],Player[k].name)==0){
                        test1=1;
                        for(int j = 0; j < m; j++){
                            if(strcmp(action2[count][0],Player[j].name)==0){
                                test2=1;
                                //checking all cases when players cannot attack
                                if(Player[k].visibility==0){
                                    fprintf(fo,"This player can't play\n");
                                }
                                else if(Player[k].power==0 ){
                                    fprintf(fo,"This player is frozen\n");
                                }
                                //attack action (comparing powers, gaining power of one player and freezing other player
                                else if(Player[j].visibility==0){
                                    Player[k].power=0;
                                }
                                else if(Player[k].power > Player[j].power){
                                    Player[k].power=2*Player[k].power-Player[j].power;
                                    if(Player[k].power>1000){
                                        Player[k].power=1000;
                                    }
                                    Player[j].power=0;
                                }
                                else if(Player[k].power < Player[j].power){
                                    Player[j].power=2*Player[j].power-Player[k].power;
                                    if(Player[j].power>1000){
                                        Player[j].power=1000;
                                    }
                                    Player[k].power=0;
                                }
                                    //freezing both players
                                else if(Player[k].power==Player[j].power){
                                    Player[k].power=0;
                                    Player[j].power=0;
                                }
                            }
                        }
                    }
                }
                if(test1==0 || test2==0){
                    fclose(fo);
                    fo=fopen("output.txt", "w");
                    fprintf(fo, "Invalid inputs\n");
                    fclose(fi);
                    fclose(fo);
                    return 0;
                }
            }
        }
            //scanning flip_visibility action
        else if(strcmp(str,"flip_visibility\0")==0){
            fscanf(fi,"%s\n",action1[count][3]);
            if(strlen(action1[count][3])==0){
                fclose(fo);
                fo=fopen("output.txt","w");
                fprintf(fo, "Invalid inputs\n");
                fclose(fi);
                fclose(fo);
                return 0;
            }
            //performing flip_visibility action
            else{
                test1=0;
                for(int i = 0; i < m; i++){
                    if(strcmp(action1[count][3],Player[i].name)==0){
                        test1=1;
                        //checking the case when player cannot change visibility
                        if(Player[i].power==0){
                            fprintf(fo,"This player is frozen\n");
                        }
                        //changing visibility
                        else {
                            unsigned short old_vis = Player[i].visibility;
                            Player[i].visibility = 1 - old_vis;
                        }
                    }
                }
                if(test1==0){
                    fclose(fo);
                    fo=fopen("output.txt", "w");
                    fprintf(fo, "Invalid inputs\n");
                    fclose(fi);
                    fclose(fo);
                    return 0;
                }
            }
        }
            //scanning heal action members
        else if(strcmp(str,"heal\0")==0){
            fscanf(fi,"%s", action1[count][1]);
            fscanf(fi,"%s\n", action2[count][1]);
            if(strlen(action1[count][1])==0 || strlen(action2[count][1])==0){
                fclose(fo);
                fo=fopen("output.txt","w");
                fprintf(fo, "Invalid inputs\n");
                fclose(fi);
                fclose(fo);
                return 0;
            }
            //performing heal action
            else{
                test1=0,test2=0;
                for(int k = 0; k < m; k++){
                    //looking for the players in heal action
                    if(strcmp(action1[count][1],Player[k].name)==0){
                        test1=1;
                        for(int j = 0; j < m; j++){
                            if(strcmp(action2[count][1],Player[j].name)==0){
                                test2=1;
                                //checking all cases when players cannot heal
                                if(Player[k].visibility==0){
                                    fprintf(fo,"This player can't play\n");
                                }
                                else if(Player[k].power==0){
                                    fprintf(fo,"This player is frozen\n");
                                }
                                else if(Player[k].teamNumb!=Player[j].teamNumb){
                                    fprintf(fo, "Both players should be from the same team\n");
                                }
                                else if(Player[k].name==Player[j].name){
                                    fprintf(fo, "The player cannot heal itself\n");
                                }
                                //healing action (power ceil if needs)
                                else {
                                    Player[j].power=Player[j].power+(Player[k].power/2)+(Player[k].power%2);
                                    Player[k].power=Player[k].power/2+(Player[k].power%2);
                                    if(Player[j].power>1000){
                                        Player[j].power=1000;
                                    }
                                }
                            }
                        }
                    }
                }
                if(test1==0 || test2==0){
                    fclose(fo);
                    fopen("output.txt", "w");
                    fprintf(fo, "Invalid inputs\n");
                    fclose(fi);
                    fclose(fo);
                    return 0;
                }
            }
        }
            //scanning super action
        else if(strcmp(str,"super\0")==0){
            fscanf(fi,"%s", action1[count][2]);
            fscanf(fi,"%s\n", action2[count][2]);
            if(strlen(action1[count][2])==0 || strlen(action2[count][2])==0){
                fclose(fo);
                fo=fopen("output.txt","w");
                fprintf(fo, "Invalid inputs\n");
                fclose(fi);
                fclose(fo);
                return 0;
            }
            //performing super action
            else{
                test1=0,test2=0;
                for(int k = 0; k < m; k++){
                    //looking for players in super action
                    if(strcmp(action1[count][2],Player[k].name)==0){
                        test1=1;
                        for(int j = 0; j < m; j++){
                            if(strcmp(action2[count][2],Player[j].name)==0){
                                test2=1;
                                //checking all cases when players cannot make super action
                                if(Player[k].visibility==0){
                                    fprintf(fo,"This player can't play\n");
                                }
                                else if(Player[k].power==0){
                                    fprintf(fo,"This player is frozen\n");
                                }
                                else if(Player[k].teamNumb!=Player[j].teamNumb){
                                    fprintf(fo, "Both players should be from the same team\n");
                                }
                                else if(Player[k].name==Player[j].name){
                                    fprintf(fo, "The player cannot do super action with itself\n");
                                }
                                //healing
                                else{
                                    Player[k].power=Player[k].power+Player[j].power;
                                    if(Player[k].power>1000){
                                        Player[k].power=1000;
                                    }
                                    //"deleting" the second in super action players name
                                    strcpy(Player[j].name,"");
                                    Player[j].power=0;
                                    Player[j].teamNumb=12;
                                    Player[k].visibility=1;
                                    //changing the name after super action
                                    sprintf(Player[k].name,"%s%d","S_",l);
                                    l++;
                                }
                            }
                        }
                    }
                }
                if(test1==0 || test2==0){
                    fclose(fo);
                    fo=fopen("output.txt", "w");
                    fprintf(fo, "Invalid inputs\n");
                    fclose(fi);
                    fclose(fo);
                    return 0;
                }
            }
        }
            //if none scanned string didn't satisfy given actions output "Invalid inputs"
        else{
            fclose(fo);
            fo=fopen("output.txt","w");
            fprintf(fo, "Invalid inputs\n");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        count++;
    }
    //checking if number of actions satisfy given condition
    if(count>1000){
        fclose(fo);
        fo=fopen("output.txt","w");
        fprintf(fo,"Invalid inputs");
        fclose(fi);
        fclose(fo);
        return 0;
    }
    //creating an array for counting teams powers
    long long team_power[12]={0};
    //counting teams powers
    for(int i = 0; i < m; i++){
        team_power[Player[i].teamNumb] += Player[i].power;
    }
    //creating variables for storing maximum power and number of the team with maximum power
    long long max=0;
    int Team=0;
    //creating "Flag" variable to check if there is not only one team with maximum power
    int Flag=0;
    //looking for maximum power of the team and its number
    for(int i = 0; i < n; i++){
        if(team_power[i]>max){
            max=team_power[i];
            Team=i;
            Flag=0;
        }
        else if(team_power[i]==max){
            Flag=1;
        }

    }
    //outputting "It's a tie" if there are many teams with maximum power
    if(Flag==1){
        fprintf(fo,"It's a tie\n");
    }
        //otherwise, outputting winning team
    else{
        fprintf(fo,"The chosen wizard is %s\n", mug_names[Team]);
    }
    fclose(fi);
    fclose(fo);
    return 0;
}
