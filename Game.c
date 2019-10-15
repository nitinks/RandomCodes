#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define TEXTWIDTH 8
#define LINES 6
#define MAX_SIZE 50
#define FILENAME "n.txt"

int verify (char str[]);
void search(char str[]);
int search_ahead( char str[], int row, int col );
int search_right (char str[],int row,int col);
int search_left(char str[],int row,int col);
int search_down(char str[],int row,int col);
int search_up(char str[],int row,int col);

main()
{
    int choice;
    int error;
    char string[MAX_SIZE];

   while(1)
   {
            error=0;
            printf(" \n\n enter the string   ");
            gets(string);

            error=verify(string);  printf("error=%d\n",error);
            if(error==0)
                {
                   search(string);   /*---------go for searching ---------*/
                } 
                    

                if(error==0)
                {

                    do{ 
                            error=0;

                            printf("\ngive choice 1,retry  2.exit  ");
                             choice=getchar();   getchar();   fflush(stdin);
                             if(choice==50)
                            {
                                exit(0);
                            }


                           if(choice!=49&&choice!=50)
                            {
                                printf("\nwrong choice");  error=1;
                            }
                      }while(error==1);
                }
    }

}


/*-----verification of the input  string------*/
int verify (char str[])
{
int error=0;
int count=0;
printf("%s",str);
if(str[0]=='\0')
    {
        printf("\nerror in string");
        error=1;
        }
    while(str[count]!='\0')
        {
            if(str[count]<57&&str[count]>48)
                {
                    printf("\n numbers present in the string   ");
                    error=1;   break;
               }
        count++;
        }
      return(error);

}



/*-----------initiating the search process----------*/
void search(char str[])
{
FILE *fp;
fp=fopen(FILENAME,"r");
if(fp==NULL)
{
printf("file can not be opened  ");
exit(1);
}
int column=1;
int row=1;
int count=0;
int result;
int found=0;
char c;
fseek(fp,count,SEEK_SET);
c=fgetc(fp);
while(c!=EOF)
    {	
	/*----------if first letter matches-----*/
	if(c==str[0])
		{
                 result=search_ahead(str,row,column);/*---go to search ahead----*/
		 
		}
        found=found+result;
        count++;
        fseek(fp,count,SEEK_SET);
        c=fgetc(fp);
	
        if(c=='\n')
        {
        column=0;   row++;  
        }
        else
        {
        column++;
        }

    }
if(found==0)

    {
       printf("wrong text");/*------if not found in the files-------------*/
    }
    fclose(fp);

}



/*------searching ahead  going to up odwn right and left with current row  and column locations------*/
int search_ahead(char str[],int  row, int col)
{

int found=0;

        if(  search_right(str,row,col)   )
                {
                printf("FORWARD  at row=%d   column=%d \n ",row,col); found=1;
               }
       if(   search_left(str,row,col)    )
                {
                printf("BACKWARDS  at  row=%d  column=%d \n",row,col);  found=1; 
                }
        if(   search_down(str,row,col)    )
                {
                printf("DOWN  at row=%d   column=%d\n  ",row,col);    found=1;
                }
        if(  search_up(str,row,col)     )
                {   
                    printf("UP ta row=%d  column=%d \n  ",row,col);   found=1;
               }
return(found);
}


/*-search right---------*/
int search_right(char str[],int row,int col)
{   
FILE *fp;
fp=fopen(FILENAME,"rb+");
    char c;
    int count=0;
    int found=1;
    while(col<=TEXTWIDTH)
      { 
            fseek(fp,(   (9*(row-1))+(col-1)    ),SEEK_SET);/*-going to that element in file----*/
            c=fgetc(fp);
            if(str[count]=='\0')
                        {
                            break;
                        }
            if(c==str[count]  )
            {   
                   col++;  count++; /*--moving the column right-------*/;
            }
            else
            {
            found=0;
            break;
            }
      }
      if (col>TEXTWIDTH&&str[count]!='\0')
      {found=0;
      }
      fclose(fp);
return(found);
}



/*-------searching left ----------*/
int search_left(char str[],int row,int col)
{
FILE *fp;
fp=fopen(FILENAME,"rb+");
    char c;
    int count=0;
    int found=1;
    while(col>=1)
        {
            fseek(fp, (        (9*(row-1))+(col-1)   ),SEEK_SET);
            c=fgetc(fp);
            if(str[count]=='\0')
                    {
                            break;
                    }
            if(c==str[count]  )/*-checking the next elemnt-------*/
                {
                    col--;   count++;  /*-going left-----*/
                }
                else
                {
                found=0;
                break;
                }
        }
if(col<1&&str[count]!='\0')
{found=0;
}
        fclose(fp);
return(found);
}


/*------going down--------*/

int search_down(char str[],int row,int col)
{
FILE *fp;
fp=fopen(FILENAME,"rb+");
    char c;
    int count=0;
    int found=1;
    while(row<=LINES)/*-search till you reach the bottom of file----*/
        {
            fseek(fp, (        (9*(row-1))+(col-1)   ),SEEK_SET);/*-reaching element---*/
            c=fgetc(fp);
            if(str[count]=='\0')/*---if the string to be searched is read fully i.e. all letters are matched-*/
                    {
                            break;
                    }
            if(c==str[count]  )/*---if current element matches---*/
                {
                    row++;   count++;/*-------incrasing row i.e. going down to search next elemtnt---*/
                }
                else
                {
                found=0;
                break;
                }
        }
if(row>LINES&&str[count]!='\0')
{found=0;
}

        fclose(fp);
return(found);
}



int search_up(char str[],int row,int col)
{
FILE *fp;
fp=fopen(FILENAME,"rb+");
    char c;
    int count=0;
    int found=1;
    while(row>=1)
        {
            fseek(fp, (        (9*(row-1))+(col-1)   ),SEEK_SET);
            c=fgetc(fp);
            if(str[count]=='\0')
                    {
                            break;
                    }
            if(c==str[count]  )
                {
                    row--;   count++;//printf("ma up\n");
                }
                else
                {
                found=0;
                break;
                }
        }


        if(row<1&&str[count]!='\0')
        {
        found=0;
        }
       fclose(fp);
return(found);
}

