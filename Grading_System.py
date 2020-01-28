'''S1,S2,S3,S4 and S5 are the five subjects, we have to provede the marks as input'''
S1 = input('Enter the marks for the subject S1 ')
S2 = input('Enter the marks for the subject S2 ')
S3 = input('Enter the marks for the subject S3 ')
S4 = input('Enter the marks for the subject S4 ')
S5 = input('Enter the marks for the subject S5 ')
'''Percentage is denoted by Perc and can be calculated by the following formula'''
Perc = ((int(S1)+int(S2)+int(S3)+int(S4)+int(S5))/5)
'''Grades are assigned as A,B,C,D and E, according to some set rules'''
if Perc >= 90:
    print('Grade is: A')
elif 70 < Perc < 90:
    print('Grade is: B')
elif 50 < Perc < 70:
    print('Grade is: C')
elif 30 < Perc < 50:
    print('Grade is: D')
else:
    print('Grade is: E')