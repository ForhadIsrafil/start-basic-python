#===== declaring a string value and print their elements =====# 
str = 'python Course'
print(str)
print(str[0],str[2],str[-1], str[-3])

name = 'shuvro baset'
print ( name.title() ) # showing value as a title case
print ( name.upper() ) # showing value uppercase
print ( name.lower() ) # showing value lower case
print ( name.upper().lower().title() ) # 3 operation finally last one is shown

# == string concatenation ======= #

frst_name = '   Abdul'
last_name = 'baset'
name1 = frst_name.lstrip() + ' ' + last_name# space hiding left strip by calling lstrip function ........./rstrip is for hide right side of space
print(name1)
# if I use only strip then, all the spaces will be hide
hidename = '    s h u v r o   '
hide = hidename.strip()
print(hide)
#=====Note : it will hide only first and last spaces, not inner spaces
#======== use quotation in string value ======== 
abs = "hi! are u understand it. won't u ? "
sba = 'hi! are u understand it. won\'t u ? '
print(abs)
# note : use different type of quotation for this 

#========= Find word in sentence ====== # 
sntnce = "check my word from here using find function"
print( sntnce.find('word'))# in this method it will show the index number . if there is no word then it will show (-1)
#===== replacing word using replace function ==== 
sntnce = sntnce.replace('check', 'finding')
print(sntnce)
# note : if there is multiple same word and i wanna change every same word then we have to use replaceAll function

# print multiple value with seperate them 
print("ami ", " baset",sep=".")
x = 'shuvro'
y = 'baset'
z = 'python programmer'
print(x,y,z, sep='| ' )

#string interpolation 
me = "{nam}'s age is {age}"
print(me.format(nam='baset', age=27))
me = '%s\'s age is %d'
print (me % ('baset',27))

#slice 
slce = "shuvo ratri"
pushpo = slce[6:]
print(pushpo)
