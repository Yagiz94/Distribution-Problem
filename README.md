# Corona_DP_Problem
A DP solution for homework distribution problem during coronavirus days.

# Description:

A HW has to be assigned and evaluated in these Corona times. An Assistant with mask will take sterilized homeworks from the Professor of the course and distribute it to the students. There are N students in the course. All the students are located in diﬀerent places and since they are doing social distancing they do not go anywhere and stay at home and also do not meet any friend. The Assistant has to distribute the HW to all the students one by one. The assistant waits for the student to complete her/his homework and take it back. Student i needs xi minutes to complete the homework. Of course, it takes some time to go from one place to another and the assistant wants to minimize his time for doing this job. Therefore, he will take the HW from the Professor, go to each student exactly once and fnally bring back together all the solutions (of the students) to the Professor at the very end. Please help this Assistant in this work to minimize his time for doing this duty.

Model this problem as an IP problem. (Please clearly state that which are parameters and which are decision variables)

Model this problem as an DP problem. (Please clearly write functional equations and parameters and decision variables

For each student generate some random xi ∈ [300,500] only once. Generate it for N = 75 students. For problem instances with smaller number of students, use this same data as follows: Use the ﬁrst 5 values for N = 5, ﬁrst 10 for N = 10 and so on. Now, for each N = 5,10,...,75 number of students, generate bN ln(N))c diﬀerent random travel time matrices (each such matrix will provide a problem instance for you to use in your experiments) with random travel times in the range [100,300] between any pair of of those N students and between each student and the professor, e.g., for N = 5 generate 8 travel time matrices (8 instances).

Solve IP problem that you modelled.

Solve DP problem according to your model.
