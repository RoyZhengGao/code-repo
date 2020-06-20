#!/bin/bash

###### for loop ######
for ((i=0; i<10; i++)); do
	touch test_$i.txt
done

###### read from terminal and print out ######
echo "What is your name?"
read PERSON
echo "Hello, $PERSON"

###### function without return value ######
demoFun(){
    echo "这是我的第一个 shell 函数!"
}
echo "-----函数开始执行-----"
demoFun
echo "-----函数执行完毕-----"

###### function with return value ######
function demoFun2(){
 echo "这是我的第二个 shell 函数!"
 expr 1 + 1 # or return `expr 1 + 1`
}
a=`demoFun2` 
echo $a

###### function with parameters ######
funWithParam(){
	echo "The value of the first parameter is $1 !" 
	echo "The value of the tenth parameter is $10 !"
	echo "The value of the tenth parameter is ${10} !"
	echo "The value of the eleventh parameter is ${11} !"
	echo "The amount of the parameters is $# !"  # 参数个数
echo "The string of the parameters is $* !"  # 传递给函数的所有参数
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73




