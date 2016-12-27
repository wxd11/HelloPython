#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python2
flag=True;
if 3<2:
     print flag
else:
     print not flag


ord('c');
chr(100);
u'bc'.encode('utf-8');
len('wwef');
'abc'.decode('utf-8');


list=[1,2,"34",[5,6,True]];
print list[0];
print list[-3];
print list;
list.append(7);
print list;
list.insert(3,'a');
print list;
list.pop();
print list;
list.pop(2);
print list;

tuple=(1,2,3);
print tuple;
print tuple[2];

t=(1,);
print t;
m=(1);
print m;

if 12>3:
     print True;
elif 12>9:
     print True;
else:
     print False;


s=input();
i=int(s);
if i>3:
     print True;
else:
     print False;


for index in list:
     print (index);


sum=0
for x in range(101):
    sum+=x;

print sum;

dict={"tom":89,"bob":99,"jack":11};
print dict;
print dict["tom"];

dict["lucy"]=77;
print dict;

s=set([1,1,2,3,4,5,3,5,6,2]);
print s;

print abs(-100);

#python3