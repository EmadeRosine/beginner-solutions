# consider a social media platform like instagram
# some post were stored in turple
post1=('Rosine','Zugerburge just released threads','10-7-2023')
post2=('Mike','thread already has millions of users','12-7-2023')
post3=('James','Zugerburge blocked Elon Musk thread account','13-7-2023')
# the set stores the followers and those following
Rose_followers={'Mike','James'}
Mike_followers={'Blinks','Esther','Rosine'}
James_followers={'Mike','Tony','Anslem','Junior'}

Rose_following={'Mike','James'}
Mike_following={'Blinks','Esther','Rosine'}
James_following={'Mike','Tony','Anslem','Junior'}
# profiles are stored in the dictionary
Roseprofile={'username':'Rosine','hobby':'listening to music','followers':Rose_followers,'following':Rose_following}
Mikeprofile={'username':'Mike','hobby':'traveling','followers':Mike_followers,'following':Mike_following}
Jamesprofile={'username':'James','hobby':'Dancing','followers':James_followers,'following':James_following}

# printing outputs
print('What is the full profile of ', post1[0]+': \n', Roseprofile)
print('when did Rose post:'+post1[2])
print('What is the full profile of ', post1[1]+': \n', Mikeprofile)
print('when did Mike post:'+post2[2])
print('What is the full profile of ', post1[2]+': \n', Jamesprofile)
print('when did James post:'+post3[2])


