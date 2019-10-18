/* 
 * Given an array of row X col size defined as array
 * where 1 denotes filled parking and 0 denotes empty.
 * Figure out the minium distance to nearest parking gate.
 *
*/
void finding_minimun(int grow,int gcol)
{
  global array, row, col;
  int grow,gcol,rowdist,coldist,distance,adderr,adderc,i,j,flag=0;
  distance=0;
  printf("\n********_________*************\n");
  printf("gate is at location%d,%d",grow,gcol);
  printf("\n************--------************\n");
 
  do{
      /*---------controls the increment of radius-------*/
      rowdist=distance;
      coldist=0;
      do{
          /*----for each distance start at top of diamond--------*/
          adderr=rowdist;
          adderc=coldist;
          for(i=0;i<2;i++)
          /*-----makes the adder-r to move down and then up----*/
          {
              for(j=0;j<2;j++)
              /*----makes the column go down and then up----*/
              {
              if((((grow+adderr)>=0)&&((grow+adderr)<row)) && (((gcol+adderc)>=0)&&((gcol+adderc)<column))&&(flag==0))
              /*---checking the data to be in boundary of array----*/
                  {
                  if(array[grow+adderr][gcol+adderc]==0)
                      {
                          array[grow+adderr][gcol+adderc]=1;   flag=1;
                          printf("\n%d-%d\n slot is free",grow+adderr,gcol+adderc);
                      }       
                  }
              /*--end of checking iff---*/
              adderc=-adderc;
              }
          adderr=-adderr;
          }
          rowdist--;  coldist++;
        }while(rowdist>=0&&flag==0);
    distance++;
  }while(distance<=row+column&&flag==0);
}
