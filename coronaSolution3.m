format compact
%problem variables
time = 0; % total time spent on the road to go student i
runTime = zeros(1, 15);
recursiveRunTime = zeros(1, 15);
resultTimeArray = zeros(1, 15);

n_array = zeros(1,15);
n_array(1)=5; n_array(2) = 10; n_array(3) = 15;
n_array(4)=20; n_array(5) = 25; n_array(6) = 30;
n_array(7)=35; n_array(8) = 40; n_array(9) = 45;
n_array(10)=50; n_array(11) = 55; n_array(12) = 60;
n_array(13)=65; n_array(14) = 70; n_array(15) = 75;

r = 1; %recursiveRuntime iteration
iterativeT = 1; %runTime iteration
n1 = 5;
limit = 75;

while n1<=limit
size1 = n1 + 1; % professor is also included in the timetravel matrix
completionTime1 = randi([300 500],n1,1); %this array will hold the completion time for homework of each student
finalTravelTime1 = zeros(size1);%its elements are initially zero
                                %after getting the average of the
                                %travelTime matrices, it will have values
                                %except zero.
deliveredHomework = zeros(1,n1); %initially no students delivered their homework. 
student = 0; %to iterate the students for distibuting homework

%calculate the # of the travel time matrices
numTravelTime1 = n1 * log(n1);
disp("# of travel time matrices is: " + int8(numTravelTime1));
numTravelTime1 = int8(numTravelTime1);%convert it into integer
timeTaken = zeros(1,n1);

%assign random values into completionTime1
for i=1:n1
    disp(completionTime1(i,1));
end

%create travel time matrices
travelTime1 = randi([100 300],numTravelTime1,size1,size1); % create 8x6x6 matrix

%create symetric matrix
for i=1:numTravelTime1
    for j=1:size1
        for a=1:size1
           travelTime1(i,j,a) = travelTime1(i,a,j);
        end
    end
end

for i=1:numTravelTime1
    disp(" ");
    disp("Matrix " + i + ":");
    for j=1:size1
        disp(" ");
        for a=1:size1
            if j == a
                travelTime1(i,j,a) = 0;
            end
            fprintf('%d ',travelTime1(i,j,a)); 
            %disp(travelTime1(i,j,a));
        end
    end
end

%next step is to obtain the average values of the time matrices
for i=1:size1
    for j=1:size1
        for a=1:numTravelTime1
            finalTravelTime1(i,j) = finalTravelTime1(i,j) + travelTime1(a,i,j);            
        end
        
    end
end

for i=1:size1
    for j=1:size1  
        finalTravelTime1(i,j) = finalTravelTime1(i,j)/(n1 * log(n1));           
    end
end

finalTravelTime1 = cast(finalTravelTime1,'uint8')

%next step is to find nearest student
flag = 0; %we are in the professor's office
b = 1; % to iterate the while loop
while allDelivered(deliveredHomework, n1) == false && b <= n1    
    tic
    if flag == 1
          [nTime, n_Index] = findNearestStudent(b+1, finalTravelTime1, deliveredHomework, flag,n1);
          timeTaken(1, n_Index) = nTime;
    end
    
    if flag == 0
        [nTime, n_Index] = findNearestStudent(b, finalTravelTime1, deliveredHomework, flag);
        timeTaken(1, n_Index) = nTime;
        flag = 1;
        
    end   
    
        
    disp("Nearest student is: " + n_Index);
    b = n_Index;
    deliveredHomework(1,b) = 1;
    
end
time1 = sum(timeTaken, 'all');
time2 = sum(completionTime1, 'all');
result1 = time1 + time2;
e = b+1;
time3 = finalTravelTime1(1,e);%we will go back to professor's office
result2 = zeros(1,2);
result2(1,1) = result1;
result2(1,2) = time3;
disp("Total time is: " + sum(result2, 'all'));
runTime(1,iterativeT) = toc;
iterativeT = iterativeT + 1;

for i=1:n1
    deliveredHomework(1,i) = 0;%I made it them again so that we can compute the result efficiently in recursive way.
end
%Compute total time with recursion

flag = 0;
b=1;

