filename = 'src.c'
iRange = 99999

head = '''#include <stdio.h>
int main(){
int a=0;
printf("input one number in 0~99999: ");
scanf("%d" ,&a);
switch(a){
'''

end = '''}
return 0;
}
'''

def putCase(i):
    digit = 0
    i = str(i)
    code = 'case ' + str(i) + ':{\n'
    for ch in i:
        digit += 1
        code += 'printf(\"Digit No.' + str(digit) + ' is: ' + ch + '\\n\");\n'
    code += 'printf(\"reversed is:' + i[::-1] +'\\n\");\n'
    code += 'break;\n'
    code += '}\n'
    return code

if __name__ == '__main__':
    code = ''
    code += head
    for j in range(iRange+1):
        code += putCase(j)
    code += end
    #print(code)
    with open(filename, 'w') as fd:
        fd.write(code)
    print("code generated with a total of " + str(len(code.splitlines())) + " lines.")