tic
b=recursiveTimeComputation(b, finalTravelTime1, deliveredHomework, flag, n1);
time1 = sum(timeTaken, 'all');
time2 = sum(completionTime1, 'all');
result1 = time1 + time2;
e = b+1;
time3 = finalTravelTime1(1,e);%we will go back to professor's office
result2 = zeros(1,2);
result2(1,1) = result1;
result2(1,2) = time3;
disp("Recursive Total time is: " + sum(result2, 'all'));
recursiveRunTime(1,r) = toc;
n1 = n1 + 5;
resultTimeArray(r) = sum(result2,'all');
r = r +1;
end

plot(n_array, resultTimeArray);
xlabel('N');
ylabel('Total Travel Time');

plot(n_array,runTime);
xlabel('N');
ylabel('Run Time of Non-Recursive Function');

%plot(n_array,recursiveRunTime);
%xlabel('N');
%ylabel('Run Time of Recursive Function');


function [lastIndex]=recursiveTimeComputation(b, finalTravelTime1, deliveredHomework, flag, n1)
   
 %recursive
 lastIndex = b;
 if allDelivered(deliveredHomework,n1) == false
    if flag == 1
          [nTime, n_Index] = findNearestStudent(b+1, finalTravelTime1, deliveredHomework, flag,n1);
          lastIndex = n_Index;
          timeTaken(1, n_Index) = nTime;
          deliveredHomework(1,n_Index) = 1;
          lastIndex=recursiveTimeComputation(n_Index, finalTravelTime1, deliveredHomework, flag, n1);
          
    end
    
    if flag == 0
        [nTime, n_Index] = findNearestStudent(b, finalTravelTime1, deliveredHomework, flag);
        lastIndex=n_Index;
        timeTaken(1, n_Index) = nTime;
        flag = 1;
        deliveredHomework(1,n_Index) = 1;
        lastIndex=recursiveTimeComputation(n_Index, finalTravelTime1, deliveredHomework, flag, n1);
        
    end  
        
    
 end
 
 %base case
 if allDelivered(deliveredHomework,n1) == true

     disp("The end...");
     return;
 end 
   
end

function [nearestTime, nearIndex] = findNearestStudent(index, finalTravelTime1, deliveredHomework, flag, n1)

  if flag==0
     temporaryArray = finalTravelTime1(index,:);
     %extract specified index from the temporary array
     %temporaryArray = temporaryArray(1,:);
     temporaryArray = nonzeros(temporaryArray);
     numElements = numel(temporaryArray);
     %sort the temporary array
     [sortedArray,I] = sort(temporaryArray,'ascend');
     
      disp("hellooooooo");
      %for i=1:length(sortedArray)
         %disp(sortedArray(i));
      %end
      %for i=1:length(I)
         %disp(I(i));
      %end
     
      nearestTime = sortedArray(1);
      nearIndex = I(1);
      return;
  end
  
  if flag == 1
     temporaryArray2 = finalTravelTime1(index,:); 
     %for i=1:numel(temporaryArray2)
         %disp(temporaryArray2(i));
     %end
     temporaryArray = zeros(1,n1);
     for i=2:(n1+1)
         temporaryArray(1,i-1) = temporaryArray2(1,i);
         %disp("Flag 1, temporaryArray element: " + temporaryArray(i-1));
     end
     [sortedArray,I2] = sort(temporaryArray,'ascend');
     sortedArray = nonzeros(sortedArray);
     I = zeros(1, n1-1);
     for i=2:n1
         I(i-1) = I2(i);
     end
     
     for check=1:numel(I)
         k = I(check);
         
         if deliveredHomework(k) == 0
             nearestTime = sortedArray(check);
             nearIndex = I(check);
             deliveredHomework(1,index) = 1;
             return;
         end     
         if deliveredHomework(I(check)) == 1
             check = check + 1;
             continue;
         end
             
     end
  end
 
  
end

function done = allDelivered(homework, numberOfStudents)
      student1 = 1;
      while student1 <= numberOfStudents
          if homework(student1) == 0
              done = false;
              return
          end
          
          student1 = student1 + 1;
      end
      done = true;
      return     
      
end

